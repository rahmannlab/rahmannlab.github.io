---
layout: basic
linktext: Algorithmen auf Sequenzen
instructor: Prof. Dr. Sven Rahmann
---

## Vorlesung “Algorithmen auf Sequenzen”

### Wintersemester 2018/19

Die Vorlesung hat jetzt eine eigene Seite:\\
[https://rahmannlab.gitlab.io/algorithmen-auf-sequenzen](https://rahmannlab.gitlab.io/algorithmen-auf-sequenzen).

Informationen zur Vorlesung ab WS2018/19 finden Sie nur dort!

---

### Wintersemester 2016/17

**Vorlesung**: Do 08:30-10:00 in OH14/304.\\
**Übungen**:   Do 12:15-13:00 in OH14/304.\\
**Material**:    Skript-Entwurf (Oktober 2014)\\
**Prüfungen**: Für das Bachelor-Modul INF-BSc-315 werden in diesem Semester nur mündliche Prüfungen angeboten.  Die erweiterte Prüfung zur Diplom-Spezialvorlesung (3V+1Ü, SpG 4,6,7) wird nur mündlich angeboten.  Es ist kein Leistungsnachweis notwendig zur Prüfungsanmeldung. Prüfungstermine stehen noch nicht fest.

| Do 20.10. | **Vorlesung**: Einführung, Vokabeln (Folien); Bitsequenzen, population count (Folien) <br /> **Übung**: Blatt 1 |
| Do 27.10. | **Vorlesung**: Rank-Datenstruktur (Folien), Problem der Mustersuche: naiv (Folien) <br /> **Übung**: Blatt 2 |
| Do 03.11. | **Vorlesung**: Mustersuche: NFA und Shift-And (Folien), DFA und Knuth-Morris-Pratt (Folien) <br /> **Übung**: Blatt 3 mit Zusatzaufgaben |
| Do 10.11. | **Vorlesung**: Sublineare Algorithmen zur Mustersuche (Horspool, BNDM; Folien). <br /> **Übung**: Blatt 4 |
| Do 17.11. | **Vorlesung**: Mengen von Mustern (Folien), erweiterte Musterklassen (Folien). <br /> **Übung**: Blatt 5 |
| Do 24.11. | **Vorlesung** und **Übung** fallen heute wegen Krankheit aus!
| Do 01.12. | **Vorlesung**: Volltext-Indexdatenstrukturen: Suffixtries und Suffixbäume (Folien) <br /> **Übung**: Blatt 6 |
| Do 08.12. | **Vorlesung**: Suffixarrays und Anwendungen (Folien) <br /> **Übung**: Blatt 7 |
| Do 15.12. | **Vorlesung**: SA-IS-Algorithmus zur Konstruktion von Suffixarrays (Folien s.o.) <br /> **Übung**: Blatt 8 |
| Do 22.12. | **Vorlesung**: BWT, FM-Index (Folien) <br /> **Übung**: Blatt 9 |
| Do 12.01. | **Vorlesung**: Hamming-Distanz, q-Gramm-Distanz, Edit-Distanz, longest common subsequence, Berechnung der Edit-Distanz, Alignments, Anzahl verschiedener Alignments (Folien) <br /> **Übung**: Blatt 10 |
| Do 19.01. | **Vorlesung**: Algorithmen zur fehlertoleranten Musterusche (Folien) <br /> **Übung**: Blatt 11 |
| Do 26.01. | **Vorlesung**: Four-Russians-Methode (Folien), Alignment-Varianten (Folien) <br /> **Übung**: Blatt 12 |
| Do 02.02. | **Vorlesung**: Sequenzalignment: Erweiterungen (Folien) <br /> **Übung**: Blatt 13 |
| Do 09.02. | **Vorlesung**: Zusammenfassung, Fragen, Prüfungen <br /> keine **Übung**! |

---

## Inhalt (Vorlesungskommentar)

Das folgende Problem ist aus den Einführungsvorlesungen bekannt: Gegeben ist ein Text T und ein Muster P. Liste alle Positionen in T auf, an denen P vorkommt.

Von diesem Problem gibt es viele Varianten: Statt aus einem einzelnen String kann P aus einer Menge von Strings bestehen, oder in impliziter Form gegeben sein, etwa durch einen regulären Ausdruck, oder eine sogenannte position weight matrix, oder auch durch eine kontextfreie Grammatik. Zudem suchen wir unter Umständen auch nach approximativen Vorkommen im Text (z.B. Meier vs. Mayer). Vielleicht wollen wir auch nur wissen, ob P überhaupt vorkommt, oder auch nur, wie oft (ohne alle Positionen aufzulisten).

Auch die Frage nach der Statistik der Anzahl der Vorkommen ist von Interesse: Angenommen, wir beobachten ein bestimmtes Muster siebzehn mal in einem bestimmten Text: Ist das überraschend oft, oder lässt sich das durch puren Zufall erklären?

Die biologische Sequenzanalyse hat sich aus den Gebiet des pattern matching entwickelt, das in den 70er Jahren vor allem von theoretischen Informatikern bearbeitet wurde. Hier ist in den letzten 20 Jahren eine Fülle von (sowohl sehr einfachen als auch sehr komplizierten) Algorithmen entstanden, und es stellt sich heraus, dass die Algorithmen, “die man so kennt”, in der Praxis häufig langsam sind.

In der Vorlesung werden wir Varianten des Pattern Matching Problems ausführlich behandeln und sowohl klassische als auch die zur Zeit in der Praxis schnellsten Algorithmen kennen lernen. Es geht sowohl um on-line Algorithmen (bei denen der Text vorher nicht bekannt sein muss) als auch um Index-basierte Verfahren (bei denen vorher ein Index des Textes erstellt wird). Index-basierte Verfahren sind heute sowohl bei der Analyse von Biosequenzen wichtig, als auch für web-basierte Suchmaschinen wie Google oder Bing ein essentieller Bestandteil des Kerngeschäfts.

In letzter Zeit nimmt die Bedeutung komprimierter Text-Inidizes stetig zu. Hierzu werden wir die wichtigsten Grundlagen kennen lernen und vor allem die zentrale Rolle der Burrows-Wheeler Transformation herausarbeiten.

Dem ersten Teil der Vorlesung liegt das Buch **Flexible Pattern Matching in Strings** von Gonzalo Navarro und Mathieu Raffinot zu Grunde. Es wird ergänzt durch Übersichtsartikel aus der Originalliteratur, die ich in der Vorlesung angeben werde. Zur Vorlesung wird ein Skript zur Verfügung gestellt.

Die Vorlesung wird von praktischen und theoretischen Übungsaufgaben begleitet, deren Bearbeitung wichtig für ein richtiges Verständnis des Stoffs ist. Im Anschluss an diese Vorlesung besteht bei Begabung und Interesse die Möglichkeit, in diesem Bereich eine Abschlussarbeit zu schreiben.

### Literatur

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
(Taschenbuchausgabe von 2000 des 1983 erschienenen Originals)

Weitere Originalliteratur (wissenschaftliche Aufsätze, “paper”), die im Lauf der Vorlesung bekannt gegeben wird.

---

## Prüfungsleistungen

* Bachelor-Wahlmodul (2V+1Ü; 4 LP); erweiterter Umfang für Studierende der RUB (5 CP)
* mündliche Prüfung von 20-30 Minuten Dauer oder Klausur von 90 Minuten Dauer
* Die genaue Prüfungsform wird abhängig von der Teilnehmerzahl kurz nach Vorlesungsbeginn festgelegt.
* Vordruck für die Prüfungsanmeldung ausfüllen, bei Frau Jankord (OH14 / R2.39) einen Termin/Uhrzeit geben lassen, von Prof. Rahmann oder Frau Jankord unterschreiben lassen; wird von Frau Jankord zur Prüfungsverwaltung geschickt.
