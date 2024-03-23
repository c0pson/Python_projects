from wonderwords import RandomWord
import customtkinter as ctk
from enum import Enum
import enchant

class Color(str, Enum):
    MAIN = '#35374B'
    FRAM = '#354050'
    BUT1 = '#344955'
    BUT2 = '#425E68'
    BUT3 = '#425E68'
    BUT4 = '#64897F'
    BUT5 = '#78A083'
    TEXT = '#FAF0E6'

class App(ctk.CTk):
    def __init__(self, width: int, height: int):
        super().__init__(fg_color=Color.MAIN)

        self.word = RandomWord().word(word_min_length=5, word_max_length=5)

        self.font_x40 = ctk.CTkFont(family='JetBrains Mono', size=40)
        self.geometry(f'{width}x{height}+{self.winfo_screenheight()//2-self.winfo_screenmmwidth()//4}+{self.winfo_screenmmheight()//2}')
        self.bind('<Key>', lambda event: self.get_user_input(event))

        self.frame = ctk.CTkFrame(self, fg_color=Color.FRAM, width=264)
        self.frame.pack(side='top', fill='y', padx=10, pady=10)
        self.guesses = ctk.CTkLabel(self.frame, text=' ', font=self.font_x40, anchor='nw', width=264)
        self.guesses.pack(fill='x')

    def get_user_input(self, event):
        prev = self.guesses.cget('text')
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if len(prev) < 10 and event.keysym in alphabet:
            self.guesses.configure(text=f'{prev + event.keysym.upper()} ')
        else:
            print(self.guesses.winfo_width())
        if event.keysym == 'BackSpace' and len(prev) > 1:
            self.guesses.configure(text=f'{prev[:-2].upper()}')
        if len(prev) > 10 and event.keysym == 'Return' and self.is_word(prev.replace(' ', '')):
            print('nice')

    def is_word(self, word):
        dictionary = enchant.Dict('en_US')
        return dictionary.check(word)

    def check_letters(self):
        ...

def main():
    ctk.deactivate_automatic_dpi_awareness()
    app = App(1080, 720)
    app.mainloop()

if __name__ == "__main__":
    main()
