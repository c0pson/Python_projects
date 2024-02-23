import customtkinter as ctk
from customtkinter import filedialog

PURPLE_1 = '#1F2544'
PURPLE_2 = '#474F7A'
PURPLE_3 = '#81689D'
PURPLE_4 = '#FFD0EC'

#--------------------------------file handling-------------------------------------#
def try_opening_file(file_name):
    try:
        open(file_name, 'r')
        return 1
    except FileNotFoundError:
        return 0

def get_file_name():
    file_name = ''.join(file_opened)
    if file_name == '':
        file_name = filedialog.askopenfilename()
    return file_name

def modify_before_saving():
    text = text_box.get('0.0', 'end')
    text = text.replace('\n\n', '\n').rstrip('\n')
    return text
#--------------------------------file handling-------------------------------------#


#------------------------------------buttons---------------------------------------#
def click_button_open():
    file_name = filedialog.askopenfilename()
    if try_opening_file(file_name):
        text_box.delete('0.0', 'end')
        with open(file_name, 'r') as file:
            content = file.read()
            content = content.replace('\n\n', '\n')
            text_box.insert('end', content)
        file_opened.clear()
        file_opened.append(file_name)
        file.close()
        app.title(f'File: {file_name}')

def click_button_save():
    text = modify_before_saving()
    file_name = get_file_name()
    if try_opening_file(file_name):
        with open(file_name, 'w') as file:
            file.write(text)
        file.close()

def click_button_help():
    print('instruction')
#------------------------------------buttons---------------------------------------#


#--------------------------------------root----------------------------------------#
app = ctk.CTk()
app.geometry('1280x780')
app.title('Note ')
font_size = 23
my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=font_size)
file_opened = []
#--------------------------------------root----------------------------------------#


#-------------------------------right side of screen-------------------------------#
right_frame = ctk.CTkFrame(master=app, fg_color=PURPLE_1, corner_radius=0)
right_frame.pack(side='right',fill='both', expand=True, padx=0, pady=0)
    # content of right frame

text_box = ctk.CTkTextbox(master=right_frame, font=my_font, fg_color=PURPLE_2, corner_radius=6, activate_scrollbars=False)
text_box.pack(side='right', fill='both', expand=True, padx=10, pady=10)
#-------------------------------right side of screen-------------------------------#


#-------------------------------left side of screen--------------------------------#
left_frame = ctk.CTkFrame(master=app, fg_color=PURPLE_1, corner_radius=0)
left_frame.pack(side='top', fill='both', expand=True, padx=0, pady=0)
    #content of left side

open_button = ctk.CTkButton(master=left_frame, font=my_font, fg_color=PURPLE_3, corner_radius=6, text='Open', command=click_button_open)
open_button.pack(side='top', padx=10, pady=10)

open_button = ctk.CTkButton(master=left_frame, font=my_font, fg_color=PURPLE_3, corner_radius=6, text='Save', command=click_button_save)
open_button.pack(side='top', padx=10, pady=0)

open_button = ctk.CTkButton(master=left_frame, font=my_font, fg_color=PURPLE_3, corner_radius=6, text='Help', command=click_button_help)
open_button.pack(side='bottom', padx=10, pady=10)
#-------------------------------left side of screen--------------------------------#

app.mainloop()
