---
title: New paper and software "xengsort" for xenograft sorting
date: 2020-05-16
image: /news/xengsort.png
imagewidth: 60
layout: basic
---

Finally, our preprint ["Fast lightweight accurate xenograft sorting"](https://www.biorxiv.org/content/10.1101/2020.05.14.095604v2) is online.
Xenograft sorting classifies the (paired-end or single-end) reads of a xenograft sample according to species of origin. 
A typical application concnerns sequenced samples from patient-derived xenografts (PDX; tumors extracted from human patients and implanted into mice), where the reads have to be classified into human reads and mouse reads (and, possibly, reads that could originate from both species, reads from neither species, and ambiguous reads).
We have developed an alignment-free approach based on 3-way bucketed Cuckoo hashing. 
Our tool ["xengsort"](https://gitlab.com/genomeinformatics/xengsort/) is faster by a factor of 4 than existing alignment-free tools on typical PDX datasets.

A poster about this work will be presented at [ISMB HiTSeq](http://hitseq.org.s3-website-us-east-1.amazonaws.com/news.html).
The full paper has been submitted for review.
