---
title: GAMIBHEAR-a tool for accurate haplotype reconstruction from GAM data
date: 2021-04-08
layout: basic
---

Genome Architecture Mapping (GAM) was recently introduced as a digestion- and ligation-free method to detect chromatin conformation.GAM’s ability to capture both inter- and intra-chromosomal contacts from low amounts of input data makes it particularly well suited for allele-specific analyses in a clinical setting. Allele-specific analyses are powerful tools to investigate the effects of genetic variants on many cellular phenotypes including chromatin conformation, but require the haplotypes of the individuals under study to be known a priori. So far, however, no algorithm exists for haplotype reconstruction and phasing of genetic variants from GAM data, hindering the allele-specific analysis of chromatin contact points in non-model organisms or individuals with unknown haplotypes.
We present GAMIBHEAR, a tool for accurate haplotype reconstruction from GAM data. GAMIBHEAR aggregates allelic co-observation frequencies from GAM data and employs a GAM-specific probabilistic model of haplotype capture to optimize phasing accuracy. 
["GAMIBHEAR"](https://bitbucket.org/schwarzlab/gamibhear) is available as an R package under the open-source GPL-2 license. The paper has been published in the Bioinformatics journal. ["GAMIBHEAR: whole-genome haplotype reconstruction from Genome Architecture Mapping data"](https://doi.org/10.1093/bioinformatics/btab238) 
