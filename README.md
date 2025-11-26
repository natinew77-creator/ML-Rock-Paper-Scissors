# Rock Paper Scissors AI

## 🔗 Live Demonstration

### 🚀 Launch Live VS Code Environment

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/natinew77-creator/ML-Rock-Paper-Scissors)
> **Note:** Click the "Run on Replit" button above.



## Project Overview
This project is a Machine Learning solution for the **Rock Paper Scissors** challenge from freeCodeCamp. The goal was to create an AI player that can consistently beat four different bots (Quincy, Abbey, Kris, and Mrugesh) with a **win rate of at least 60%**.

## Strategy & Algorithm
The solution uses a **Markov Chain** strategy (Pattern Matching) to predict the opponent's next move.
* **History Tracking:** The AI keeps a history of the opponent's last `n` moves.
* **Pattern Recognition:** It looks for sequences (e.g., "Rock -> Paper -> Rock") to determine what the opponent is most likely to throw next.
* **Counter-Move:** Based on the prediction, the AI calculates the ideal counter-move to win.
* **Dynamic Reset:** The strategy resets its memory between matches to adapt to different opponents.

## Final Results
My AI successfully defeated all four bots with the following win rates:

| Opponent | Win Rate | Result |
| :--- | :--- | :--- |
| **Quincy** | **99.59%** | Passed |
| **Abbey** | **60.79%** |  Passed |
| **Kris** | **72.67%** |  Passed |
| **Mrugesh** | **63.00%** |  Passed |

## Technologies
* **Python**
* **Replit** (for testing and execution)
