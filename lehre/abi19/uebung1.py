import random
from collections import Counter


# das Alphabet wird als globale Variable definiert.
alphabet = list(range(ord("0"), ord("9")+1)) \
           + list(range(ord("A"), ord("Z")+1)) \
           + list(range(ord("a"), ord("z")+1))
alphabet = "".join(map(chr, alphabet))


# Aufgabe 1.1.1
def simuliere_gleichverteilt(n=10000000):
    """
    Ziehe n-mal gleichverteilt aus dem Alphabet.
    Gib einen Zaehler mit den Symbolhaeufigkeiten zurueck.
    """
    rand = random.randrange
    m = len(alphabet)
    L = [alphabet[rand(m)] for i in range(n)]
    return Counter(L)

# Aufgabe 1.1.2
def erzeuge_p():
    """
    Berechne p laut Aufgabenbeschreibung.
    Gib p als Liste zurueck.
    """
    q = [1/(i*i) for i in range(1,63)]
    Z = sum(q)
    return [x/Z for x in p]

# Aufgabe 1.1.3
def simuliere_nach_p(p, n=1000000):
    """
    Ziehe n mal gemaess p aus dem Alphabet.
    Gib einen Zaheler mit den Symbolhaeufigkeiten zurueck.
    """
    rand = random.random  # Zahl in [0,1[
    L = []
    m = len(alphabet)
    for i in range(n):
        U = rand()
        for j in range(m):
            U -= p[j]
            if U < 0:  break
        L.append(alphabet[j])            
    return Counter(L)


# Aufruf der verschiedenen Teile zu Aufgabe 1
def aufgabe1():
    p = erzeuge_p()
    print(p[0], p[10], p[36], p[61]) # 1.1.2
    c = simuliere_nach_p(p)
    print(c)  # Symbolhaeufigkeiten


# Funktion zum Lesen von FASTA-Dateien fuer Aufgabe 1.2
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


# Illustration der Benutzung von read_fasta
def zaehle_sequenzen(fastaname):
    """
    Zaehele Sequenzen in der FASTA-Datei <fastaname>.
    Gib die Anzahl der Sequenzen zurueck.
    """
    nseq = 0
    with open(fastaname) as f:
        for seqname, seq in read_fasta(f):
            nseq += 1
            # hier kann man noch etwas mit seqname und seq machen
    return nseq


if __name__ == "__main__":
    aufgabe1()
    

