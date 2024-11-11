import random
import tkinter as tk
from tkinter import messagebox, PhotoImage
import pygame  

class Word:
    def __init__(self):
        self.categories = {
            'Countries': ['colombia', 'indonesia', 'madagascar', 'netherlands', 
                          'portugal', 'switzerland', 'thailand', 'venezuela', 
                          'poland', 'germany', 'italy', 'greece', 
                          'spain', 'russia', 'australia', 'argentina', 
                          'egypt', 'morocco'],
            'Animals': ['lion', 'tiger', 'elephant', 'panda', 'camel', 
                        'horse', 'spider', 'fox', 'rabbit', 'kangaroo', 
                        'turtle', 'hamster'],
            'Fruits': ['apple', 'banana', 'watermelon', 'pear', 
                       'strawberry', 'raspberry', 'orange'],
            'Colours': ['red', 'purple', 'pink', 'brown', 
                        'yellow', 'white', 'black', 'green', 'blue'],
        }
        self.category = ''
        self.chosen_word = ''

    def draw_word(self):
        self.category = random.choice(list(self.categories.keys()))
        self.chosen_word = random.choice(self.categories[self.category])
    
    def get_chosen_word(self):
        return self.chosen_word
    
    def get_category(self):
        return self.category

class Hangman:
    def __init__(self):
        self.mistakes = 0
        self.hangman_imgs = [
            'res/hangman0.png', 'res/hangman1.png', 'res/hangman2.png', 
            'res/hangman3.png', 'res/hangman4.png', 'res/hangman5.png', 
            'res/hangman6.png', 'res/hangman7.png', 'res/hangman8.png', 
            'res/hangman9.png', 'res/hangman10.png'
        ]
        self.max_mistakes = len(self.hangman_imgs) - 1

    def set_hangman(self, label):
        img_path = self.hangman_imgs[self.mistakes]
        img = PhotoImage(file=img_path)
        label.config(image=img)
        label.image = img  

    def add_mistake(self):
        if self.mistakes < self.max_mistakes:
            self.mistakes += 1

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.word_obj = Word()
        self.hangman_obj = Hangman()
        self.guessed_letters = set()
        
        pygame.mixer.init()
        self.win_sound = pygame.mixer.Sound('res/win.wav')  
        self.lose_sound = pygame.mixer.Sound('res/lose.mp3') 
        
        self.title("Hangman Game")
        self.geometry("400x500")  
        
        self.hangman_label = tk.Label(self)
        self.hangman_label.pack(pady=10)

        self.category_label = tk.Label(self, text="", font=("Arial", 14))
        self.category_label.pack(pady=10)

        self.word_label = tk.Label(self, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.make_guess)  

        self.guess_button = tk.Button(self, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.play_game()

    def play_game(self):
        self.word_obj.draw_word()
        self.category_label.config(text=f"Category: {self.word_obj.get_category()}")
        self.update_display_word()
        self.hangman_obj.mistakes = 0
        self.hangman_obj.set_hangman(self.hangman_label)  

    def update_display_word(self):
        chosen_word = self.word_obj.get_chosen_word()
        displayed_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in chosen_word])
        self.word_label.config(text=displayed_word)

    def make_guess(self, event=None): 
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            messagebox.showwarning("Warning", "You've already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)
        chosen_word = self.word_obj.get_chosen_word()
        
        if guess not in chosen_word:
            self.hangman_obj.add_mistake()
            self.hangman_obj.set_hangman(self.hangman_label)
            if self.hangman_obj.mistakes == self.hangman_obj.max_mistakes:
                self.lose_sound.play()  
                messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{chosen_word}'.")
                self.reset_game()
        else:
            self.update_display_word()
            if all(letter in self.guessed_letters for letter in chosen_word):
                self.win_sound.play()  
                messagebox.showinfo("Congratulations!", "You won!")
                self.reset_game()

    def reset_game(self):
        self.guessed_letters.clear()
        self.play_game()

if __name__ == "__main__":
    app = HangmanGame()
    app.mainloop()
