---
title: Best Paper Award at WABI 2017
date: 2017-09-01
image: news/wabi17.jpg
imagewidth: 35
layout: basic

---
The article "*Analysis of min-hashing for variant tolerant DNA read mapping*" by Jens Quedenfeld (now at TU Munich) and Sven Rahmann has received the Best Paper Award at the Workshop of Algorithms in Bioinformatics (WABI) 2017, held in Cambridge, MA, USA, August 20-23, 2017.

The authors consider an important question, as DNA read mapping has become a ubiquitous task in bioinformatics. New technologies provide ever longer DNA reads (several thousand basepairs), although at comparatively high error rates (up to 15%), and the reference genome is increasingly not considered as a simple string over ACGT anymore, but as a complex object containing known genetic variants in the population. Conventional indexes based on exact seed matches, in particular the suffix array based FM index, struggle with these changing conditions, so other methods are being considered, and one such alternative is locality sensitive hashing. Here we examine the question whether including single nucleotide polymorphisms (SNPs) in a min-hashing index is beneficial. The answer depends on the population frequency of the SNP, and we analyze several models (from simple to complex) that provide precise answers to this question under various assumptions. Our results also provide sensitivity and specificity values for min-hashing based read mappers and may be used to understand dependencies between the parameters of such methods. This article may provide a theoretical foundation for a new generation of read mappers.

The article can be freely accessed in the [WABI conference proceedings](http://drops.dagstuhl.de/opus/portals/lipics/index.php?semnr=16042) (Proceedings of the 17th International Workshop on Algorithms in Bioinformatics (WABI 2017), Russell Schwartz and Knut Reinert (Eds.), LIPICS Vol. 88).

This work is part of subproject [C1](/research/sfb876c1/) of the collaborative research center [SFB 876](http://www.sfb876.de/).
