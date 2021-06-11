---
layout: basic
date: 2021-04-01
linktext: Algorithms for Sequence Analysis
instructor: Prof. Dr. Sven Rahmann
---

# Lecture “Algorithms for Sequence Analysis”

Specialized course, M.Sc. Bioinformatics, Saarland University.\\
Elective course, M.Sc. Computer Science and related, Saarland University.

| **Prerequisites** | B.Sc. in Bioinformatics or CS, no special requirements. |
| **Credits** | 9 ECTS credits |
| **Required time** | 4V+2Ü (4 hours of lectures, 2 hours of tutorials per week) |
| **Language** | English |
| **Registration** | specific to each semester, see below |


## Topics

The following topics will be covered in the course; additional topics may be included, depending on time and current events.

* exact pattern matching algorithms (simple patterns, no index) and their analysis
* algorithms based on automata and bit-parallel algorithms
* full-text index data structures (suffix tree, suffix arrays)
* several applications of full-text index data structures to bioinformatics, e.g. repeat discovery
* succinct index data structues (FM index) and algorithms (backward search)
* approximate pattern matching (simple patterns, with and without index)
* application: read mapping
* pairwise sequence alignment: algorithms, variations, speed-ups
* score matrices and evolutionary Markov processes
* alignment statistics
* multiple sequence alignment: models, hardness, heuristics
* alignment-free methods, *k*-mers, hashing
* locality sensitive hashing; min hashing; analysis
* several applications of alignment-free methods
* genome assembly
* motif search and discovery; statistical evaluation of motifs

Scroll down for course schedule and assignments.

---


## Summer 2021

Because of the ongoing CoViD-19 pandemic, this lecture and its associated tutorials will be online only and delivered via Zoom.
Lecture recordings and exercise sheets will be linked on this page.

We will discuss the exercises together as a group.
For this to work effectively, it is expected that you have watched the lectures or recordings and thought about the problems each week!

| **Instructor** | Prof. Dr. Sven Rahmann |
| **Lectures** | Tue 12:30-14:00 and Thu 08:30-10:00 each week via Zoom.  These lectures will be recorded. |
| **Exercises** | either (A) Tue 14:15-15:45 or (B) Wed 08:30-10:00 |
| **Lecture notes** | [TODO](TODO) |
| **Exams** | 9 ECTS credits. Dates and details TBD. [General information](/infos/pruefungen) on exams (in German) |
| **Registration** | Register at the [CMS](https://cms.sic.saarland/alsa/) until Friday April 16. |
| **Note** | Summer 2021 is a virtual online semester. Lectures will be delivered via Zoom. To obtain the Zoom link, please register for the course and then look at the provided link in the CMS. |


#### Schedule

**Note 1:** [Video recordings of the lectures](https://cms.sic.saarland/alsa/materials) are only available in the CMS for registered students.

**Note 2:** Links for assignment submission are sent out by email to registered students.
They are also [available in the CMS](https://cms.sic.saarland/alsa/materials).


| **Date** | **Topics** | **Slides** |
| Tue 13.04. | **Exact pattern search:** Naive, Horspool. Adminstrative issues. | [Slides](alsa21/01-1-naive-horspool.pdf); [Admin](alsa21/00-0-overview.pdf) |
| Thu 15.04. |  Automata-based algorithms (NFA: Shift-And; DFA: Knuth-Morris-Pratt) | [Slides](alsa21/01-2-automata.pdf)
|            | [Assignment 1](alsa21/sheet1.pdf), submit via github classroom |
| Tue 20.04. | Bit-parallel algorithms: BNDM; more general patterns | [Slides](alsa21/01-3-bitparallel.pdf)
| Thu 22.04. | A primer on efficient Python programming: Counting motif occurrences in genomes | [Slides](alsa21/01-4-python.pdf) |
|            | [Assignment 2](alsa21/sheet2.pdf), submit via github classroom |
| Tue 27.04. | **Full-text index data structures:** Suffix trees, Ukkonen's algorithm. | [Slides](alsa21/02-1-suffixtrees.pdf)|
| Thu 29.04. | Ukkonen's algorithm: Skip/count trick analysis. Suffix arrays and enhancements (lcp). | [Slides](alsa21/02-2-suffixarrays.pdf) |
|            | [Assignment 3](alsa21/sheet3.pdf), submit via github classroom |
| Tue 04.05. | Applications of suffix arrays and linear-time lcp construction (Kasai's algorithm) | Slides above |
| Thu 06.05. | Linear-time suffix array construction: SAIS algorithm | [Slides](alsa21/02-3-sais.pdf) |
|            | [Assignment 4](alsa21/sheet4.pdf), submit via github classroom |
| Tue 11.05. | SAIS algorithm, implementation details | [Code](alsa21/sais.py) |
|            | [Assignment 5](alsa21/sheet5.pdf), submit via github classroom |
| Thu 13.05. | (Holiday) |
| Tue 18.05. | Connections between suffix trees and suffix arrays; range minimum queries (RMQs) | [Slides](alsa21/02-4-connections.pdf)|
| Thu 20.05. | The Burrows-Wheeler transform (BWT) and backward search | [Slides](alsa21/02-5-bwt.pdf) |
|            | [Assignment 6](alsa21/sheet6.pdf), submit via github classroom |
| Tue 25.05. | FM index, rank in sublinear space, wavelet trees | [Slides](alsa21/02-6-fmindex.pdf) |
| Thu 27.05. | Text compression | [Slides](alsa21/02-7-compression.pdf) |
|            | [Assignment 7](alsa21/sheet7.pdf), submit via github classroom |
| Tue 01.06. | **Error tolerant pattern search:** Distance and similarity measures; edit distance | [Slides](alsa21/03-1-dist-sim.pdf) |
| Thu 03.06. | (Holiday) |
|            | [Assignment 8](alsa21/sheet8.pdf), submit via github classroom |
| Tue 08.06. | Error tolerant pattern matching algorithms I | [Slides](alsa21/03-2-patternsearch-1.pdf) |
| Thu 10.06. | Error tolerant pattern matching algorithms II | [Slides](alsa21/03-3-patternsearch-2.pdf) |
|            | [Assignment 9](alsa21/sheet9.pdf), submit via github classroom |
| Tue 15.06. | Pairwise sequence alignment (and variations) | [Slides](alsa21/03-4-pairwise-alignment.pdf) [Code](alsa21/alignments.py) |
| Thu 17.06. | DNA read mapping | |
| Tue 22.06. | Extensions and improvements of pairwise alignment algorithms | |
| Thu 24.06. | On the theory of scoring schemes | |
| Tue 29.06. | Local alignment statistics (E-values, p-values) | |
| Thu 01.07. | | |
| Tue 06.07. | | |
| Thu 08.07. | | |
| Tue 13.07. | | |
| Thu 15.07. | | |
| Tue 20.07. | | |
| Thu 22.07. | **Summary:** Recurring topics, Comments about exam | |

---


### Literature

Gonzalo Navarro, Mathieu Raffinot\\
**Flexible Pattern Matching in Strings**\\
Cambridge University Press\\
ISBN: 0-521-03993-2

Dan Gusfield\\
**Algorithms on Strings, Trees and Sequences**\\
Cambridge University Press\\
ISBN: 0-521-58519-8

David Sankoff und Joseph P. Kruskal\\
**Time Warps, String Edits, and Macromolecules**\\
University of Chicago Press\\
ISBN: 1-575-86217-4\\

Additional research papers may be provided during the lectures.
