import customtkinter as ctk
import random

class Points():
    points = 0
    def __init__(self) -> None:
        pass

    def print_points(self) -> None:
        print(self.points)

    @classmethod
    def add_point(cls) -> int:
        cls.points += 1
        return cls.points

    @classmethod
    def rem_point(cls) -> int:
        cls.points -= 1
        return cls.points

def timer():
    ...

def replace_target(main_frame, target, size, points):
    target.place(x=random.randrange(0, int(main_frame._current_width-size)),
                y=random.randrange(0, int(main_frame._current_height-size)))

def training_frame(main_frame, size, points):
    target = ctk.CTkButton(master=main_frame, text='', corner_radius=100,
                            width=40, height=40, command=lambda: replace_target(main_frame, target, size, points))
    target.place(x=random.randrange(0, int(main_frame._current_width-size)),
                y=random.randrange(0, int(main_frame._current_height-size)))

def main():
    app = ctk.CTk()
    points = Points()
    score_frame = ctk.CTkFrame(master=app, height=100)
    score_frame.pack(side='top', fill='x', anchor='n', padx=0, pady=0)
    main_frame = ctk.CTkFrame(master=app)
    main_frame.pack(side='top', fill='both', expand=True, padx=0, pady=0)
    training_frame(main_frame, 40, points)
    app.mainloop()

if __name__ == "__main__":
    main()
