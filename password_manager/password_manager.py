import customtkinter as ctk

def login(app, password_box):
    password = password_box.get()
    secret_password = 'secret' # I will add some hashing or something like this
    if secret_password == password:
        print('Successful login')

def main():
    app = ctk.CTk()
    app.title('Password manager')
    app.geometry('1080x720')
    my_font = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)

    login_frame = ctk.CTkFrame(master=app, corner_radius=10)
    login_frame.pack(side='top', expand=True, padx=10, pady=10)

    password_label = ctk.CTkLabel(master=login_frame, fg_color='transparent', bg_color='transparent', text='Password', font=my_font)
    password_label.pack(padx=5, pady=5)

    password_box = ctk.CTkEntry(master=login_frame, width=270, height=60, corner_radius=10, font=my_font, show='*')
    password_box.pack(padx=15, pady=0)

    login_button = ctk.CTkButton(master=login_frame, width=120, height=50, corner_radius=10, text='Login', font=my_font, command=lambda: login(app, password_box))
    login_button.pack(padx=10, pady=15)

    app.mainloop()

if __name__ == "__main__":
    main()
