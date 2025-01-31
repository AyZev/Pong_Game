# 🏓 Ping Pong Game

## 📌 Introduction
This is a **Ping Pong Game** developed using `Pygame`. The game features a **single-player mode**, where the player competes against an AI-controlled paddle. The objective is to **score points** by hitting the ball past the opponent. The first player to reach **3 points** wins.

## 🎮 Features
- 🏓 **Smooth gameplay** with AI-controlled paddle movement.
- 🔊 **Sound effects** for ball hits, game start, and game over.
- 🎨 **Customizable background images** and colors.
- 🎹 **Keyboard controls** for paddle movement.
- 🏆 **Game Over screen** with replay and exit options.

## 🛠 Installation

Make sure you have **Python** installed along with `Pygame`.

### Install Pygame
```
pip install pygame
```
## 🎮 Controls
- ⬆ **Arrow Up (`↑`)** → Move paddle **up**
- ⬇ **Arrow Down (`↓`)** → Move paddle **down**
- ⎋ **ESC** → Quit the game
- 🛑 **Spacebar** → Restart after **Game Over**

## 🏆 Game Rules
- 🎮 The player controls the **right paddle**.
- 🤖 The AI controls the **left paddle**.
- 🔄 The ball **bounces off** the paddles and walls.
- ✅ If the ball **passes the AI's paddle**, the player **gains a point**.
- ❌ If the ball **passes the player's paddle**, the AI **gains a point**.
- 🏅 First to **3 points** wins!

## 🎨 Customization
- **Change AI difficulty**: Modify the `difficulty` variable in `main.py` to adjust AI response speed.
- **Change background**: Replace `image.jpg` or `15133.jpg` in the `Assets` folder.
- **Modify paddle speed**: Adjust `paddle_velocity_y` in `main.py`.

## 🔗 Dependencies
- 🐍 **Python 3.x**
- 🎮 **Pygame**

## 📜 License
This project is open-source under the **MIT License**. Feel free to **modify and distribute** it.

## File Structure 
```
📂 ping-pong-game/
├── main.py              # Main game script
├── Assets/
│   ├── RGB_Colors.py    # Color definitions
│   ├── pong.ogg         # Ball hit sound
│   ├── game_start.ogg   # Game start sound
│   ├── game_over.ogg    # Game over sound
│   ├── image.jpg        # Background image
│   ├── 15133.jpg        # Alternative background
│   ├── Font.ttf         # Game font
```