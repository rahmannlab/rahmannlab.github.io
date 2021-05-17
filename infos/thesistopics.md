---
layout: basic
linktext: Thesis Topics
description: Ideas for Projects and Thesis Topics
who: Bachelor and Master students in Bioinformatics
order: 9
---

# Ideas for Thesis Projects

The following is an **incomplete** list of ideas for thesis topics in (Algorithmic) Bioinformatics that may be supervised by members of the group.
You are encouraged to suggest your own ideas and follow your own interests as well.

----

## Polishing circular assemblies from long reads

Most long-read assemblers are optimized to assemble linear, not circular, contigs.
Some assemblers do support circular structures, but the resulting contigs may need polishing.
The goal of this project is to investigate different strategies for refining contigs produced by different assemblers (like CANU) when we expect circular contigs.

In the long run, this project may be extended to write an optimized assembler for circular structures.

**Contact:** Sven Rahmann

----

## Converting images of structural formulas of organic molecules to a formal representation (InChI)

In early 2021, kaggle presented a [challenge](https://www.kaggle.com/c/bms-molecular-translation) that asks participants to derive a formal molecule description (InChI strings) from a scanned image of the structural formula of any organic molecule.

This project will look at the successful approaches in this challenge and extend them.
This will involve AI methods like deep neural networks, but also methods for graph-to-string encoding.

**Contact:** Sven Rahmann, Christopher Schröder (Essen)

----

## Porting and improving scientific software to just-in-time compiled Python

A large fraction of scientific software in the biosciences is written in C/C++ (especially numerical code and simulation-heavy code) or in R (especially high-level statistical methods).

The [numba project](https://numba.pydata.org) provides just-in-time compilations capabilities for Python and is working towards a v1.0 release.
The advantage is jit compilation is that the compiler can exploit and optimize for what we might call "runtime constants", i.e., parameter values that are known only at runtime, but that do not change once they are initialized.
If we compile the time-critical code after the initialization work has been done, we may achieve speeds beyond what is possible with C++ or other statically compiled languages.

We offer seveal topics that aim to port existing scientific software (or part of its functionality) to the Python universe, extending the functionality, improving the user experience and optimizing the speed all at the same time.

Such a project makes most sense together with another group that relies on compute-intensive software that has proven to be a time-bottleneck in their research workflow.

You will need good Python programming skills, as well as a good unterstanding of low-level (C or assembly) code, e.g., bit manipulations. 
Essentially you will be writing part high-level Python code using existing scientific libraries (numpy, scipy, pandas, ML packages) and part low-level C code, but using Python syntax.

**Contact:** Sven Rahmann

----

## Alignment-free analysis of whole genome data

We run several projects that aim to analyze whole genome sequencing (WGS) data using alignment-free methods:
We look at short DNA fragments (so-called "*k*-mers") and their counts in each sample of a large dataset to answer questions about (for example) copy number aberrations, structural variants, disease-specific genome alterations, etc.

The basis for these methods is an extremely efficient hash table implementation that we have developed recently.
In each of the thesis projects offered here, we will explore a different genome-scale application of this technology and develop new algorithms to solve genome analysis questions.

This includes the analysis of real datasets, either publically available ones, or exclusive data provided by partners from the Faculty of Medicine or Biology.

**Contact:** Sven Rahmann
