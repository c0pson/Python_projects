import customtkinter as ctk
from enum import Enum
import random
import time

class Colors(str, Enum):
    MAIN = '#222831'

class target_button(ctk.CTkButton):
    points = 0
    _time = time.time()
    def __init__(self, master, text: str, size: tuple[int, int]):
        self._text = text
        self._size = size
        self.after_id = None
        master.bind('<Button>', lambda e: self.punishment(e))
        super().__init__(master, text=self._text, command=self.button_callback,
                        corner_radius=100, width=size[0], height=size[1])
        self.place(x=100, y=100)
        self.replace_button_after_time()

    def button_callback(self):
        self.place(x=random.randrange(0, self.master.winfo_width()-self._size[0]), y=random.randrange(0, self.master.winfo_height()-self._size[1]))
        target_button._time = time.time()
        target_button.points += 1
        if self.after_id:
            self.master.after_cancel(self.after_id)
        print(target_button.points)
        self.replace_button_after_time()

    def replace_button_after_time(self):
        if time.time() - target_button._time >= 2.0:
            target_button.points -= 2
            target_button._time = time.time()
            self.button_callback()
            if self.after_id:
                self.master.after_cancel(self.after_id)
            self.after_id = self.replace_button_after_time()
            return
        if self.after_id:
            self.master.after_cancel(self.after_id)
        self.after_id = self.master.after(501, self.replace_button_after_time)

    @classmethod
    def punishment(cls, e):
        cls.points -= 1
        print(cls.points)

    @classmethod
    def return_points(cls):
        return cls.points

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=Colors.MAIN)
        self.geometry('1080x720')
        self.title('Mouse training')

        self.top_frame = ctk.CTkFrame(self, height=100)
        self.top_frame.pack(side='top', fill='x')
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(fill='both', expand=True)
        self.after(100, self.create_button)

    def create_button(self):
        butto1 = target_button(self.frame, '', (40, 40))

if __name__ == "__main__":
    app = App()
    app.mainloop()
