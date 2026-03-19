# 🎮 Python Mini Game Collection

> *A collaborative Python project by three developers — building games, learning together.*

---

## 👥 Team

| Avatar | Name | GitHub |
|--------|------|--------|
| 🧑‍💻 | **Abdulkadir** | [@abdulkadir-yz](https://github.com/abdulkadir-yz) |
| 🧑‍💻 | **Efe** | [@efeglr](https://github.com/efeglr) |
| 🧑‍💻 | **Andrew** | [@agvn23](https://github.com/agvn23) |

---
## Mentor
| Avatar | Name | GitHub |
|--------|------|--------|
| 🧑‍💻 | **Maria** | [@mariblan](https://github.com/mariblan) |
---
## 📌 Project Overview

A collection of **three console-based mini games** built in Python. The project focuses on applying core programming fundamentals — loops, conditionals, functions — in a hands-on, playful way, while also practicing real-world **team collaboration** using Git and GitHub workflows.

---

## 🎯 Learning Objectives

By completing this project, we will:

- ✅ Gain experience structuring small Python programs
- ✅ Learn how to use randomness, loops, and user input
- ✅ Practice writing clean, reusable functions
- ✅ Improve debugging and testing skills
- ✅ Build confidence by shipping playable, working games
- ✅ Practice collaborative coding in a team
- ✅ Improve Git & GitHub flow (branches, PRs, reviews)

---

## 🕹️ The Games

### 1. 🎲 Number Guessing Game
> The computer picks a random number between **1 and 100** — can you guess it?

- Computer randomly selects a secret number
- Player guesses repeatedly until correct
- Program gives hints after each guess: **"Too high!"** / **"Too low!"**

**Concepts practiced:**
- `random.randint` for random number generation
- `while` loops for repeated prompting
- `if / else` conditionals for feedback logic

---

### 2. ✊✋✌️ Rock, Paper, Scissors
> Classic hand game — you vs. the computer!

- Player picks: `rock`, `paper`, or `scissors`
- Computer randomly selects its move
- Winner is determined and displayed
- *(Optional: track score across multiple rounds)*

**Concepts practiced:**
- Lists for storing choices
- Randomness (`random.choice`)
- Nested conditionals for win logic
- Simple scoring system

---

### 3. ❌⭕ Tic-Tac-Toe
> The ultimate 3×3 showdown — two players, one board.

- Two players take turns on a `3×3` grid displayed in the console
- Game automatically detects a **winner** or a **draw**
- Clean board rendering after each move

**Concepts practiced:**
- 2D list (or 1D list of 9 cells) for board state
- Functions for win/draw detection
- Loops for managing player turns
- Grid printing with formatted output

---

## 📋 Menu System

All three games are tied together with a single interactive menu:

```
===== Python Mini Games =====
1. Play Number Guessing
2. Play Rock, Paper, Scissors
3. Play Tic-Tac-Toe
4. Exit
==============================
Choose an option:
```

- Choosing `1`, `2`, or `3` launches the corresponding game
- Choosing `4` exits the program gracefully
- Any invalid input prompts the user to try again

**Concepts practiced:**
- Lists for storing menu options
- Functions for menu logic
- Loops for continuous prompting until valid input

---

## 🗄️ Data Structures Used

| Game | Data Structure |
|------|---------------|
| Number Guessing | `int` (single number) |
| Rock, Paper, Scissors | `list` — `["rock", "paper", "scissors"]` |
| Tic-Tac-Toe | `list` — 2D or 1D list of 9 cells |
| Menu System | `list` of option strings |

---

## 🗓️ Weekly Breakdown

| Days | Task |
|------|------|
| Day 1–2 | 🎲 Game 1: Number Guessing Game |
| Day 1–2 | ✊ Game 2: Rock, Paper, Scissors |
| Day 3–5 | ❌ Game 3: Tic-Tac-Toe |
| Day 4–5 | 📋 Menu System & Integration |

---

## 🏗️ Project Structure

```
mini-game-collection/
│
├── main.py           # Entry point — runs the menu system
├── games/
│   ├── guessing.py   # Number Guessing Game
│   ├── rps.py        # Rock, Paper, Scissors
│   └── tictactoe.py  # Tic-Tac-Toe
│
└── README.md
```

---

## 🚀 How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Clone the repository
git clone https://github.com/YOUR-REPO-URL.git

# Navigate into the project folder
cd mini-game-collection

# Run the game
python main.py
```

---

## 🔀 Git Workflow

We follow a **feature-branch workflow**:

1. Create a branch for each game or feature
   ```bash
   git checkout -b feature/number-guessing
   ```
2. Commit your changes with clear messages
   ```bash
   git commit -m "feat: add number guessing game logic"
   ```
3. Push and open a **Pull Request** for review
4. Get approval from at least one teammate before merging to `main`

**Branch naming convention:**
- `feature/game-name` — for new game implementations
- `fix/bug-description` — for bug fixes
- `chore/task-description` — for housekeeping tasks

---

## 🐍 Code Base

```python
import random

# NUMBER GUESSING GAME
def number_guessing_game():
    pass  # TODO: implement

# ROCK, PAPER, SCISSORS
def rock_paper_scissors():
    pass  # TODO: implement

# TIC-TAC-TOE
def print_board(board):
    pass  # TODO: implement

def check_winner(board):
    pass  # TODO: implement

def tic_tac_toe():
    pass  # TODO: implement

# MENU SYSTEM
def main_menu():
    pass  # TODO: implement

# Run the program
main_menu()
```

---

## 📈 Progress Tracker

- [ ] 🎲 Number Guessing Game — complete
- [ ] ✊ Rock, Paper, Scissors — complete
- [ ] ❌ Tic-Tac-Toe — complete
- [ ] 📋 Menu System — integrated
- [ ] 🧪 All games tested
- [ ] 📝 README finalized

---

*Built with 🐍 Python and ☕ good vibes — WBS Coding School, 2026*
