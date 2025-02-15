---
layout: basic
date: 2022-01-11
linktext: Thesis Topics
instructor: Members of the Algorithmic Bioinformatics group
#description: Ideas for Projects and Thesis Topics
#who: Bachelor and Master students in Bioinformatics
#order: 9
---

# Ideas for Thesis Projects

The following is an **incomplete** list of ideas for thesis topics in (Algorithmic) Bioinformatics that may be supervised by members of the group.
You are encouraged to suggest your own ideas and follow your own interests as well.

----

## Alignment-free analysis of whole genome data

We run several projects that aim to analyze whole genome sequencing (WGS) data using alignment-free methods:
We look at short DNA fragments (so-called "*k*-mers") and their counts in each sample of a large dataset to answer questions about (for example) copy number aberrations, structural variants, disease-specific genome alterations, etc.

The basis for these methods is an extremely efficient hash table implementation that we have developed recently.
In each of the thesis projects offered here, we will explore a different genome-scale application of this technology and develop new algorithms to solve genome analysis questions.

This includes the analysis of real datasets, either publically available ones, or exclusive data provided by partners from the Faculty of Medicine or Biology.

**Contact:** Sven Rahmann

----

## A fast modern genome viewer

Existing genome viewers focus on alignments (from BAM files) or quantitative information from BED files.
In the era of alignment-free sequence analysis, it would be very helpful to view k-mer related information in selected genome areas (e.g., for a given set of genes).
With modern web and indexing technology, it should be possible to create a lightweight genome viewer that can display such information responsively.
We can offer theses at both Bachelor and Master level about this topic.

**Contact:** Sven Rahmann

----

## An automated guide to the human genome

When the human genome was first published, books about statistics of the human genome (e.g. how many genes on each chromosome, how many CpG islands) were written and printed.
Most of such information can be generated by automated workflows by examining the most recent genome sequence and annotation.
The goal of a thesis could be to write or extend an automated workflow (using Snakemake) to collect several bits of such information from an annotated genome and create an interactive HTML-based booklet, including tables, interactive graphs and texts.
The workflow language Snakemake is a syntactical extension of Python and allows us to define readable and reproducible workflows.

**Contact:** Sven Rahmann

----

## Rapid computational rRNA removal in metatranscriptomics datasets

As an extension of metagenomics, *metatranscriptomics* aims to both identify which species are present in a sample and which genes (or pathways) are active in them (Who is there? And what are they doing?).
After RNA sequencing, a considerable amount of the obtained reads may in fact contain ribosomal RNA (rRNA) and not messenger RNA (mRNA).
Several methods already exist to identify and remove rRNA reads.
This project aims to develop an even more efficient alignment-free method for this task.

**Contact:** Sven Rahmann

----

## Detection of novel viral sequences in metagenomic datasets

Large metagenomic datasets may contain many known and unknown bacteria and viruses.
While known species can be identified by database similarity searches, finding novel viral species (without a known reference sequence) is a more challenging task.
In the past, sequence-derived features have been used for this task, such as codon usage bias in coding sequences, together with machine learning methods, such as random forests or neural networks.
The goal of this project is to propose alternative methods and improve upon the state of the art.

**Contact:** Sven Rahmann

----

## Exploration of the Sichel Probability Distribution

The Sichel distribution arises when we let the unique parameter of a Poisson distribution (which is both its expectation and variance) be *randomly drawn* from a generalized Inverse Gaussian distribution, i.e., we obtain a particular mixture of Poissons.
The Sichel distribution can take a variety of shapes and properties, and in this (Bachelor or Master) thesis project, we want to examine how well it can fit different biological datasets.
One goal is to develop an interactive visual application that will allow to modify the parameters to obtain a certain shape.
Another goal is to implement efficient parameter estimation methods based on (robust) maximum likelihood or moments that work rapidly even on very large datasets.

**Contact:** Sven Rahmann

---

## Identification and quantification of SARS-CoV2 variants

Complementary to existing approaches, we want to develop an alignment-free method that can detect and quantify different variants of the coronavirus in wastewater samples based on variant-specific subsequences.

**Contact:** Sven Rahmann

----

## Polishing circular assemblies from long reads

Most long-read assemblers are optimized to assemble linear, not circular, contigs.
Some assemblers do support circular structures, but the resulting contigs may need polishing.
The goal of this project is to investigate different strategies for refining contigs produced by different assemblers (like CANU) when we expect circular contigs.

In the long run, this project may be extended to write an optimized assembler for circular structures.

**Contact:** Sven Rahmann


----

## Improving and porting and scientific software to just-in-time compiled Python

A large fraction of scientific software in the biosciences is written in C/C++ (especially numerical code and simulation-heavy code) or in R (especially high-level statistical methods).

The [numba project](https://numba.pydata.org) provides just-in-time compilations capabilities for Python and is working towards a v1.0 release.
The advantage is jit compilation is that the compiler can exploit and optimize for what we might call "runtime constants", i.e., parameter values that are known only at runtime, but that do not change once they are initialized.
If we compile the time-critical code after the initialization work has been done, we may achieve speeds beyond what is possible with C++ or other statically compiled languages.

We offer seveal topics that aim to port existing scientific software (or part of its functionality) to the Python universe, extending the functionality, improving the user experience and optimizing the speed all at the same time.

Such a project makes most sense together with another group that relies on compute-intensive software that has proven to be a time-bottleneck in their research workflow.

You will need good Python programming skills, as well as a good unterstanding of low-level (C or assembly) code, e.g., bit manipulations. 
Essentially you will be writing part high-level Python code using existing scientific libraries (numpy, scipy, pandas, ML packages) and part low-level C code, but using Python syntax.

**Contact:** Sven Rahmann, Vu Lam Dang, Jens Zentgraf

----

## A modern sequence and alignment editor

Sequence management, alignment editing and figure generation is an important task performed daily by biologists.
Older existing tools are still widely used but no longer maintained.
We propose the creation of a new open-source software package that aims to replace and extend them.

View [Details](topics/alignmenteditor.md).

**Contact:** Vu Lam Dang

----

## Fast PWM matching using just-in-time compilation

Fifteen to twenty years ago, the first algorithm appeared that allowed fast matching of position weight matrices (PWMs) against genomes.
These algorithms have since been further engineered and the resulting tools have become quite sophisticated, e.g. [MOODS](https://www.cs.helsinki.fi/group/pssmfind/).
We would like to find out whether the speed of PWM matching can be further improved using just-in-time compilation techniques when the matcher is compiled after the motif is known.

**Contact:** Sven Rahmann

