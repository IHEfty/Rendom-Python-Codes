# ColorDots

ColorDots is a classic Dots and Boxes game implemented using Python's Tkinter library. Players take turns connecting dots to form boxes, with the goal of creating as many boxes as possible. The player who completes the most boxes wins the game.

## Features

- **Two-player mode**: Play against a friend locally.
- **Customizable player names**: Set player names through a configuration file.
- **Dynamic gameplay**: The game board updates in real-time as players take their turns.
- **Visual feedback**: Boxes are shaded to indicate ownership.
- **Score display**: The game shows the current score and announces the winner at the end.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IHEfty/ColorDots.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd ColorDots
   ```

3. Ensure you have Python installed (preferably Python 3.6 or later). You can download it from [python.org](https://www.python.org/downloads/).

4. Install the necessary libraries if not already installed:
   ```bash
   pip install numpy
   ```

5. Create a configuration file named `config.ini` in the project directory with the following content:
   ```ini
   [Players]
   player1_name = Player 1
   player2_name = Player 2
   ```

## Usage

Run the game by executing the following command in your terminal:
```bash
python main.py
```

## Gameplay

1. The game starts with an empty board. Players take turns clicking on the lines to create connections between dots.
2. If a player completes a box, they are rewarded with an extra turn.
3. The game continues until no more moves can be made.
4. At the end of the game, the scores are displayed, and a winner is announced.

## Contributing

If you would like to contribute to the project, feel free to submit a pull request or open an issue. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
