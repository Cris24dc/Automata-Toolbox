# 🚀 Automata Toolbox

![Banner](https://private-user-images.githubusercontent.com/107889454/420669273-eacd5b56-9a68-467c-9ba9-3e4e73e482de.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE1MjI0NjMsIm5iZiI6MTc0MTUyMjE2MywicGF0aCI6Ii8xMDc4ODk0NTQvNDIwNjY5MjczLWVhY2Q1YjU2LTlhNjgtNDY3Yy05YmE5LTNlNGU3M2U0ODJkZS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwOVQxMjA5MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04YTcxNDZlODk1NmU3MjUxYmY2ODE4ODUyYzNmNzAwNjlmOTNiMWMwMDgxZTE0MjNhNmEzZjIxYTRhMzUzYzM2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ce5uiWvmN9Pg1q1db3e3aBYBKMEUMP6ZHvYwAavPIjg)

## 🌟 Overview

**Automata Toolbox** is a powerful Python framework for simulating various types of automata in computational theory. It supports the following automaton types:

- 🤖 **Deterministic Finite Automata (DFA)**
- 🔀 **Non-Deterministic Finite Automata (NFA)**
- 📚 **Pushdown Automata (PDA)**
- 🎭 **Context-Free Grammar (CFG)**

This framework enables users to **define and execute automata** using structured configuration files or Python classes, offering utilities for **parsing, validation, and execution** of automata.

📌 **PyPI Package**: [Automata Toolbox on PyPI](https://pypi.org/project/automata-toolbox/)

---

## 🎯 Features

✅ **Complete Automata Simulation** - Supports DFA, NFA, PDA, and CFG.  
✅ **Structured Configuration** - Define automata using `.cfg` configuration files.  
✅ **Python API** - Programmatically create and run automata.  
✅ **Command-Line Interface (CLI)** - Manage automata directly from the terminal.  
✅ **Modular & Extensible** - Easily customizable and extendable.  

---

## 📥 Installation

**Requires Python 3.7+**. Install via pip:
```bash
pip install automata-toolbox
```
Or install from source:
```bash
git clone https://github.com/Cris24dc/Automata-Toolbox.git
cd Automata-Toolbox
pip install -e .
```

---

## 🖥 CLI Usage

### 🔧 **Generate an Automaton Template**
```bash
automata generate dfa my_dfa
```
Supported types: `dfa`, `nfa`, `pda`, `cfg`.

### 🏃 **Run a DFA on an Input String**
```bash
python3 -m toolbox.main config/my_dfa.cfg abba
```

---

## 🐍 Using the Python API

### 🎯 **Creating and Running a DFA**
```python
from toolbox import DFA

dfa = DFA("config/example.cfg")
if dfa.is_valid():
    print("✅ DFA is valid")
    print("Result:", dfa.run("abba"))
```

### 🔄 **Using an NFA**
```python
from toolbox import NFA

nfa = NFA("config/example_nfa.cfg")
if nfa.is_valid():
    print("✅ NFA is valid")
    print("Result:", nfa.run("abba"))
```

---

## ⚙️ Configuration Files
Each automaton type uses a `.cfg` file structured as follows:

### 📌 **DFA Configuration Example**
```
[Sigma]
a
b
end

[States]
q0
q1
end

[Start]
q0
end

[Final]
q1
end

[Delta]
q0 a q1
q1 b q0
end
```

### 📌 **CFG Configuration Example**
```
[Variables]
S
end

[Terminals]
a
b
end

[Rules]
S -> aSb
S -> $
end
```

---

## 🔧 Development & Contribution
Want to contribute? Follow these steps:
1. 🍴 **Fork the repository**
2. 🌿 **Create a new branch**: `git checkout -b feature-xyz`
3. 💾 **Commit changes**: `git commit -m "Added feature XYZ"`
4. 🚀 **Push to GitHub**: `git push origin feature-xyz`
5. 🔄 **Submit a pull request**

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact
For inquiries or contributions, reach out via **cristianandrei752@gmail.com** or visit the **[GitHub Repository](https://github.com/Cris24dc/Automata-Toolbox.git)**.

🔗 Also available on **[PyPI](https://pypi.org/project/automata-toolbox/)** 🚀
