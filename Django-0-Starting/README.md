# 🐍 Day 00: Python Starting

> **Focus:** Python Syntax, Data Structures, Algorithmic Logic, and File I/O.

## 📝 Overview

This module served as the "bootcamp within a bootcamp," designed to facilitate a rapid transition into Python. Unlike the web-focused modules, this segment focused purely on the language itself—mastering Python's syntax, dynamic typing, and powerful data structures (dictionaries, lists, sets) before applying them to web development.

The exercises progressed from basic variable declaration to complex data parsing and HTML generation scripts.

## 📂 Project Breakdown

### 🔢 Ex00: The Type System (`var.py`)
**Concepts:** Dynamic Typing, Built-in Types
A strict introduction to Python's variable system.
* **Task:** Created a script that initializes and detects variable types (integers, floats, strings, lists, dicts, tuples, sets) and prints their class types to `stdout`.
* **Takeaway:** Understanding how Python handles memory and types differently compared to statically typed languages like C.

### 📄 Ex01: File I/O (`numbers.py`)
**Concepts:** File Handling, String Manipulation
* **Task:** Wrote a program to open a text file (`numbers.txt`), read number-heavy content, and format it for display without using external libraries.
* **Skill:** Managing file pointers and cleaning raw string data.

### 📚 Ex02 - Ex05: The Dictionary Deep Dive
**Concepts:** Hash Maps, Key-Value Logic, Exception Handling
A series of progressive exercises focusing on Python's most important data structure: the **Dictionary**.
* **Ex02 (`var_to_dict.py`):** Converted a list of tuples (Musician, Birth Year) into a dictionary, handling data transformation.
* **Ex03 (`capital_city.py`):** Implemented a state-to-capital lookup system. Required robust error handling for unknown keys.
* **Ex04 (`state.py`):** Reverse lookup (Capital-to-State). This required iterating through values to find the associated key, demonstrating the efficiency difference between O(1) key lookups and O(n) value searches.
* **Ex05 (`all_in.py`):** A complex parser that accepts a comma-separated string of queries (mixed states and capitals) and resolves each one to its counterpart, handling case insensitivity and whitespace formatting.

### 📊 Ex06: Custom Sorting (`my_sort.py`)
**Concepts:** Sorting Algorithms, Lambdas
* **Task:** Sorted a dictionary of musicians first by birth year (chronological), and then alphabetically by name for those born in the same year.
* **Challenge:** Python dictionaries are inherently unordered (in older versions) or insertion-ordered. This required converting the data to a list structure to apply a multi-key sort stable algorithm.

### 🧪 Ex07: The Periodic Table (`periodic_table.py`)
**Concepts:** Data Parsing, HTML Generation, CSS
The capstone project for this module.
* **Input:** A raw text file describing chemical elements with unstructured attributes (name, position, weight, electron configuration).
* **Process:** My script parses this text file, extracts the relevant data attributes into objects/dictionaries, and programmatically generates a valid HTML file.
* **Output:** An HTML page that renders the Periodic Table of Elements, utilizing CSS for the grid layout. This bridged the gap between backend Python logic and frontend rendering.

## 🚀 How to Run

1.  **Basic Scripts (Ex00 - Ex06):**
    Run these directly with the Python interpreter.
    ```bash
    python3 ex00/var.py
    python3 ex03/capital_city.py "Oregon"
    python3 ex05/all_in.py "New York, Paris, Berlin"
    ```

2.  **Periodic Table (Ex07):**
    This script generates a file.
    ```bash
    cd ex07
    python3 periodic_table.py
    # This creates 'periodic_table.html'
    # Open the resulting file in your browser to see the table.
    ```

## 🛠️ Tools Used
* **Python 3:** The core language for all logic.
* **Sys Module:** For command-line argument parsing (`sys.argv`).
* **File Operations:** `open()`, `read()`, `write()`.
* **Data Structures:** Heavy usage of `dict`, `list`, `tuple`, and `set`.
