import sys
from collections import namedtuple, Counter
from itertools import count

class FormatError(RuntimeError):
    pass

def read_fasta(f):
    """
    Quick and dirty implementation of a FASTA reader.
    Does not fully conform to specifications.
    For each sequence, yields (name, seq),
    where name is a string with everything behind the '>',
    and seq is a string with the DNA sequence.
    """
    # wait for first '>'
    newname = None
    for line in f:
        if line.startswith(">"):
            newname = line.strip()[1:]
            break
    # forever
    while True:
        # check if another sequence is starting; escape if not.
        if newname is None:  break
        name, newname = newname, None
        seq = list()
        for line in f:
            if line.startswith(">"):
                newname = line.strip()[1:]
                break
            seq.append(line.strip())
        yield (name, "".join(seq))


def write_fasta(iterable_of_name_seq, seqwidth=70, file=None):
    if file is None:  file = sys.stdout
    for name, seq in iterable_of_name_seq:
        print(">{}".format(name), file=file)
        for i in count():
            piece = seq[i*seqwidth:(i+1)*seqwidth]
            if not piece:  break
            print(piece, file=file)


_rc = str.maketrans("acgtACGT", "tgcaTGCA")
def revcomp(seq, rctable=_rc):
    return seq[::-1].translate(rctable)


_common_startcodons = frozenset(("ATG", "GTG"))
def all_cds(fastaname, coordinatesname, common_startcodons=_common_startcodons):
    nseq = 0
    startcodons = Counter()
    with open(fastaname) as f:
        for seqname, seq in read_fasta(f):
            nseq += 1
    if nseq > 1:
        raise FormatError("fasta file contains more than one sequence")
    with open(coordinatesname) as f:
        omit_spaces = str.maketrans("", "", " ")
        header = [s.translate(omit_spaces) for s in next(f).strip().split("\t")]
        Elements = namedtuple("Elements", header)
        #print(Elements.__dict__)
        for line in f:
            elements = line.strip().split("\t")
            elements = Elements(*elements)
            if elements.FeatureType != "CDS":  continue
            strand = 1 if elements.Strand == "forward" else -1
            left, right = int(elements.LeftEnd), int(elements.RightEnd)
            gene = seq[left-1:right].upper()
            length = right - left + 1
            if strand < 0:
                gene = revcomp(gene)
            gene = gene[:-3]  # omit stop codon
            length -= 3
            #print(strand, left, right, length, length % 3)
            assert length > 0
            assert length % 3 == 0
            startcodon = gene[:3]
            startcodons[startcodon] += 1
            if startcodon not in common_startcodons:
                continue
            yield(elements.FeatureName, gene)


def extract_cds(args):
    fastaname, coordinatesname = args
    coding_seqs = all_cds(fastaname, coordinatesname)
    write_fasta(coding_seqs, file=sys.stdout)


def codons(seq):
    it = iter(seq)
    while it:
        yield "".join((next(it), next(it), next(it)))

def count_codons(args):
    fastaname = args[0]
    counter = Counter()
    with open(fastaname) as f:
        for seqname, seq in read_fasta(f):
            for codon in codons(seq[3:]):  # skip start codon
                counter[codon] += 1
    return counter

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2:  # extract cds from fasta and annotation
        extract_cds(args)
    elif len(args) == 1:  # count codons in sequences
        counter = count_codons(args)
        print(len(counter))
        print(counter)
    else:
        raise RuntimeError("usage:  analyze_cds.py  <fastafile> [<featurefile>]")
