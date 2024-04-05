from wonderwords import RandomWord
import customtkinter as ctk
from enum import Enum
import enchant

class Color(str, Enum):
    MAIN = '#35374B'
    FRAM = '#354050'
    BUT1 = '#344955'
    BUT4 = '#64897F'
    TEXT = '#FAF0E6'
    GOOD = '#90D26D'
    ISIN = '#F3B95F'
    GRAY = '#31363F'

class Keyboard(ctk.CTkFrame):
    def __init__(self, master, font_x40):
        super().__init__(master, fg_color=Color.BUT1)

        self.font_x40 = font_x40

        self.frame1 = ctk.CTkFrame(self, fg_color=Color.BUT1)
        self.frame1.pack(padx=10, pady=10)
        self.q = ctk.CTkLabel(self.frame1, text='Q', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.q.pack(side='left', padx=4, pady=4)
        self.w = ctk.CTkLabel(self.frame1, text='W', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.w.pack(side='left', padx=4, pady=4)
        self.e = ctk.CTkLabel(self.frame1, text='E', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.e.pack(side='left', padx=4, pady=4)
        self.r = ctk.CTkLabel(self.frame1, text='R', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.r.pack(side='left', padx=4, pady=4)
        self.t = ctk.CTkLabel(self.frame1, text='T', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.t.pack(side='left', padx=4, pady=4)
        self.y = ctk.CTkLabel(self.frame1, text='Y', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.y.pack(side='left', padx=4, pady=4)
        self.u = ctk.CTkLabel(self.frame1, text='U', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.u.pack(side='left', padx=4, pady=4)
        self.i = ctk.CTkLabel(self.frame1, text='I', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.i.pack(side='left', padx=4, pady=4)
        self.o = ctk.CTkLabel(self.frame1, text='O', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.o.pack(side='left', padx=4, pady=4)
        self.p = ctk.CTkLabel(self.frame1, text='P', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.p.pack(side='left', padx=4, pady=4)

        self.frame2 = ctk.CTkFrame(self, fg_color=Color.BUT1)
        self.frame2.pack(padx=10, pady=10)
        self.a = ctk.CTkLabel(self.frame2, text='A', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.a.pack(side='left', padx=4, pady=4)
        self.s = ctk.CTkLabel(self.frame2, text='S', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.s.pack(side='left', padx=4, pady=4)
        self.d = ctk.CTkLabel(self.frame2, text='D', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.d.pack(side='left', padx=4, pady=4)
        self.f = ctk.CTkLabel(self.frame2, text='F', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.f.pack(side='left', padx=4, pady=4)
        self.g = ctk.CTkLabel(self.frame2, text='G', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.g.pack(side='left', padx=4, pady=4)
        self.h = ctk.CTkLabel(self.frame2, text='H', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.h.pack(side='left', padx=4, pady=4)
        self.j = ctk.CTkLabel(self.frame2, text='J', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.j.pack(side='left', padx=4, pady=4)
        self.k = ctk.CTkLabel(self.frame2, text='K', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.k.pack(side='left', padx=4, pady=4)
        self.l = ctk.CTkLabel(self.frame2, text='L', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.l.pack(side='left', padx=4, pady=4)

        self.frame3 = ctk.CTkFrame(self, fg_color=Color.BUT1)
        self.frame3.pack(padx=10, pady=10)
        self.z = ctk.CTkLabel(self.frame3, text='Z', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.z.pack(side='left', padx=4, pady=4)
        self.x = ctk.CTkLabel(self.frame3, text='X', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.x.pack(side='left', padx=4, pady=4)
        self.c = ctk.CTkLabel(self.frame3, text='C', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.c.pack(side='left', padx=4, pady=4)
        self.v = ctk.CTkLabel(self.frame3, text='V', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.v.pack(side='left', padx=4, pady=4)
        self.b = ctk.CTkLabel(self.frame3, text='B', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.b.pack(side='left', padx=4, pady=4)
        self.n = ctk.CTkLabel(self.frame3, text='N', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.n.pack(side='left', padx=4, pady=4)
        self.m = ctk.CTkLabel(self.frame3, text='M', corner_radius=7, fg_color=Color.BUT4, font=self.font_x40, text_color=Color.TEXT)
        self.m.pack(side='left', padx=4, pady=4)

        self.alphabet= [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m,
                        self.n, self.o, self.p, self.q, self.r, self.s, self.t, self.u, self.v, self.w, self.x, self.y, self.z]

    def change_tile_color(self, index, correct):
        if correct == 0:
            self.alphabet[index].configure(fg_color=Color.GOOD)
        if correct == 1 and self.alphabet[index].cget('fg_color') != Color.GOOD:
            self.alphabet[index].configure(fg_color=Color.ISIN)
        if correct == 2:
            self.alphabet[index].configure(fg_color=Color.GRAY)

    def restore(self):
        for item in self.alphabet:
            item.configure(fg_color=Color.BUT4)

class App(ctk.CTk):
    def __init__(self, width: int, height: int):
        super().__init__(fg_color=Color.MAIN)

        self.word = RandomWord().word(word_min_length=5, word_max_length=5)
        self.current_index = 0
        self.title('WORDLE')

        self.font_x40 = ctk.CTkFont(family='JetBrains Mono', size=40)
        self.geometry(f'{width}x{height}+{self.winfo_screenmmwidth()+55}+{self.winfo_screenmmheight()//4}')
        self.bind('<Key>', lambda event: self.get_user_input(event))

        self.main_frame = ctk.CTkFrame(self, fg_color=Color.MAIN)
        self.main_frame.pack(side='top', expand=True)

        self.frame = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264, corner_radius=5)
        self.frame.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses = ctk.CTkLabel(self.frame, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses.pack(fill='x', padx=5, pady=5)
        self.check_frame = ctk.CTkFrame(self.frame, width=234, height=10, corner_radius=0)
        self.check_frame.pack(anchor='s')

        self.frame1 = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264)
        self.frame1.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses1 = ctk.CTkLabel(self.frame1, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses1.pack(fill='x', padx=5, pady=5)
        self.check_frame1 = ctk.CTkFrame(self.frame1, width=234, height=10, corner_radius=0)
        self.check_frame1.pack(anchor='s')

        self.frame2 = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264)
        self.frame2.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses2 = ctk.CTkLabel(self.frame2, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses2.pack(fill='x', padx=5, pady=5)
        self.check_frame2 = ctk.CTkFrame(self.frame2, width=234, height=10, corner_radius=0)
        self.check_frame2.pack(anchor='s')

        self.frame3 = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264)
        self.frame3.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses3 = ctk.CTkLabel(self.frame3, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses3.pack(fill='x', padx=5, pady=5)
        self.check_frame3 = ctk.CTkFrame(self.frame3, width=234, height=10, corner_radius=0)
        self.check_frame3.pack(anchor='s')

        self.frame4 = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264)
        self.frame4.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses4 = ctk.CTkLabel(self.frame4, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses4.pack(fill='x', padx=5, pady=5)
        self.check_frame4 = ctk.CTkFrame(self.frame4, width=234, height=10, corner_radius=0)
        self.check_frame4.pack(anchor='s')

        self.frame5 = ctk.CTkFrame(self.main_frame, fg_color=Color.FRAM, width=264)
        self.frame5.pack(side='top', fill='y', padx=5, pady=5)
        self.guesses5 = ctk.CTkLabel(self.frame5, text=' ', font=self.font_x40, anchor='nw', width=264, text_color=Color.TEXT)
        self.guesses5.pack(fill='x', padx=5, pady=5)
        self.check_frame5 = ctk.CTkFrame(self.frame5, width=234, height=10, corner_radius=0)
        self.check_frame5.pack(anchor='s')

        # self.frames_list = [self.frame, self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]
        self.guesses_list = [self.guesses, self.guesses1, self.guesses2, self.guesses3, self.guesses4, self.guesses5]
        self.check_frames_list = [self.check_frame, self.check_frame1, self.check_frame2, self.check_frame3, self.check_frame4, self.check_frame5]

        self.keyboard = Keyboard(self, self.font_x40)
        self.keyboard.pack(side='bottom', expand=True)

        self.alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def get_user_input(self, event):
        if self.current_index == 6:
            return
        prev = self.guesses_list[self.current_index].cget('text')
        if len(prev) < 10 and event.keysym in self.alphabet:
            self.guesses_list[self.current_index].configure(text=f'{prev + event.keysym.upper()} ')
        if event.keysym == 'BackSpace' and len(prev) > 1:
            self.guesses_list[self.current_index].configure(text=f'{prev[:-2].upper()}')
        if len(prev) > 10 and event.keysym == 'Return' and self.is_word(prev.replace(' ', '')):
            self.check_letters(prev.replace(' ', '').lower())

    def is_word(self, word):
        dictionary = enchant.Dict('en_US')
        return dictionary.check(word)

    def mark(self, frame, correct):
        if correct == 0:
            mark_frame = ctk.CTkFrame(master=frame, fg_color=Color.GOOD, width=48, height=10, corner_radius=0)
            mark_frame.pack(side='left', padx=0, pady=0)
        if correct == 1:
            mark_frame = ctk.CTkFrame(master=frame, fg_color=Color.ISIN, width=48, height=10, corner_radius=0)
            mark_frame.pack(side='left', padx=0, pady=0)
        if correct == 2:
            mark_frame = ctk.CTkFrame(master=frame, fg_color=Color.GRAY, width=48, height=10, corner_radius=0)
            mark_frame.pack(side='left', padx=0, pady=0)

    def check_letters(self, user_word):
        if self.current_index == 6:
            return
        counter = 0
        word_list = [lett for lett in self.word]
        correct_list = []
        for i, letter in enumerate(user_word):
            if letter in word_list:
                correct_list.append(letter)
                word_list.remove(letter)
                if user_word[i].strip() == self.word[i]:
                    self.mark(self.check_frames_list[self.current_index], 0)
                    self.keyboard.change_tile_color(self.alphabet.index(user_word[i]), 0)
                    counter += 1
                else:
                    self.mark(self.check_frames_list[self.current_index], 1)
                    self.keyboard.change_tile_color(self.alphabet.index(user_word[i]), 1)
            else:
                self.mark(self.check_frames_list[self.current_index], 2)
                self.keyboard.change_tile_color(self.alphabet.index(user_word[i]), 2)
        self.current_index += 1
        if counter == 5:
            self.after(500, lambda: self.win_label('YOU WON'))
            self.after(5000, lambda: self.win_lose())
            return
        elif self.current_index == 6:
            self.after(500, lambda: self.win_label('YOU LOST'))
            self.after(5000, lambda: self.win_lose())
            return

    def win_label(self, _text):
        win_frame = ctk.CTkFrame(self, fg_color=Color.GRAY, corner_radius=10)
        win_frame.place(relx=0.5, rely=0.4, anchor='center')
        text = ctk.CTkLabel(win_frame, text=_text, font=('JetBrains Mono', 100))
        text.pack(anchor='center', expand=True, padx=10, pady=10)
        self.after(4500, lambda: win_frame.destroy())

    def win_lose(self):
        for i in range(6):
            self.guesses_list[i].configure(text=' ')
            self.destroy_children(self.check_frames_list[i])
        self.keyboard.restore()
        self.current_index = 0
        self.word = RandomWord().word(word_min_length=5, word_max_length=5)

    def destroy_children(self, frame):
        for child in frame.winfo_children():
            child.destroy()

def main():
    ctk.deactivate_automatic_dpi_awareness()
    app = App(750, 840)
    app.mainloop()

if __name__ == "__main__":
    main()
