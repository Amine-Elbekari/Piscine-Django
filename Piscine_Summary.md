# 🐍 Python & Django Piscine - 42 Network / 1337

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-LTS-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 👋 Overview

This repository documents my intensive dive into Python and full-stack web development during the **1337 (42 Network) Django Piscine**. The curriculum is structured to build understanding from the ground up: starting with raw scripts and manual HTML generation, moving to SQL and ORM internals, and culminating in real-time asynchronous web applications.

Below is a breakdown of the specific modules and the problems I solved in each.

---

## 🏗️ Module 00: Initiation
**Focus:** Web Fundamentals, HTTP, & Strict Standards

Before touching a backend language, this module enforced a rigorous understanding of the frontend standards that Django eventually abstracts away. It wasn't just about "making it look good," but about strict compliance and understanding the request cycle.

* **Shell Scripting:** Wrote a script (`myawesomescript.sh`) to decode shortened `bit.ly` URLs using `curl` and text processing tools, stripping away abstractions to see raw HTTP headers.
* **Strict HTML/CSS:** Built a resume and a contact form from scratch, adhering to strict W3C validation standards without reliance on frameworks.
* **Reverse Engineering:** Replicated a specific webpage design (pixel-perfect) using only the provided assets and CSS, learning to interpret design specs accurately.

## 🐍 Module 00: Starting
**Focus:** Python Syntax & Data Structures

This module was the "bootcamp within a bootcamp," designed to transition from C to Python. It focused on Pythonic syntax, data manipulation, and the language's philosophy.

* **Data Structures:** Solved algorithmic problems using dictionaries and lists to manage and sort data (e.g., mapping musicians to their birth years).
* **Periodic Table Generator:** Created a script that parses a raw text file of chemical elements and programmatically generates a valid HTML Periodic Table, bridging the gap between data processing and frontend rendering.

## 🧩 Module 00: OOB (Object Oriented Basics)
**Focus:** Advanced OOP & Pythonic Design Patterns

Here, I built a custom template engine and an HTML generator to deeply understand Object-Oriented Programming in Python, specifically inheritance and magic methods.

* **Templating Engine:** Built a lightweight template rendering script (`render.py`) that parses `.template` files and injects context variables—essentially recreating a tiny version of Django's Jinja2 engine.
* **"The Elem Class":** The core project of this module. I architected a Python class system that generates valid HTML trees. By overloading standard operators (like `__str__` and `__add__`), I created a tool where Python objects compile directly into HTML tags.
* **Validation Logic:** Implemented a recursive validation method (`is_valid()`) to ensure the generated HTML structure adhered to strict nesting rules (e.g., `<ul>` can only contain `<li>`).

---

## 📦 Module 01: Libraries
**Focus:** Environment Management, Scraping, & APIs

Modern development relies on the ecosystem. This module covered package management (`pip`, `virtualenv`) and interacting with external data.

* **Environment Management:** Wrote scripts to automate the setup of virtual environments and dependency installation, ensuring reproducibility.
* **API Interaction:** Built a CLI tool to query the Wikipedia API and format the results, handling JSON responses and error states gracefully.
* **Web Scraping (BeautifulSoup):** Developed "Roads to Philosophy," a scraper that navigates Wikipedia links to test the theory that all articles eventually link to the "Philosophy" page, handling cycles and dead ends.

## 🌐 Module 01: Base Django
**Focus:** The Django Framework & MVT Architecture

My first steps into Django proper. The goal was to understand the Model-View-Template architecture without relying on "magic" shortcuts.

* **Django Configuration:** Set up a multi-app project structure, configuring the `settings.py` and `urls.py` for modular design.
* **Template Inheritance:** Utilized Django's DTL (Django Template Language) to create a DRY (Don't Repeat Yourself) frontend using `base.html`, blocks, and includes.
* **Forms & Persistence:** Built a persistent input history system where data submitted via a form is logged to a file and displayed with timestamps, teaching me about data persistence outside of a database.

---

## 🗄️ Module 02: ORM (Object-Relational Mapping)
**Focus:** SQL vs. ORM

This was a comparative study. I had to implement the exact same features twice: once using raw SQL with `psycopg2`, and again using Django's ORM. This solidified my understanding of what the ORM actually does under the hood.

* **Raw SQL:** Manually wrote queries to `CREATE`, `INSERT`, `UPDATE`, and `DELETE` data for a "Movies" database, handling database connections and cursors directly.
* **Django Models:** Re-implemented the schema using Django Models, exploring Field types, primary keys, and auto-timestamps.
* **Relationships:** Modeled complex relationships (Foreign Keys for Planets/People, Many-to-Many for Movies/Characters) and queried them efficiently.

---

## 🔐 Module 03: Sessions
**Focus:** Authentication, Cookies, & Business Logic

This module focused on user state. I built a "Life Pro Tips" application that required complex session management and permission logic.

* **Anonymous Sessions:** Implemented a system where unregistered users are assigned temporary, random usernames that persist for a set duration using session cookies.
* **Custom Auth:** Built a full registration and login system, replacing Django's default User model with a custom implementation to handle reputation scoring.
* **Reputation System:** Engineered a permission system (similar to StackOverflow) where user rights (voting, deleting posts) are dynamically granted based on a "Reputation" score derived from upvotes/downvotes.

## 🚀 Module 03: Advanced
**Focus:** Generic Views & Internationalization

Refactoring and optimizing. I took standard function-based views and converted them into robust, reusable Class-Based Views.

* **Class-Based Views (CBV):** Refactored application logic to use Django’s `ListView`, `DetailView`, and `CreateView`, strictly avoiding function-based views to enforce cleaner architecture.
* **Internationalization (i18n):** Implemented Django's translation hooks to make the application multilingual, switching languages based on URL prefixes (e.g., `/en/`, `/fr/`).
* **Unit Testing:** Wrote a suite of tests to verify permission logic and view accessibility, ensuring that unauthorized users couldn't bypass frontend restrictions.

---

## ⚡ Module 03: Final (Real-time Web)
**Focus:** AJAX, Websockets, & Asynchronous Django

The final challenge broke the request/response cycle. I built a real-time chat application.

* **AJAX Authentication:** Created a login/logout flow that communicates entirely via AJAX, updating the DOM without page reloads.
* **Websockets (Django Channels):** Built a chatroom that uses Websockets to push messages instantly to all connected clients.
* **Async Features:** Implemented a live user list that updates when users join/leave, and a persistent message history that loads seamlessly upon connection.