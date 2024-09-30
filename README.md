

---

# Rock, Paper, Scissors 🎮

This is a Python implementation of the classic **Rock, Paper, Scissors** game. You can play against the computer by selecting one of the three options: rock, paper, or scissors. The program will randomly generate a choice for the computer and determine the winner.

## How It Works

1. The player chooses **rock (0)**, **paper (1)**, or **scissors (2)** by entering the corresponding number.
2. The computer makes a random selection.
3. Both the player's and computer's choices are displayed using ASCII art.
4. The winner is determined based on the following rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
5. The game announces if it is a **win**, **loss**, or **draw**.

## ASCII Art
Here are the ASCII art representations for **Rock**, **Paper**, and **Scissors**:

### Rock:
```
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
```

### Paper:
```
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
```

### Scissors:
```
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
```


   ```

## Usage

1. When prompted, **enter 0 for Rock**, **1 for Paper**, or **2 for Scissors**.
2. The computer will make a random choice, and the game will display both selections using ASCII art.
3. The result (win, loss, or draw) will be printed.

### Example:

```bash
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: 0

You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You lose!
```

