# 🏗️ Day 00: Web Fundamentals & Initiation

> **Focus:** HTTP Protocols, Semantic HTML5, CSS3 Architecture, and Legacy JS Integration.

## 📝 Overview

This module is the foundational layer of the Django Piscine. Before using a framework like Django to generate HTML, I was required to demonstrate a mastery of the underlying technologies. The exercises here focus on **strict standards compliance** (W3C), **raw HTTP manipulation**, and **frontend architecture** without frameworks.

The goal was to understand the *mechanics* of the web—how a browser renders a form, how HTTP headers redirect traffic, and how to structure a document semantically.

## 📂 Project Breakdown

### 🔧 Ex00: The HTTP Script (`myawesomescript.sh`)
**Tech:** Bash, `curl`, `grep`, `cut`
A raw shell script designed to handle HTTP redirection manually.
**The Challenge:** Resolve a shortened `bit.ly` URL to its actual destination without using a browser.
**Implementation:** Used `curl` to fetch headers and text processing tools (`grep`/`cut`) to extract the location, mirroring how backend services handle redirects programmatically.

### 📄 Ex01: Semantic Resume (`cv.html`)
**Tech:** HTML5, CSS3
A strict exercise in separation of concerns (Structure vs. Style).
**Constraints:** required the use of specific tags (`<h1>`, `<table>`, `<ul>`) and precise styling (merged table borders, specific hex codes like `#424242`).
**Takeaway:** enforced the discipline of keeping CSS separate from HTML structure, a critical skill before moving to Django Templates.

### 📨 Ex02: The Contact Form (`form.html`)
**Tech:** HTML5 Forms, Legacy Javascript
Building a robust frontend interface that integrates with pre-existing, immutable code.
**Legacy Integration:** I had to integrate a "black box" Javascript file (`popup.js`) written by a third party.I was strictly forbidden from modifying this file, simulating a real-world scenario of supporting legacy dependencies [cite: 598-600].
**HTML5 Features:** Utilized specific input types (`tel`, `email`, `number`) to leverage browser-native validation.

### 🕵️ Ex03: Pixel Perfect (`copy.html`)
**Tech:** CSS Reverse Engineering
A simulation of a frontend implementation task based on a design mock.
**The Scenario:** "Industrial Espionage"—replicating a competitor's website using only a screenshot and a provided (immutable) CSS file.
**The Challenge:** I had to reverse-engineer the HTML structure required to make the provided CSS render correctly.This tested my ability to read and understand CSS selectors and layouts deeply.

### 🧩 Ex04: JS Snippets (`snippets.html`)
**Tech:** Javascript Imports, DOM Manipulation
***Task:** Correctly import and sequence four distinct Javascript files (`file1.js` through `file4.js`) to trigger a specific DOM event (a popup).
***Constraint:** No inline Javascript was allowed; purely script tag management.

### ✅ Ex05: W3C Validation (`index.html`)
**Tech:** HTML Standards, Debugging
* **Task:** I was given a "broken" HTML file full of syntax errors and non-standard tags.
***Objective:** Refactor the code to pass the official **W3C Validator** with **0 Errors and 0 Warnings**, without removing the actual content. This emphasized the importance of standards compliance for accessibility and SEO.

## 🚀 How to Run

1.  **Shell Script (Ex00):**
    ```bash
    cd ex00
    ./myawesomescript.sh bit.ly/1072s3U
    # Expected Output: [http://42.fr/](http://42.fr/)
    ```

2.  **HTML Projects (Ex01 - Ex05):**
    These are static files. You can open them directly in any modern browser.

## 🛠️ Tools Used
* **W3C Validator:** For strict code compliance.
* **Curl:** For inspecting HTTP headers.
* **Browser DevTools:** For debugging CSS layouts and JS console errors.
