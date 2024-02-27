import customtkinter as ctk

def login(app, password_box):
    password = password_box.get()
    secret_password = 'secret' # I will add some hashing or something like this
    if secret_password == password:
        for child in app.winfo_children():
            child.destroy()

def login_page(app, my_font):
    login_frame = ctk.CTkFrame(master=app, corner_radius=10)
    login_frame.pack(side='top', expand=True, padx=10, pady=10)

    password_label = ctk.CTkLabel(master=login_frame, fg_color='transparent', bg_color='transparent', text='Password', font=my_font)
    password_label.pack(padx=5, pady=5)

    password_box = ctk.CTkEntry(master=login_frame, width=270, height=60, corner_radius=10, font=my_font, show='*')
    password_box.pack(padx=15, pady=0)

    login_button = ctk.CTkButton(master=login_frame, width=120, height=50, corner_radius=10, text='Login', font=my_font, command=lambda: login(app, password_box))
    login_button.pack(padx=10, pady=15)

def main():
    app = ctk.CTk()
    app.title('Password manager')
    app.geometry('1080x720')
    my_font_x32 = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)
    my_font_x21 = ctk.CTkFont(family='Hack Nerd Font Propo', size=21)

    # login_page(app, my_font_x32)
    button_index = []
    button_index_2 = []
    current_label = ['']

    def button_clicked(event, label):
        print(int(button_index_2.index(label.cget('text'))))
        if current_label[0] != '':
            button_index[int(button_index_2.index(current_label[0]))].configure(fg_color='transparent')
        button_index[int(button_index_2.index(label.cget('text')))].configure(fg_color='gray')
        current_label[0] = label.cget('text')

    def add():
        pop_up = ctk.CTkInputDialog(text='Provide title for label', title='Test')
        label_name = str(pop_up.get_input())
        new_label=ctk.CTkLabel(master=password_index_frame, text=label_name, font=my_font_x21, corner_radius=10)
        new_label.bind(sequence='<Button-1>', command=lambda event: button_clicked(event, new_label))
        new_label.pack(side='top', fill='x')
        button_index.append(new_label)
        button_index_2.append(label_name)

    def remove():
        if current_label[0] != '':
            button_index[int(button_index_2.index(current_label[0]))].destroy()
            button_index.pop(int(button_index_2.index(current_label[0])))
            button_index_2.pop(int(button_index_2.index(current_label[0])))
        current_label[0] = ''

    main_frame = ctk.CTkFrame(master=app, corner_radius=10)
    main_frame.pack(side='top', expand=True, fill='both', padx=5, pady=5)

    index_frame = ctk.CTkFrame(master=main_frame, corner_radius=7)
    index_frame.pack(side='left', fill='y', padx=5, pady=5)

    password_index_frame = ctk.CTkScrollableFrame(master=index_frame, corner_radius=4)
    password_index_frame.pack(side='top', expand=True, fill='both', padx=3, pady=3)

    buttons_index_frame = ctk.CTkFrame(master=index_frame, corner_radius=4)
    buttons_index_frame.pack(side='bottom', fill='x', padx=3, pady=3)

    add_button = ctk.CTkButton(master=buttons_index_frame, text='Add', font=my_font_x32, command=add)
    add_button.pack(side='top', fill='both', padx=15, pady=5)

    remove_button = ctk.CTkButton(master=buttons_index_frame, text='Remove', font=my_font_x32, command=remove)
    remove_button.pack(side='top', fill='both', padx=15, pady=5)

    app.mainloop()

if __name__ == "__main__":
    main()
