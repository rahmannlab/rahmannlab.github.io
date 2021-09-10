---
title: Analysis of ddRAD-seq data
members: Henning Timm, Johannes Köster & Sven Rahmann
collaborators: <a href="https://www.uni-due.de/leeselab/martina-weiss.php">Martina Weiss</a>, <a href="https://www.uni-due.de/aquatische_oekosystemforschung/fleese">Florian Leese</a>
summary: We develop pipelines and software for the analysis of (dd)RAD-seq data and evaluate them using both real and simulated data.
image: /research/ddrad.svg
software: ddRAGE
funding: internal
status: past
date: 2019-10-10
layout: project
---


Double digest sequencing of restriction site associated DNA (ddRAD-seq) is used in population genomics in order to reduce the complexity of genomic data for inter- and intra-population analysis. The genetic diversity, meaning the abundance of different mutations in a population, can give insight into the quality of the habitat.
For example, if the diversity of two populations differs, this might be a sign for a stressor affecting one of the populations. A population under stress is expected to show less diversity, as only the best fitted individuals can survive under bad conditions.

### How is ddRAD-seq data generated?

The ddRAD-seq protocol uses restriction enzymes to digest the DNA sequences of the target genome.
From the resulting fragments those with right size and structure are sequenced.
Due to this, all reads in a ddRAD-seq data set originate from distinct loci in the genome, namely the restriction sites at which the enzymes cut the DNA strand.

### Simulated ddRAD-seq data
With our simulation software ddRAGE, we are able to create high quality ground truth data for the evaluation of ddRAD analysis software.


### Challenges

As for most species no high quality reference genome, if any at all, is available.
Because of that, the analysis of ddRAD-seq data (RAD data for short) has to work without a reference.
The main problem to be solved is the re-association of reads with their originating loci, where both mutations and sequencing errors have to be taken into account.
As the data sets can be huge, the efficient clustering of similar sequences, preferably with linear run time, is needed, before any other analysis can begin.
This problem can be solved with the help of error tolerant hashing, both precisely and efficiently.

As the analysis of RAD data is highly dependent on the structure enforced by the ddRAD-seq protocol, verifying the results of an analysis can be difficult.
Due to this a well documented ground truth is needed, which has to model the structure as well as biological and technical patterns expected in RAD data.

### Publications

  * Poster: “Clustering of ddRAD-seq reads with randomized hash functions for biodiversity analysis&#8221 at [iSEQ Symposium on Methods and Applications of Next Generation Sequencing in Evolutionary Research][1], 2014, hosted at the [Max Planck Institute for Evolutionary Anthropology][2] in Leipzig.
  * Poster: “Estimation of genetic diversity with RAD sequencing and mutation-tolerant hashing” at 14. Tag der Forschung der Medizinischen Fakultät der Universität Duisburg-Essen, 2015.
  * Henning Timm, Hannah Weigand, Martina Weiss, Florian Leese, and Sven Rahmann. “ddRAGE: A Data Set Generator to Evaluate ddRADseq Analysis Software”. In: Molecular Ecology Resources 18.3 (2018). doi: [10.1111/1755-0998.12743][3].
  

 [1]: https://www.idiv.de/
 [2]: http://www.eva.mpg.de/german/index.html
 [3]: https://doi.org/10.1111/1755-0998.12743
