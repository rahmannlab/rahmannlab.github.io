---
title: Pangenome Local Alignment Search Tool for detecting high scoring local alignments
date: 2021-02-03
image: /news/pangenome-graphs.jpeg
imagewidth: 60
layout: basic
---
Our paper [Detecting high-scoring local alignments in pangenome graphs](https://doi.org/10.1093/bioinformatics/btab077) is about a new heuristic method to find maximum scoring local alignments of a DNA query sequence to a pangenome represented as a compacted colored de Bruijn graph. 

Our approach additionally allows a comparison of similarity among sequences within the pangenome. We show that local alignment scores follow an exponential-tail distribution similar to BLAST scores, and we discuss how to estimate its parameters to separate local alignments representing sequence homology from spurious findings. An implementation of our method is presented, and its performance and usability are shown. Our approach scales sublinearly in running time and memory usage with respect to the number of genomes under consideration. This is an advantage over classical methods that do not make use of sequence similarity within the pangenome.

PLAST builds a compacted, colored de Bruijn graph from given input genomes using the API of Bifrost. Apart from the requirements of Bifrost (c++ and cmake), there are no further strict dependencies.
The source code and test data is available here: [PLAST]( https://gitlab.ub.uni-bielefeld.de/gi/plast)
