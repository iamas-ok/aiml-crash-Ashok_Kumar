# aiml-crash-Ashok_Kumar Day1 - Task

![Python](https://img.shields.io/badge/Python-3.13.5+-blue?logo=python&logoColor=white)

---

## Repository Structure

```
aiml-crash-Ashok_Kumar/
└── Day1_Task/
    ├── intro.py
    ├── skills_counter.py
    ├── even_odd.py
    ├── tip_calculator.py
    ├── word_frequency.py
    ├── calculator.py
    ├── grade_classifier.py
    ├── guessing_game.py
    └── contact_book.py
```

---

## Day 1 — Practice Tasks (10 Tasks)

| # | File | Description | Run |
|---|------|-------------|-----|
| [Task1](./intro.py) | `intro.py` | Self-intro using variables, dicts, and f-strings with str methods | `python intro.py` |
| [Task2](./skills_counter.py) | `skills_counter.py` | Skills list with numbered for loop and enumerate() explore | `python skills_counter.py` |
| [Task3](./even_odd.py) | `even_odd.py` | Even/odd checker with user input, modulo operator, and try/except | `python even_odd.py` |
| [Task4](./tip_calculator.py) | `tip_calculator.py` | Tip calculator function returning a dict with tip and total | `python tip_calculator.py` |
| [Task5](./word_frequency.py) | `word_frequency.py` | Word frequency counter using dicts, sorted by frequency | `python word_frequency.py` |
| [Task6](./calculator.py) | `calculator.py` | Simple calculator with 4 functions and dict-based dispatch | `python calculator.py` |
| [Task7](./grade_classifier.py) | `grade_classifier.py` | Grade classifier using list of dicts, sorted with lambda | `python grade_classifier.py` |
| [Task8](./guessing_game.py) | `guessing_game.py` | Number guessing game with while loop and 7-attempt limit | `python guessing_game.py` |
| [Task9](./contact_book.py) | `contact_book.py` | Mini contact book with case-insensitive search function | `python contact_book.py` |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/iamas-ok/aiml-crash-Ashok_Kumar.git
cd aiml-crash-Ashok_Kumar/Day1_Task

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3.Install dependencies
python --version
```

---

## 🧠 Quick Reference — Key Concepts Covered

| Concept | Where Used | Description |
|---------|------------|-------------|
| Variables & f-strings | [Task1](./intro.py) | Store data in variables and format output using f-strings |
| Dictionaries | [Task1](./intro.py), [Task4](./tip_calculator.py), [Task7](./grade_classifier.py), [Task9](./contact_book.py) | Key-value pairs for structured data storage |
| `str.upper()`, `str.lower()`, `str.title()` | [Task1](./intro.py) | String methods to change text casing |
| `for` loop & `len()` | [Task2](./skills_counter.py) | Iterate over a list and count its elements |
| `enumerate()` | [Task2](./skills_counter.py) | Loop with automatic index — cleaner than manual counters |
| `if` / `elif` / `else` | [Task3](./even_odd.py), [Task6](./calculator.py), [Task7](./grade_classifier.py) | Conditional branching based on a value |
| Modulo operator `%` | [Task3](./even_odd.py) | Returns remainder — used to check even/odd |
| `input()` & `int()` | [Task3](./even_odd.py), [Task6](./calculator.py), [Task8](./guessing_game.py) | Accept user input and convert to integer |
| `try` / `except` | [Task3](./even_odd.py), [Task6](./calculator.py) | Handle errors gracefully without crashing |
| Functions & `return` | [Task4](./tip_calculator.py), [Task5](./word_frequency.py), [Task6](./calculator.py), [Task7](./grade_classifier.py), [Task9](./contact_book.py) | Reusable blocks of code that return a value |
| `float` math | [Task4](./tip_calculator.py) | Decimal arithmetic for money calculations |
| `return` vs `print` | [Task4](./tip_calculator.py) | `return` passes a value; `print` only displays it |
| `str.split()` & counting | [Task5](./word_frequency.py) | Split sentence into words and count occurrences |
| `collections.Counter` | [Task5](./word_frequency.py) | One-line word frequency counter from standard library |
| `sorted()` with `key=lambda` | [Task5](./word_frequency.py), [Task7](./grade_classifier.py) | Sort lists or dicts by a custom rule using lambda |
| Dict of functions (dispatch) | [Task6](./calculator.py) | Map strings to functions — cleaner than if/elif chains |
| List of dicts | [Task7](./grade_classifier.py), [Task9](./contact_book.py) | Store multiple records as a list of dictionaries |
| `while` loop | [Task8](./guessing_game.py) | Repeat until a condition is met |
| `random` module | [Task8](./guessing_game.py) | Generate random numbers with `random.randint()` |
| Case-insensitive search | [Task9](./contact_book.py) | Use `.lower()` on both sides to match regardless of case |

---