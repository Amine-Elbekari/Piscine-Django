# 📦 Day 01: Python Libraries & Environment

> **Focus:** Dependency Management, Virtual Environments, API Consumption, and Web Scraping.

## 📝 Overview

In modern software development, writing code is only half the battle; the other half is managing the ecosystem. **Module 01** shifted focus from pure syntax to the tools that make Python powerful.

This module covered the essential skills required to maintain a healthy development environment: managing packages with `pip`, isolating dependencies with `virtualenv`, and interacting with the outside world via HTTP requests and HTML parsing. It concluded with the initialization of my first Django project.

## 📂 Project Breakdown

### 📍 Ex00: Geohashing (`geohashing.py`)
**Tech:** Standard Library, `antigravity`
A cryptographic warm-up based on the famous XKCD comic.
* **Task:** Implemented a Geohashing algorithm that calculates a coordinate based on the date and the opening price of the Dow Jones.
* **Skill:** Working with precise data types and the Python standard library's easter eggs.

### 🐍 Ex01: Package Management (`my_script.sh`)
**Tech:** `pip`, Bash, Local Libraries
* **Task:** Created a script to install a specific development version of a library (`path.py`) from a GitHub repository into a **local** directory, rather than the global site-packages.
* **Challenge:** I had to configure a Python program to import this locally installed library, demonstrating an understanding of `PYTHONPATH` and how the interpreter resolves imports.

### 🧠 Ex02: API Consumer (`request_wikipedia.py`)
**Tech:** `requests`, `json`, `dewiki`
* **Task:** Built a CLI tool that queries the Wikipedia API.
* **Logic:** The script accepts a search term, fetches the page data, de-serializes the JSON response, and strips the Wikitext markup (using `dewiki`) to produce a clean, human-readable output file.
* **Error Handling:** Robustly handles 404s, ambiguous search terms, and network timeouts.

### 🕸️ Ex03: The Scraper (`roads_to_philosophy.py`)
**Tech:** `BeautifulSoup4`, `requests`, Recursion
* **The Theory:** Clicking the first non-parenthesized link in any Wikipedia article eventually leads to the article for "Philosophy."
* **Implementation:** I built a web scraper to test this hypothesis.
* **Logic:**
    * Parses the HTML of a Wikipedia page.
    * Intelligently skips links inside parentheses or italics (requiring complex DOM traversal).
    * Follows the "first valid link" recursively.
    * **Loop Detection:** Tracks visited pages to detect infinite loops and abort gracefully if the path gets stuck.

### ⚙️ Ex04: Environment Automation (`my_script.sh`)
**Tech:** `virtualenv`, `pip freeze`
* **Task:** Automated the setup of a Django-ready environment.
* **Outcome:** A script that creates a specific `virtualenv`, activates it, and installs a strict set of dependencies (`Django`, `psycopg2`) from a `requirements.txt` file. This ensures the development environment is reproducible on any machine.

### 🌍 Ex05: Hello Django (`django_project`)
**Tech:** Django Framework
* **Task:** The final step—bootstrapping the first Django project.
* **Outcome:** Configured the initial settings and routes to serve a simple "Hello World" page, validating that the environment setup from Ex04 was successful.

## 🚀 How to Run

1.  **Wikipedia API (Ex02):**
    ```bash
    pip install requests dewiki
    python3 ex02/request_wikipedia.py "Python (programming language)"
    # Output: Creates 'Python_(programming_language).wiki'
    ```

2.  **Roads to Philosophy (Ex03):**
    ```bash
    pip install requests beautifulsoup4
    python3 ex03/roads_to_philosophy.py "Elon Musk"
    # Output: Prints the path of articles taken to reach "Philosophy".
    ```

3.  **Environment Setup (Ex04):**
    ```bash
    cd ex04
    ./my_script.sh
    # Output: Creates and populates 'django_venv'
    ```

## 🛠️ Tools Used
* **Requests:** For synchronous HTTP requests.
* **BeautifulSoup:** For parsing and navigating HTML trees.
* **Virtualenv:** For isolating project dependencies.
* **Pip:** For package installation and requirements management.
