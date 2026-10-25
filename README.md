# Number Guessing Game 🎯

An interactive command-line Python game where the computer generates a secret random number between 1 and 100, and the player tries to guess it in the fewest attempts possible.

## ✨ Features
- **Random Number Generation:** Uses Python's built-in `random` module to pick a secret number between 1 and 100 every game.
- **Crash-Proof Input Validation:** Implements `try-except` (`ValueError`) handling so the game doesn't crash if a user enters text instead of a number.
- **Boundary Checks:** Alerts the player if their guess is out of bounds (less than 1 or greater than 100) without wasting a turn.
- **Dynamic Hints & Attempt Tracking:** Guides the player with `"Too low!"` or `"Too high!"` hints and tracks the total number of attempts taken to win.

## 🚀 How to Run

1. Make sure **Python 3** is installed on your computer.
2. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/python-number-guessing-game.git](https://github.com/devsalilpandey/python-number-guessing-game.git)
   ```
3. Navigate to the project folder:
   ```bash
   cd python-number-guessing-game
   ```
4. Run the game script:
   ```bash
   python guessing_game.py
   ```

## 🖥️ Example Gameplay
```text
Welcome to the Guessing Game!
Please enter your guess (between 1 and 100): abc
Invalid input. Please enter a number between 1 and 100.
Please enter your guess (between 1 and 100): 150
Your guess is out of bounds. Please try again.
Please enter your guess (between 1 and 100): 50
Too low! Try again.
Please enter your guess (between 1 and 100): 75
Too high! Try again.
Please enter your guess (between 1 and 100): 62
Congratulations! You've guessed the secret number 62 in 3 attempts!
```

## 🤝 Acknowledgments / Credits
- **Code & Logic Implementation:** Written and tested by me as part of my Python learning journey.
- **Project Blueprint & Documentation:** Structured with the guidance of **Google Gemini AI**.