# BIOGEEKS

BICP 201 project for Data Structures & Algorithm [KU]

---

# KMP DNA Motif Visualizer

A Python-based graphical tool designed to demonstrate the **Knuth–Morris–Pratt (KMP)** string-matching algorithm specifically for bioinformatics. This project visualizes character-by-character comparisons and the efficiency of the Longest Prefix Suffix (LPS) array in real-time using DNA sequences.

## 1. Project Overview

The KMP algorithm optimizes string searching by avoiding redundant comparisons. This visualizer provides an intuitive look at how the algorithm "skips" through the DNA sequence based on pre-processed pattern data.

### Key Features

* **Real-Time Animation:** Visualizes the sliding window approach and character matches using Matplotlib.
* **DNA Validation:** Includes a built-in logic check to ensure only valid genomic bases (A, T, G, C) are processed.
* **Frequency Analysis:** Generates a bar chart showing the distribution and index positions of found motifs.
* **Results Export:** Automatically saves biological records (match positions and metadata) to a `kmp_dna_results.txt` file.
* **Dynamic Input:** Support for user-defined DNA sequences and search motifs via a Tkinter GUI.

## 2. Algorithm & Complexity

The core of this tool is the Knuth–Morris–Pratt logic, which utilizes an auxiliary **LPS (Longest Prefix Suffix)** array to determine the next shift.

| Metric | Complexity |
| --- | --- |
| **Time Complexity** |  |
| **Space Complexity** |  |
| **Visualization Delay** | 500ms (Step-by-step) |

*Note:  represents the length of the DNA sequence and  represents the length of the pattern/motif.*

---

## 3. Technologies Used

* **Python:** Core Logic
* **Tkinter:** GUI for user input and error handling
* **Matplotlib:** Dynamic plotting and frequency visualization

---

## 4. How It Works

1. **Input:** Enter the main **DNA Sequence** and the **Target Motif** in the GUI.
2. **Preprocessing:** The program calculates the LPS array to handle pattern shifts efficiently.
3. **Visualization:** * **Text (Black):** The target DNA sequence.
* **Pattern (Blue):** The sliding motif being compared.
* **Status (Green):** Displays the exact position when a match is successfully identified.


4. **Analytics:** Once the search concludes, a bar graph displays the occurrence positions.

---

## 5. Educational Context

This project was developed for **Data Structures & Algorithms (DSA)** study, focusing on:

* Pattern matching optimization.
* Practical application of auxiliary arrays (LPS).
* Data visualization and GUI development for algorithm demonstration.

**Submitted by:** Prapti Poudel & Nayana Shakya

---

