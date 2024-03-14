from ctypes import windll, byref, sizeof, c_int 
from wonderwords import RandomSentence
import customtkinter as ctk
from enum import Enum
import time

class Color(str, Enum):
    MAIN = '#352F44'
    FR_1 = '#5C5470'
    FR_2 = '#B9B4C7'
    TEXT = '#FAF0E6'
    RED =  '#D24545'
    GREEN= '#C5EBAA'
    GRAY = '#575261'

def destroy_old_page(page):
    children = page.winfo_children()
    children[-1].destroy()

def destroy_old_pages(page):
    for child in page.winfo_children():
        child.destroy()

def update_labels(typ_time, all_times, text, wps_label, points, avarge_accuracy, score_label, accuracy_save, speed_save):
    if typ_time[0] != 0:
        typ_time[1] = time.time()
    all_times.append(len(text)/(5.1*(typ_time[1] - typ_time[0]))*60)
    avarge_time = 0
    for item in all_times:
        avarge_time += item
    wps_label.configure(text=f'SPEED: {round((avarge_time / len(all_times)), 2)} WPM')
    accuracy = 0
    for item in points:
        accuracy += item
    avarge_accuracy.append((accuracy / len(points)))
    av_accuracy = 0
    for item in avarge_accuracy:
        av_accuracy += item
    score_label.configure(text=f'ACCURACY: {round((av_accuracy / (len(avarge_accuracy)-1)*100), 2)}%')
    accuracy_save[0] = round((av_accuracy / (len(avarge_accuracy)-1)*100), 2)
    speed_save[0] = round((avarge_time / len(all_times)), 2)
    save_results(accuracy_save[0], speed_save[0])

def listener(event, keys_history, label_1, check, text, typ_time, app,
            points, wps_label, all_times, avarge_accuracy, score_label,
            speed_save, accuracy_save, next_text, current_sentance, starting_time, menu):
    if menu[0] == 1:
        return
    if len(keys_history) == 0:
        typ_time[0] = time.time()
    characters = [  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    'space', 'period', 'minus', 'comma']
    if len(text) == len(keys_history) and event.keysym != 'BackSpace':
        current_sentance = next_text
        next_text = RandomSentence().sentence()
        destroy_old_pages(app)
        load_new_game(app, all_times, avarge_accuracy, speed_save, accuracy_save, next_text, current_sentance, starting_time, menu)
        return
    if event.keysym == 'BackSpace' and len(keys_history):
        keys_history.pop()
        points.pop()
        destroy_old_page(check)
    elif event.keysym == 'space' and text[len(keys_history)] == ' ':
        keys_history.append(' ')
        create_check_mark(check, Color.GREEN)
        points.append(1)
    elif event.keysym == 'period' and text[len(keys_history)] == '.':
        keys_history.append('.')
        create_check_mark(check, Color.GREEN)
        points.append(1)
    elif event.keysym == 'minus' and text[len(keys_history)] == '-':
        keys_history.append('-')
        create_check_mark(check, Color.GREEN)
        points.append(1)
    elif event.keysym == 'comma' and text[len(keys_history)] == ',':
        keys_history.append(',')
        create_check_mark(check, Color.GREEN)
        points.append(1)
    elif (event.keysym) == text[len(keys_history)]:
        keys_history.append(event.keysym)
        create_check_mark(check, Color.GREEN)
        points.append(1)
    elif event.keysym != text[len(keys_history)] and (event.keysym).lower() in characters:
        if event.keysym == 'space':
            keys_history.append(' ')
        elif event.keysym == 'period':
            keys_history.append('.')
        elif event.keysym == 'minus':
            keys_history.append('-')
        elif event.keysym == 'comma':
            keys_history.append(',')
        else:
            keys_history.append(event.keysym)
        create_check_mark(check, Color.RED)
        points.append(0)
    if len(text) == len(keys_history):
        update_labels(typ_time, all_times, text, wps_label, points, avarge_accuracy, score_label, accuracy_save, speed_save)
    label_1.configure(text=f'{''.join(keys_history)}')

def create_check_mark(check, color):
    label = ctk.CTkFrame(master=check, width=18, height=5, fg_color=color, corner_radius=0, bg_color=color)
    label.pack(side='left', padx=0)

def close_menu_frame(frame, app, menu):
    frame.destroy()
    app.bind('<Escape>', lambda event: quit_fullscreen(event, app))
    menu[0] = 0

def save_results(time_consumed, accuracy):
    with open('statistics.txt', 'a') as file:
        file.write(f'{time_consumed}, {accuracy}\n')

def plot_from_database():
    # here will be plot showing users statistics
    ...

def exit_app(app):
    app.destroy()

def menu_label(app, font_x30, menu):
    menu[0] = 1

    frame = ctk.CTkFrame(master=app, fg_color='#49425A')
    frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

    option_menu = ctk.CTkFrame(master=frame, fg_color=Color.FR_1)
    option_menu.pack(side='top', anchor='center', expand=True, padx=40, pady=30)

    button_1 = ctk.CTkButton(master=option_menu, text='RESUME', fg_color=Color.FR_2,
                            hover=False, text_color=Color.TEXT, font=font_x30, 
                            command= lambda: close_menu_frame(frame, app, menu))
    button_1.pack(side='top', padx=10, pady=10, fill='x')

    button_2 = ctk.CTkButton(master=option_menu, text='STATISTICS', fg_color=Color.FR_2, hover=False,
                            text_color=Color.TEXT, font=font_x30)
    button_2.pack(side='top', padx=10, pady=10, fill='x') # graphs to display in tkinter

    button_3 = ctk.CTkButton(master=option_menu, text='TIME CHALLENGE', fg_color=Color.FR_2, hover=False,
                            text_color=Color.TEXT, font=font_x30)
    button_3.pack(side='top', padx=10, pady=10, fill='x') # implement timed session

    button_4 = ctk.CTkButton(master=option_menu, text='QUIT', fg_color=Color.FR_2, hover=False,
                            text_color=Color.TEXT, font=font_x30, command=lambda: exit_app(app))
    button_4.pack(side='top', padx=10, pady=10, fill='x')

def load_new_game(app, all_times, avarge_accuracy, speed_save, accuracy_save, next_text, current_sentance, starting_time, menu):
    font_x30 = ctk.CTkFont(family='JetBrains Mono Regular', size=30)
    font_x21 = ctk.CTkFont(family='JetBrains Mono Regular', size=21)
    points = []
    keys_history = []
    typ_time = [0, 0]

    top_frame = ctk.CTkFrame(master=app, fg_color=Color.FR_1)
    top_frame.pack(side='top', fill='x', padx=10, pady=10)

    score_label = ctk.CTkLabel(master=top_frame, text=f'ACCURACY: {accuracy_save[0]}%', font=font_x21, text_color=Color.TEXT)
    score_label.pack(side='left', anchor='nw', padx=20, pady=10)

    wps_label = ctk.CTkLabel(master=top_frame, text=f'SPEED: {speed_save[0]} WPM', font=font_x21, text_color=Color.TEXT)
    wps_label.pack(side='right', anchor='ne', padx=20, pady=10)

    space_label = ctk.CTkLabel(master=app, text='\n\n')
    space_label.pack(side='top')

    frame_for_frame = ctk.CTkFrame(master=app, fg_color=Color.MAIN)
    frame_for_frame.pack(anchor='center', expand=True, pady=10, padx=40, fill='x')

    label_for_next = ctk.CTkLabel(master=frame_for_frame, text=next_text, font=font_x30, text_color=Color.GRAY)
    label_for_next.pack(side='bottom', anchor='n', pady=40)

    frame_for_frame_2 = ctk.CTkFrame(master=frame_for_frame, fg_color=Color.FR_1)
    frame_for_frame_2.pack(fill='x')

    frame = ctk.CTkFrame(master=frame_for_frame_2, fg_color=Color.FR_1)
    frame.pack(side='top', anchor='center', pady=10, padx=5)

    label = ctk.CTkLabel(master=frame, text=current_sentance, font=font_x30, text_color=Color.TEXT)
    label.pack(side='top', anchor='w', pady=10, padx=5)

    label_1 = ctk.CTkLabel(master=frame, text='' , font=font_x30, text_color=Color.TEXT)
    label_1.pack(side='top', anchor='w', pady=10, padx=5)

    check = ctk.CTkFrame(master=frame, height=5, fg_color=Color.FR_2)
    check.pack(side='bottom', padx=5, pady=5, fill='x')

    menu_frame = ctk.CTkFrame(master=app, fg_color=Color.FR_1)
    menu_frame.pack(side='bottom', fill='x', padx=10, pady=10)

    menu_button = ctk.CTkButton(master=menu_frame, fg_color=Color.FR_2, hover=False, text_color=Color.TEXT,
                                text='≡', font=font_x30, anchor='n', width=60, command= lambda: menu_label(app, font_x30, menu))
    menu_button.pack(side='right', padx=5, pady=5)

    app.bind('<Key>', lambda even: listener(even, keys_history, label_1, check, current_sentance, typ_time, app,
                                            points, wps_label, all_times, avarge_accuracy, score_label, speed_save,
                                            accuracy_save, next_text, current_sentance, starting_time, menu))

def bar_color(app):
    HWND = windll.user32.GetParent(app.winfo_id())
    DWMWA_CAPTION_COLOR = 35
    COLOR_1 = 0x00433034 # not equicalent to fg color in rest of the code idk why
    windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_CAPTION_COLOR, byref(c_int(COLOR_1)), sizeof(c_int)) 

def quit_fullscreen(event, app):
    app.attributes('-fullscreen', False)
    bar_color(app)

def go_fullscreen(event, app):
    app.attributes('-fullscreen', True)

def main():
    app = ctk.CTk()
    app.geometry('1080x720')
    app.minsize(1080, 720)
    app.title('')
    app.iconbitmap('logo.ico')
    app.configure(fg_color =Color.MAIN)
    # app.attributes('-fullscreen', True)

    bar_color(app)

    all_times = [0]
    avarge_accuracy = [0]
    speed_save = [0]
    accuracy_save = [0]
    menu = [0]
    starting_time = time.time()
    next_text = RandomSentence().sentence()
    current_sentance = RandomSentence().sentence()

    load_new_game(app, all_times, avarge_accuracy, speed_save, accuracy_save, next_text, current_sentance, starting_time, menu)

    app.bind('<Escape>', lambda event: quit_fullscreen(event, app))
    app.bind('<F11>', lambda event: go_fullscreen(event, app))

    app.mainloop()

if __name__ == "__main__":
    main()
