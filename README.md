# 🕹️ Pong The Game

A Python recreation of the classic Pong arcade game using the turtle graphics module. It supports two-player gameplay, real-time ball-paddle interactions, and live score tracking. This is a beginner-friendly project made with clean, modular, and object-oriented code.

---

## ✨ Features

-   Two-player paddle controls
-   Ball with bounce physics and speed scaling
-   Scoreboard display
-   Wall collision detection
-   Modular codebase with OOP principles

---

## 🎮 Controls

| Player | Move Up      | Move Down      |
| ------ | ------------ | -------------- |
| Left   | W            | S              |
| Right  | ↑ (Up Arrow) | ↓ (Down Arrow) |

---

## 🛠️ Requirements

Make sure you have the following installed:

-   Python 3.7 or higher
-   turtle (comes with the Python standard library)

You can check Python version using:

```bash
python --version
```

Install Python from https://www.python.org/downloads/ if needed.

---

## 🚀 Getting Started

### 📦 Clone the Repository

```bash
git clone https://github.com/Itsmesachin98/pong-the-game.git
cd pong-the-game
```

### ▶️ Run the Game

```bash
python3 main.py
```

The game window should open and you can start playing!

---

## 📁 Project Structure

```
pong-the-game/
├── main.py            # Main game loop
├── paddle.py          # Paddle class (controls movement)
├── ball.py            # Ball class (movement, bounce logic)
├── scoreboard.py      # Scoreboard class (display & score updates)
├── check.py           # Vertical coordinate test helper
└── README.md          # Project documentation
```

---

## 🧠 How It Works

-   Ball starts at center and moves diagonally.
-   It bounces off the top and bottom walls.
-   If it touches a paddle, it bounces back and speeds up.
-   If it goes out of bounds, the opposing player scores.
-   Score is updated and ball resets to center.

---

## 💡 Future Improvements

-   Sound effects on bounce or score
-   Single player mode (add basic AI)
-   Main menu and game-over screen
-   Settings menu with difficulty options

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the game, feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add YourFeature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software for personal or commercial purposes.

See the LICENSE file for more info.
