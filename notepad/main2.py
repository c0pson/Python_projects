import customtkinter as ctk
from customtkinter import filedialog
from CTkMenuBar import CTkTitleMenu

def click_button_open():
    file_name = filedialog.askopenfilename()
    with open(file_name, 'r') as file:
        content = file.read()
        content.replace('\n\n', '\n')
        text_box.insert('end', content)
    file_opened.append(file_name)

def click_button_save():
    text = text_box.get('0.0', 'end')
    text = text.replace('\n\n', '\n')
    print(text)
    file_name_copy = ''.join(file_opened)
    print(file_name_copy)

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
right_frame = ctk.CTkFrame(master=app, fg_color='gray', corner_radius=10)
right_frame.pack(side='right',fill='both', expand=True, padx=5, pady=5)
    # content of right frame
text_box = ctk.CTkTextbox(master=right_frame, font=my_font, corner_radius=6)
text_box.pack(side='top', fill='both', expand=True, padx=5, pady=5)
#-------------------------------right side of screen-------------------------------#


#-------------------------------left side of screen--------------------------------#
left_frame = ctk.CTkFrame(master=app, fg_color='gray', corner_radius=10)
left_frame.pack(side='top', fill='both', expand=True, padx=5, pady=5)
    #content of left side

#-------------------------------left side of screen--------------------------------#

#------------------------------------menu bar--------------------------------------#
menu_bar = CTkTitleMenu(master=app)
text = text_box.get('0.0', 'end')
menu_bar.add_cascade('Open', command=click_button_open)
menu_bar.add_cascade('Save', command=click_button_save)
menu_bar.add_cascade('Help', command=click_button_help)
#------------------------------------menu bar--------------------------------------#

app.mainloop()
