import customtkinter as ctk
from customtkinter import filedialog

class Open_Dialog():
    def __init__(self, choice):
        self.choice = choice
        print(choice)

class Open_Folder():
    def __init__(self):
        self.filedialog = filedialog.askdirectory()
        print(self.filedialog)

class Option_Menu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.menu_bar = ctk.CTkOptionMenu(master=self, width=40, height=10 ,values=["option 1", "option 2"], command=Open_Dialog)
        self.menu_bar.pack()

class Frame_For_Button(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button = ctk.CTkButton(master=self, width=40, height=40, command=Open_Folder, bg_color='transparent', hover=False)
        self.button.pack()

class Frame_For_Text(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.text_box = ctk.CTkTextbox(master=self, width=400, height=400, corner_radius=0)
        self.text_box.pack()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1080x720')
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.option_menu = Option_Menu(master=self)
        self.option_menu.grid(row=0, column=0, sticky='nw')

        self.button_frame = Frame_For_Button(master=self)
        self.button_frame.grid(row=1, column=0, sticky='nw')

        self.text_frame = Frame_For_Text(master=self)
        self.text_frame.grid(row=1, column=0, sticky='ne')

if __name__ == "__main__":
    app = App()
    # app.iconbitmap('path/to/icon.png')
    app.mainloop()
