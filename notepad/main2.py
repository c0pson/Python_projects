import customtkinter as ctk

def text_field(root):
    text_box = ctk.CTkTextbox(master=root, width=800, height=400, corner_radius=0)
    text_box.grid(row=0,column=0, sticky='w')

def button():
    ...

def main():
    app = ctk.CTk()
    app.geometry('1280x740')
    # code here
    text_field(app)
    app.mainloop()

if __name__ == "__main__":
    main()
