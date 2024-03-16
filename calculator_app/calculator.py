import customtkinter as ctk

def key_num_handle(number, input_text):
    input_text.insert('end', number)
    input_text.xview_moveto(len(input_text.get()))

def create_button(numbers_frame, buttons, num, input_text, font_x21):
    num_button = ctk.CTkButton(master=numbers_frame, text=f'{num+1}', font= font_x21, width=80, height=80,
                                command=lambda: key_num_handle(num_button.cget('text'), input_text))
    num_button.pack(side='left', fill='both')
    buttons.append(num_button)

def negate(input_text):
    if '−' in input_text.get():
        input_text.delete(0, 1)
    else:
        input_text.insert('0', '−')

def make_float(input_text):
    if '.' not in input_text.get() and input_text.get():
        input_text.insert('end', '.')

def numbers_keyboard(app, screen_frame):
    font_x21 = ctk.CTkFont(family='JetBrains Mono', size=21)
    font_x42 = ctk.CTkFont(family='JetBrains Mono', size=42)
    input_text = ctk.CTkEntry(master=screen_frame, font=font_x42, justify='right')
    input_text.pack(fill='x')
    frame = ctk.CTkFrame(master=app)
    frame.pack(side='left', fill='both', expand=True)
    buttons = []
    for _ in range(9):
        if _ % 3 == 0:
            numbers_frame = ctk.CTkFrame(master=frame)
            numbers_frame.pack(side='top', expand=True)
        create_button(numbers_frame, buttons, _, input_text, font_x21)
    numbers_frame = ctk.CTkFrame(master=frame)
    numbers_frame.pack(side='left', expand=True)
    plus_minus_button = ctk.CTkButton(master=numbers_frame, text='+\\-', width=80, height=80,
                                        command=lambda: negate(input_text), font=font_x21)
    plus_minus_button.pack(side='left', fill='both')
    create_button(numbers_frame, buttons, -1, input_text, font_x21)
    dot_button = ctk.CTkButton(master=numbers_frame, text='.', width=80, height=80,
                                command=lambda: make_float(input_text), font=font_x21)
    dot_button.pack(side='left', fill='both')

def operations(app):
    ...

def main():
    app = ctk.CTk()
    app.title('Calculator')
    bottom_frame = ctk.CTkFrame(master=app)
    bottom_frame.pack(side='bottom', fill='x', expand=True)
    screen_frame = ctk.CTkFrame(master=app)
    screen_frame.pack(side='top', fill='x', expand=True, anchor='n')
    numbers_keyboard(bottom_frame, screen_frame)
    app.mainloop()

if __name__ == "__main__":
    main()
