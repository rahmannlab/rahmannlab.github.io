---
title: New preprint and software "ting" for TCR repertoire clustering
date: 2020-05-29
image: /news/ting.png
imagewidth: 45
layout: basic
---

Our preprint ["Rapid T cell receptor interaction grouping with ting"](https://www.biorxiv.org/content/10.1101/2020.05.04.069914v1) is online.
Clustering of antigen-specific T cell receptor repertoire (TCRR) sequences remains challenging. While established tools like gliph aim to solve this problem they suffer from serveral shortcommings, including bad performance on huge repertoires, non-determinism, potential loss of significant antigen-specific or inclusion of too many unspecific sequences.
["ting"](https://github.com/FelixMoelder/ting) solves these issues by applying an efficient algorithm for identifying antigen-specific k-mers based on Fisher's Exact Test. This allows fast processing of large scale repertoires and an improved differentiation between naive and specific TCR3b sequences.

The full paper has been submitted for review.
