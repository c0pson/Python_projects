import customtkinter as ctk
from customtkinter import filedialog

def click_button_open():
    file_opened.clear()
    file_name = filedialog.askopenfilename()
    with open(file_name, 'r') as file:
        content = file.read()
        content.replace('\n\n', '\n')
        text_box.insert('end', content)
    file_opened.append(file_name)
    file.close()
    app.title(f'{file_name}')

def click_button_save():
    file_name_copy = ''.join(file_opened)
    if file_name_copy == '':
        file_name_copy = filedialog.askopenfilename()
    text = text_box.get('0.0', 'end')
    text = text.replace('\n\n', '\n')
    lines = text.split('\n')
    modified_text = '\n'.join(line + '\n' for line in lines)
    for _ in range(2):
        if modified_text.endswith('\n'):
            modified_text = modified_text[:-1]
    with open(file_name_copy, 'w') as file:
        file.write(modified_text)
    file.close()

def click_button_help():
    print('help')

#--------------------------------------root----------------------------------------#
app = ctk.CTk()
app.geometry('1280x780')
app.title('Note ')
my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=23)
file_opened = []
#--------------------------------------root----------------------------------------#


#-------------------------------right side of screen-------------------------------#
right_frame = ctk.CTkFrame(master=app, fg_color='gray', corner_radius=0)
right_frame.pack(side='right',fill='both', expand=True, padx=0, pady=0)
    # content of right frame

text_box = ctk.CTkTextbox(master=right_frame, font=my_font, corner_radius=6)
text_box.pack(side='top', fill='both', expand=True, padx=5, pady=5)

#-------------------------------right side of screen-------------------------------#


#-------------------------------left side of screen--------------------------------#
left_frame = ctk.CTkFrame(master=app, fg_color='gray', corner_radius=0)
left_frame.pack(side='top', fill='both', expand=True, padx=0, pady=0)
    #content of left side

open_button = ctk.CTkButton(master=left_frame, fg_color='dark gray', corner_radius=6, text='Open', command=click_button_open)
open_button.pack(side='top', padx=10, pady=10)

open_button = ctk.CTkButton(master=left_frame, fg_color='dark gray', corner_radius=6, text='Save', command=click_button_save)
open_button.pack(side='top', padx=10, pady=0)

open_button = ctk.CTkButton(master=left_frame, fg_color='dark gray', corner_radius=6, text='Help', command=click_button_open)
open_button.pack(side='bottom', padx=10, pady=10)

#-------------------------------left side of screen--------------------------------#

app.mainloop()
