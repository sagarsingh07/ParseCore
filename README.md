
# LR Parser for Source Code Analysis: A Compiler Front-End Tool

## 📌 Project Overview
This project is a compiler front-end tool that implements an LR parser (LALR(1)) for a simplified programming language. It includes lexical analysis, parsing, error detection, and a command-line interface. A GUI-based visualization module is planned for the next phase.

## 👨‍💻 Team: ParseCore
- **Agam Gairola** (Team Lead) – Coordination, Testing, Integration
- **Abhishek Singh** – Parser Implementation, Tree Logic, CLI Integration
- **Sagar Singh** – Lexer, Token Definitions, GUI Plannin

## 🛠️ Technologies Used
- Python 3.x
- PLY (Python Lex-Yacc)
- Command-line interface
- (GUI with Tkinter/Matplotlib – *Upcoming*)

## 📁 Project Structure
```
LR_Parser_Project/
│
├── lexer.py             # Lexical analyzer (tokenizer)
├── parser.py            # LALR(1) grammar and parse rules
├── main.py              # CLI interface and integration
├── examples/            # Sample expressions and inputs
└── README.md            # This file
```

## ✅ Features Implemented
- Grammar and tokens for arithmetic expressions
- Lexical analysis using PLY
- LALR(1) parsing rules with precedence handling
- Error handling and expression validation
- CLI-based interaction and test cases

## 🚧 Phase 3 Goals
- Parse tree visualization (graphical)
- Simplified GUI interface
- Full-scale testing and documentation

## 🧪 Sample Test
```bash
$ python3 main.py
Enter expression (or press Enter to quit): 3 + 5 * (10 - 2)
Parsed successfully: ('+', 3, ('*', 5, ('-', 10, 2)))
```

## 📝 License
This project is for academic use under the Project-Based Learning (PBL) initiative at GEU.
