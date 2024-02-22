import customtkinter as ctk
from customtkinter import filedialog

class open_folder():
    def __init__(self):
        self.filedialog = filedialog.askdirectory()
        print(self.filedialog)

class Frame_For_Button(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button = ctk.CTkButton(master=self, width=40, height=40, command=open_folder, bg_color='transparent', hover=False)
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

        self.button_frame = Frame_For_Button(master=self)
        self.button_frame.grid(row=0, column=0, sticky='w')

        self.text_frame = Frame_For_Text(master=self)
        self.text_frame.grid(row=0, column=0, sticky='e')

if __name__ == "__main__":
    app = App()
    app.mainloop()
