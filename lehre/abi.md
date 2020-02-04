---
layout: basic
linktext: Algorithmische Bioinformatik
instructor: Prof. Dr. Sven Rahmann
---

# Vorlesung “Algorithmische Bioinformatik”

## Wintersemester 2019/20

Wegen ausgefallener Veranstaltungen wird es einen Nachholtermin geben: Mittwoch 12.02.2020 um 10:15-11:45 in OH14/202.

**Vorlesung**: Di 08:30-10:00 in OH12 / 1.056\\
**Übungen**:   Di 12:15-13:45 in OH12 / 1.055\\
**Modul**:     INF-MSc-606, Forschungsbereich Algorithmen und Komplexität\\
**Material**:  [Skript-Entwurf](abi19/skript.pdf)\\
**Prüfungen**: 6 CP; mündlich nach Vereinbarung. Zur Anmeldung ist kein Leistungsnachweis erforderlich. [Informationen](/infos/pruefungen).

|Di 08.10. | Einführung, Simulation von Zufallssequenzen |
|          | Übung: [Blatt 1](abi19/blatt01.pdf). Material: [Gene von *E. coli*](abi19/ecoli_K12_MG1655_genes.fa).  Lösung: [Python](abi19/uebung1.py)
|Di 15.10. | Textmodelle: M0, M1, M*k*, Markovmodelle variabler Ordnung. |
|          | Übung: [Blatt 2](abi19/blatt02.pdf) | 
|Di 22.10. | <font color="crimson">Achtung! Um 08:30 keine Vorlesung. Die Vorlesung wird 12:15-13:45 in OH12/1.055 von Jens Zentgraf vertreten.</font><br/>Allgemeine Textmodelle; Rechnen mit kleinen Wahrscheinlichkeiten. |
|          | <font color="crimson">Keine Übung!</font> |
|Di 29.10. |  Textmodelle: Parameterschätzung. Einführung in Hidden-Markov-Modelle. Material: [ML- und MAP-Schätzung der Erfolgswahrscheinlichkeit beim Münzwurf](http://www.mi.fu-berlin.de/wiki/pub/ABI/Genomics12/MLvsMAP.pdf) |
|          |  Übung: [Blatt 3](abi19/blatt03.pdf) |
|Di 05.11. |  Hidden Markov Modelle: Algorithmen (Forward, Viterbi) |
|          |  Übung: [Blatt 4](abi19/blatt04.pdf) |
|Di 12.11. |  Hidden Markov Modelle: Algorithmen (Forward-Backward), Training |
|          |  Übung: [Blatt 5](abi19/blatt05.pdf) |
|Di 19.11. |  <font color="crimson">fällt aus; keine Vorlesung; keine Übung</font> |
|Di 26.11. |  HMMs: Erweiterungen. [Artikel zur Verweildauermodellierung](https://link.springer.com/content/pdf/10.1007%2F11851561_3.pdf). Kein neues Übungsblatt. |
|Di 03.12. |  <font color="crimson">fällt wegen Krankheit aus!</font>|
|Di 10.12. |  Motivmodelle, insbesondere PWMs. |
|          |  Übung: [Blatt 6](abi19/blatt06.pdf)
|Di 17.12. |  Probabilistische arithmetische Automaten; Anwendungen von PAAs. |
|          |  Übung: [Blatt 7](abi19/blatt07.pdf), Material: [Corynebacterium diphtheriae gzipped FASTA](abi19/material07/c_diphtheriae.fa.gz) |
|(Weihnachts-)  |  |
|(ferien)       |  |
|Di 07.01. |  Probabilistische arithmetische Automaten: Konstruktion über DAAs |
|          |  Übung: [Blatt 8](abi19/blatt08.pdf) |
|Di 14.01. |  Phylogenetik: Bäume, Anzahlen, Perfekte Phylogenien |
|          |  Übung: [Blatt 9](abi19/blatt09.pdf) |
|Di 21.01. |  Phylogenetik: Merkmalsbasierte Methoden: Maximum Parsimony, Minimum Flip |
|          |  Übung: [Blatt 10](abi19/blatt10.pdf) |
|Di 28.01. |  Phylogenetik: Distanzbasierte Methoden |
|          |  Übung: [Blatt 11](abi19/blatt11.pdf) |
|Mi 12.02. |  Phylogenetik: Details zu Neighbor Joining (OH14/202!) |
|          |  Besprechung von Blatt 11; kein neues Blatt. |


---

## Inhalt (Vorlesungskommentar)

Wir behandeln verschiedene algorithmische Aspekte der Bioinformatik.
Ein vorausgegangener Abschluss der Bachelor-Vorlesung “Algorithmen auf Sequenzen“ ist hilfreich.

Themenbereiche sind:

*    statistische Modelle für biologische Sequenzen (und andere Texte)
*    Data Mining in Genomdaten (z.B. Motivsuche)
*    Rekonstruktion phylogenetischer Bäume
*    Genom-Dynamik (Umordnungsprobleme)

Die Vorlesung wird von praktischen und theoretischen Übungsaufgaben begleitet, deren Bearbeitung wichtig für ein genaues Verständnis des Stoffs ist.
Im Anschluss an diese Vorlesung besteht bei Interesse die Möglichkeit, in diesem Bereich eine Masterarbeit zu schreiben.

### Literatur

* Durbin, Eddy, Krogh & Mitchison:\\
  **Biological Sequence Analysis (Probabilistic Models of Proteins and Nucleic Acids)**\\
  Cambridge University Press
* Pavel Pevzner:\\
  **Computational Molecular Biology - An Algorithmic Approach**\\
  MIT Press
* Neil Jones and Pavel Pevzner:\\
  **An Introduction to Bioinformatics Algorithms**\\
   MIT Press
* Hans-Joachim Böckenhauer and Dirk Bongartz:\\
  **Algorithmische Grundlagen der Bioinformatik - Modelle, Methoden und Komplexität**\\
  Teubner
* David Mount:
  **Bioinformatics (Sequence and Genome Analysis)**\\
  Cold Spring Harbor Laboratory Press
* Weitere Originalliteratur (wissenschaftliche Aufsätze, “paper”), die im Lauf der Vorlesung bekannt gegeben wird.
