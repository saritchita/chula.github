import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "gor gai"),
    ("\u0E02", "kho khai"),
    ("\u0E03", "kho kuat"),
    ("\u0E04", "kho khwai"),
    ("\u0E05", "kho khon"),
    ("\u0E06", "kho rakhang"),
    ("\u0E07", "ngo ngu"),
    ("\u0E08", "cho chan"),
    ("\u0E09", "cho ching"),
    ("\u0E0A", "cho chang"),
]

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = random.choice(thai_consonants)
        
        self.card_label = tk.Label(root, text="", font=("Arial", 60))
        self.card_label.pack(pady=20)
        
        self.show_consonant_button = tk.Button(root, text="Show Consonant", command=self.show_consonant)
        self.show_consonant_button.pack()
        
        self.show_name_button = tk.Button(root, text="Show Name", command=self.show_name)
        self.show_name_button.pack()
        
        self.name_label = tk.Label(root, text="", font=("Arial", 30))
        self.name_label.pack(pady=20)
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text="?")
        self.name_label.config(text="")
    
    def show_consonant(self):
        self.card_label.config(text=self.current_card[0])
    
    def show_name(self):
        self.name_label.config(text=self.current_card[1])

# Run the application
root = tk.Tk()
game = ThaiFlashcardGame(root)
root.mainloop()
