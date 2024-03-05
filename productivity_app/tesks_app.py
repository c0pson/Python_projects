import customtkinter as ctk
from enum import Enum
import datetime
import time

class Colors(str, Enum):
    ONYX  ='#352F44'
    BLACK_CORAL = '#5C5470'
    GRAY_X11 = '#B9B4C7'
    LINEN = '#FAF0E6'
    GRAPHITE = '#3D3B40'

########################################### general cases  ###########################################

def destroy_old_pages(frame):
    for child in frame.winfo_children():
        child.destroy()

########################################### general cases  ###########################################

########################################### files operation ##########################################

def read_task_info(task_name, line):
    ...

########################################### files operation ##########################################

########################################### index of tasks ###########################################

def show_task(task_list_1, task_list_2, current_task, task, task_info_frame, my_font):
    if current_task[0] != '':
        task_list_1[int(task_list_2.index(current_task[0]))].configure(fg_color=Colors.GRAY_X11)
    task.configure(fg_color=Colors.ONYX)
    current_task[0] = task.cget('text')
    load_task_info(task_info_frame, my_font, datetime.datetime.fromtimestamp(time.time()))

def create_task(frame, task_name, my_font, task_list_1, task_list_2, current_task, task_info_frame):
    task = ctk.CTkButton(master=frame, text=task_name, font=my_font, fg_color=Colors.GRAY_X11,
                        hover_color=Colors.GRAPHITE, text_color=Colors.LINEN, command=lambda:
                        show_task(task_list_1, task_list_2, current_task, task, task_info_frame, my_font))
    task.pack(side='top', padx=5, pady=5, fill='x')
    task_list_1.append(task)
    task_list_2.append(task.cget('text'))

########################################### index of tasks ###########################################

############################################# tasks info #############################################

def load_task_info(task_info_frame, my_font, creation_date):
    destroy_old_pages(task_info_frame)
    date_of_creation_label = ctk.CTkLabel(master=task_info_frame, font=my_font,
                                        text=creation_date.strftime("%Y-%m-%d %H:%M"))
    date_of_creation_label.pack(pady=5, padx=5)

############################################# tasks info #############################################

def main():
    app = ctk.CTk(fg_color=Colors.ONYX)
    app.geometry('1080x720')
    app.title('')
    font_x21 = ctk.CTkFont(family='Hack Nerd Font Propo', size=21)

    task_list_1 = []
    task_list_2 = []
    current_task = ['']

    list = [i+1 for i in range(5)]

    task_info_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLACK_CORAL, border_width=3, border_color=Colors.GRAY_X11)
    task_info_frame.pack(side='right', padx=10, pady=10, fill='both', expand=True)

    tasks_index_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLACK_CORAL, border_width=3, border_color=Colors.GRAY_X11)
    tasks_index_frame.pack(side='left', padx=10, pady=10, fill='y')
    space = ctk.CTkLabel(master=tasks_index_frame, text='', height=2, font=('Arial', 2))
    space.pack(side='top', padx=4, pady=4)
    task_text_label = ctk.CTkLabel(master=tasks_index_frame, text='Tasks:', font=font_x21, anchor='s')
    task_text_label.pack(side='top', padx=10, pady=5, anchor='s')
    scroll = ctk.CTkScrollableFrame(master=tasks_index_frame, fg_color=Colors.BLACK_CORAL)
    scroll.pack(fill='both', padx=5, pady=5, expand=True)
    for item in list:
        create_task(scroll, item, font_x21, task_list_1, task_list_2, current_task, task_info_frame)

    app.mainloop()

if __name__ == "__main__":
    main()
