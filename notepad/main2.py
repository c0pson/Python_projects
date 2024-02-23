import customtkinter as ctk
from CTkMenuBar import CTkTitleMenu

def click_button():
    print('Hello Menu')

def main():
    app = ctk.CTk()
    app.geometry('1280x780')
    app.title('Note')
    # menu bar
    menu_bar = CTkTitleMenu(master=app)
    menu_bar.add_cascade('File', command=click_button)
    # left side of screen
    left_frame = ctk.CTkFrame(master=app, fg_color='light yellow', corner_radius=5)
    left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    # right side of screen - flexible
    right_frame = ctk.CTkFrame(master=app, fg_color='dark gray', corner_radius=5)
    right_frame.pack(side='right',fill='both', expand=True, padx=5, pady=5)
    # main loop
    app.mainloop()

if __name__ == "__main__":
    main()
