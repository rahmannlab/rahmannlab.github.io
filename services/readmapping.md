---
layout: basic

title: Standard Read Mapping
linktext: Read Mapping
summary: Mapping of next generation sequence reads against a reference genome using the Burrows-Wheeler Aligner (BWA)
---
## Standard Read Mapping

### Important notes to the user of this service

* Current reference genomes are human (GRCh37) and mouse (mmv37), further genomes will follow, feel free to ask for the genome you are interested in.
* To get best mapping results we need information about the used technology (GAII, HiSeq, 454, SOLiD, …) and preprocessing steps (e.g. use of illumina pipeline). Additionally, a summary of the library preparation steps is helpful.

### Required input data

* read files (single-end reads or paired-end reads) in Sanger FASTQ format or Illumina FASTQ format (or fastq.gz )

\<SEQ_ID>\\
\<SEQUENCE>\\
<+>\<DESCRIPTION>\\
\<QUALITY VALUES>

* information about technology and preprocessing steps

### Generated results

* .bam file: sorted mapped alignment file
* .bai file: bam index file, necessary for many downstream tools, e.g. IGV
* summary report: containing information about total number of reads, number of mapped reads and number of unmapped reads

### Additional options on request

* removal of duplicates
* removal of unmapped reads
* coverage plots: graphical overview of the read distribution over the genome
* bwa run with non-standard parameters (see standard parameters below)

### Methods & Implementation

Mapping of next generation sequence reads against a reference genome is done by Burrows-Wheeler Aligner (bwa) with standard parameters. The output is converted using samtools into .sam format and finally into .bam format.
### BWA standard parameters

(This information is subject to change and is taken from here)

###  ALN

OPTIONS:

**-n** NUM | Maximum edit distance if the value is INT, or the fraction of missing alignments given 2% uniform base error rate if FLOAT. In the latter case, the maximum edit distance is automatically chosen for different read lengths. **[0.04]**
**-o** INT | Maximum number of gap opens **[1]**
**-e** INT | Maximum number of gap extensions, -1 for k-difference mode (disallowing long gaps) **[-1]**
**-d** INT | Disallow a long deletion within INT bp towards the 3’-end **[16]**
**-i** INT | Disallow an indel within INT bp towards the ends **[5]**
**-l** INT | Take the first INT subsequence as seed. If INT is larger than the query sequence, seeding will be disabled. For long reads, this option is typically ranged from 25 to 35 for ‘-k 2’. **[inf]**
**-k** INT | Maximum edit distance in the seed **[2]**
**-t** INT | Number of threads (multi-threading mode) **[1]**
**-M** INT | Mismatch penalty. BWA will not search for suboptimal hits with a score lower than (bestScore-misMsc). **[3]**
**-O** INT | Gap open penalty **[11]**
**-E** INT | Gap extension penalty **[4]**
**-R** INT | Proceed with suboptimal alignments if there are no more than INT equally best hits. This option only affects paired-end mapping. Increasing this threshold helps to improve the pairing accuracy at the cost of speed, especially for short reads (~32bp).
**-c** | Reverse query but not complement it, which is required for alignment in the color space.
**-N** | Disable iterative search. All hits with no more than maxDiff differences will be found. This mode is much slower than the default.

### SAMSE

OPTIONS:

**-n** INT | Maximum number of alignments to output in the XA tag for reads paired properly. If a read has more than INT hits, the XA tag will not be written. **[3]**
**-r** STR | Specify the read group in a format like ‘@RG\tID:foo\tSM:bar’. **[null]**

### SAMPE

OPTIONS:

**-a** INT | Maximum insert size for a read pair to be considered being mapped properly. Since 0.4.5, this option is only used when there are not enough good alignment to infer the distribution of insert sizes. **[500]**
**-o** INT | Maximum occurrences of a read for pairing. A read with more occurrneces will be treated as a single-end read. Reducing this parameter helps faster pairing. **[100000]**
**-P** | Load the entire FM-index into memory to reduce disk operations (base-space reads only). With this option, at least 1.25N bytes of memory are required, where N is the length of the genome.
**-n** INT | Maximum number of alignments to output in the XA tag for reads paired properly. If a read has more than INT hits, the XA tag will not be written. **[3]**
**-N** INT | Maximum number of alignments to output in the XA tag for disconcordant read pairs (excluding singletons). If a read has more than INT hits, the XA tag will not be written. **[10]**
**-r** STR | Specify the read group in a format like ‘@RG\tID:foo\tSM:bar’. **[null]**
