import customtkinter as ctk
from enum import Enum
import random
import time

class Colors(str, Enum):
    MAIN = '#00224D'
    FR_1 = '#5D0E41'
    FR_2 = '#A0153E'
    FR_3 = '#FF204E'
    TEXT = '#FAF0E6'

def update_score(points, score_label_list):
    score_label_list[0].configure(text=f'Score: {points[0]}')

def points_label(app, points, score_label_list):
    score_frame = ctk.CTkFrame(master=app, height=100, fg_color=Colors.MAIN)
    score_frame.pack(side='top', fill='x', anchor='n', padx=5, pady=5)
    font_x21 = ctk.CTkFont(family='Hack Nerd Font Regular', size=21)
    score_text = ctk.CTkLabel(master=score_frame, text=f'Score: {points[0]}', text_color=Colors.TEXT,
                            font=font_x21)
    score_text.pack(side='left', anchor='w', padx=10, pady=10)
    score_label_list[0] = score_text

def timer(app, main_frame, target, size, points, call_id, start_time, score_label_list):
    if call_id[0]:
        app.after_cancel(call_id[0])
    if time.time() - start_time > 2:
        points[0] -= 2  # not 1 bcs in replace 1 is added 
        replace_target(app, main_frame, target, size, points, call_id, score_label_list)
        return
    call_id[0] = app.after(500, lambda: timer(app, main_frame, target, size, points, call_id, start_time, score_label_list))

def replace_target(app, main_frame, target, size, points, call_id, score_label_list):
    target.place(x=random.randrange(0, int(main_frame._current_width-size)),
                y=random.randrange(0, int(main_frame._current_height-size)))
    points[0] += 1
    update_score(points, score_label_list)
    timer(app, main_frame, target, size, points, call_id, time.time(), score_label_list)

def training_frame(app, size, points, call_id, score_label_list):
    main_frame = ctk.CTkFrame(master=app, fg_color=Colors.MAIN)
    main_frame.pack(side='top', fill='both', expand=True, padx=5, pady=5)
    target = ctk.CTkButton(master=main_frame, corner_radius=50, fg_color=Colors.FR_2, hover_color=Colors.FR_1, text='',
                            width=40, height=40, command=lambda: replace_target(app, main_frame, target, size, points, call_id, score_label_list))
    target.place(x=random.randrange(0, int(main_frame._current_width-size)),
                y=random.randrange(0, int(main_frame._current_height-size)))

def main():
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    app.geometry('1080x720')
    points = [0]
    call_id = [None]
    score_label_list = ['']
    points_label(app, points, score_label_list)
    training_frame(app, 40, points, call_id, score_label_list)
    app.mainloop()

if __name__ == "__main__":
    main()
