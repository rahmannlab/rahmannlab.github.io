---
layout: impressum

autor: Daniela Beisser & Sven Rahmann
title: Metatranscriptome Analysis
collaboration: the Biodiversity group (Jens Boenigk), Essen
status: current
---
Next generation sequencing technologies are increasingly applied to analyse complex ecosystems by mRNA sequencing of whole communities. In principal, each sequenced mRNA allows an assignment of the underlying species as well as a functional annotation. While the functional information is sufficiently covered by databases such as Uniprot and NCBI the approach is currently limited by incomplete taxonomic references.

For an accurate assignment of taxonomic groups to environmental metatranscriptomic reads we build a custom database that comprises all major eukaryotic groups and a stand-alone tool to assign reads with a low false discovery rate.
The custom database includes peptide sequences translated from transcriptomes of all relevant eukaryotic taxonomic groups, in total 146 species. We do not attempt to assign sequence reads on species or genera level, but taxonomic groups. The biggest problem is the misassignment of sequences to incorrect species, we therefore perform rigorous filtering, in which we evaluate the distance between the best hit and next hit in another taxonomic group. The developed tool (TaxMapper, available at bitbucket and bioconda) is build in a modular way to be applicable stepwise with user-set parameters or as a complete easy-to-use analysis with standard parameters starting from a RAPsearch mapping file to a visualization of community composition.
Additionally, we develop a reliable workflow for microeukaryotic metatranscriptome analysis. Written as a rule-based Snakemake workflow, it unites all major bioinformatic steps: preprocessing of raw reads, functional and taxonomic assignment with TaxMapper and statistical analyses. The set-up is very generic and can be adjusted to any environmental sample.
