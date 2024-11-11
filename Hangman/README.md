# Hangman Game

Welcome to the Hangman Game! This is a fun and interactive game where players guess letters to uncover a hidden word. The game features categories such as Animals, Countries, Fruits, and Colours. Enjoy the challenge and see how many mistakes you can make before losing!

## Preview

![Preview](https://github.com/IHEfty/Hangman/blob/main/res/01.gif "demo.py") ![Preview](https://github.com/IHEfty/Hangman/blob/main/res/02.gif "main.y")

## Features

- **Multiple Categories**: Choose from various categories including Animals, Countries, Fruits, and Colours.
- **Visual Representation**: Each incorrect guess displays a hangman image, giving a visual cue of your progress.
- **Sound Effects**: Experience immersive gameplay with sound effects for winning and losing.
- **User-Friendly Interface**: Built using Tkinter for a simple and clean user interface.

## Requirements

To run this project, you need Python 3 and the following packages:

- `pygame`
- `tkinter` (usually comes pre-installed with Python)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IHEfty/Hangman.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Hangman
   ```

3. Install the required packages:

   ```bash
   pip install tkinter
   pip install pygame
   ```

4. Run the game:

   ```bash
   python main.py
   ```

## How to Play

1. When the game starts, a category will be displayed.
2. You will see underscores representing the letters of the hidden word.
3. Enter a letter in the text box and press **Enter** or click the **Guess** button.
4. If your guess is incorrect, the hangman image will update to reflect the number of incorrect guesses.
5. The game ends when you either guess the word correctly or make too many incorrect guesses.

## Resources

- **Images**: All hangman images are located in the `res` folder.
- **Sound Effects**: `win.wav` and `lose.wav` sound files are used for feedback on the game's outcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## Acknowledgements

- [Pygame](https://www.pygame.org/) for the sound functionalities.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI interface.

---

Enjoy playing Hangman!
