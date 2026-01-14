# 🧩 Day 00: Object Oriented Basics (OOB)

> **Focus:** Advanced Python OOP, Inheritance, Magic Methods, and Recursive Design Patterns.

## 📝 Overview

While Module 00 started with syntax, the **OOB (Object Oriented Basics)** module shifted the focus to architectural design. The goal was to master Python's object-oriented paradigms before applying them in Django.

Instead of just writing classes, I was tasked with building a **Template Engine** and a **Programmatic HTML Generator** from scratch. This provided deep insight into how frameworks like Django internally handle template rendering and DOM validation.

## 📂 Project Breakdown

### 📝 Ex00: The Template Engine (`render.py`)
**Concepts:** File I/O, String Substitution, Settings Management
A simulation of a basic template renderer (like Jinja2).
* **Task:** Created a script that reads a `.template` file and a `settings.py` file. It parses the template and replaces placeholders (e.g., `{name}`) with the corresponding values from the settings, generating a final HTML resume.
* **Skill:** Regular expressions and dynamic attribute mapping.

### ☕ Ex01: The Intern (`intern.py`)
**Concepts:** Class Instantiation, Error Handling
A humorous warm-up to class mechanics.
* **Task:** Modeled an `Intern` class that "works" (by raising an Exception) and makes coffee.
* **Logic:** Defined custom behavior where specific methods trigger specific exception types, requiring try/except blocks in the test suite to handle the workflow gracefully.

### 🍵 Ex02: Inheritance & DRY (`beverages.py`)
**Concepts:** Inheritance, Overriding, Polymorphism
* **Task:** Built a hierarchy of `HotBeverage` classes (`Coffee`, `Tea`, `Chocolate`, `Cappuccino`).
* **Architecture:** Used a base class to define common attributes (price, name) and derived classes to override specific details, enforcing the **DRY (Don't Repeat Yourself)** principle.

### ⚙️ Ex03: The Machine (`machine.py`)
**Concepts:** Composition, State Management, Custom Exceptions
* **Task:** Created a `CoffeeMachine` class that interacts with the beverage classes from Ex02.
* **Logic:** The machine has a lifecycle—it breaks down after serving 10 drinks and requires a `repair()` call. Attempting to use a broken machine raises a custom `BrokenMachineException`.
* **Randomness:** Implemented logic where the machine occasionally fails to serve the correct drink, returning an `EmptyCup` instead.

### 🏗️ Ex04: The Element Class (`elem.py`)
**Concepts:** Recursive Data Structures, Magic Methods
The core technical challenge of this day.
* **Task:** Architected a generic `Elem` class representing an HTML DOM node.
* **Implementation:**
    * Utilized `__str__` to recursively render the element and all its children into a valid HTML string.
    * Implemented `add_content` to dynamically append text or other `Elem` objects to the tree.
    * This allowed writing Python code that compiles directly into HTML.

### 🏷️ Ex05: Tag Wrappers (`elements.py`)
**Concepts:** Subclassing, API Design
* **Task:** Built specific classes for standard HTML tags (`Html`, `Head`, `Body`, `Div`, `Span`, etc.) that inherit from `Elem`.
* **Outcome:** Simplified the API. Instead of `Elem('div')`, I could instantiate `Div()`. This made the Python code look almost exactly like the HTML structure it represented.

### 🛡️ Ex06: The Validator (`Page.py`)
**Concepts:** Tree Traversal, Validation Logic
* **Task:** Created a `Page` class that wraps an HTML tree and performs strict validation before rendering.
* **Rules Engine:** Implemented a recursive `is_valid()` method that checks strict nesting rules (e.g., `<ul>` can only contain `<li>`, `<html>` must contain `<head>` then `<body>`).
* **Constraint:** If any node in the tree violates these rules, the entire page is flagged as invalid.

## 🚀 How to Run

1.  **Template Engine (Ex00):**
    ```bash
    python3 ex00/render.py ex00/myCV.template
    # Output: Generates a 'myCV.html' file with injected values.
    ```

2.  **OOP Tests (Ex01 - Ex03):**
    These files contain their own test blocks.
    ```bash
    python3 ex01/intern.py
    python3 ex03/machine.py
    ```

3.  **HTML Generator (Ex04 - Ex06):**
    You can run the provided tests to see the HTML generation and validation in action.
    ```bash
    python3 ex06/Page.py
    # Output: Prints valid HTML to stdout if the tree structure is correct.
    ```

## 🛠️ Tools Used
* **Python 3:** Core language.
* **OOP Patterns:** Inheritance, Composition, Exception Handling.
* **Algorithms:** Recursive Tree Traversal (for HTML generation and validation).
