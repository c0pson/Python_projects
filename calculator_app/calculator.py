import customtkinter as ctk

def key_num_handle(number, input_text):
    input_text.insert('end', number)
    input_text.xview_moveto(len(input_text.get()))

def create_button(numbers_frame, buttons, num, input_text, font_x21):
    num_button = ctk.CTkButton(master=numbers_frame, text=f'{num+1}', font= font_x21, width=80, height=80,
                                command=lambda: key_num_handle(num_button.cget('text'), input_text))
    num_button.pack(side='left', fill='both', padx=5, pady=5)
    buttons.append(num_button)

def negate(input_text):
    if '−' in input_text.get():
        input_text.delete(0, 1)
    else:
        input_text.insert('0', '−')

def make_float(input_text):
    if '.' not in input_text.get() and input_text.get():
        input_text.insert('end', '.')

def delete_last_digit(input_text):
    input_text.delete(len(input_text.get())-1, 'end')

def handle_c(input_text, history_list, operation):
    input_text.delete('0', 'end')
    history_list.clear()
    operation[0] = ''

def handle_ce(input_text):
    input_text.delete('0', 'end')

def handle_div_operator(input_text, history_list, operation):
    if not input_text.get():
        return
    if len(history_list) == 2:
        history_list.clear()
    numbers = input_text.get().replace('−', '-')
    history_list.append(numbers)
    input_text.delete('0', 'end')
    print(history_list)
    operation[0] = '/'
    print(operation)

def handle_mul_operator(input_text, history_list, operation):
    if not input_text.get():
        return
    if len(history_list) == 2:
        history_list.clear()
    numbers = input_text.get().replace('−', '-')
    history_list.append(numbers)
    input_text.delete('0', 'end')
    print(history_list)
    operation[0] = 'x'
    print(operation)

def handle_minus_operator(input_text, history_list, operation):
    if not input_text.get():
        return
    if len(history_list) == 2:
        history_list.clear()
    numbers = input_text.get().replace('−', '-')
    history_list.append(numbers)
    input_text.delete('0', 'end')
    print(history_list)
    operation[0] = '-'
    print(operation)

def handle_plus_operator(input_text, history_list, operation):
    if not input_text.get():
        return
    if len(history_list) == 2:
        history_list.clear()
    numbers = input_text.get().replace('−', '-')
    history_list.append(numbers)
    input_text.delete('0', 'end')
    print(history_list)
    operation[0] = '+'
    print(operation)

def handle_solution_operator(input_text, history_list, operation):
    if not history_list[0]:
        return
    if input_text.get() != '':
        history_list.append(input_text.get())
    else:
        return
    history_list[0] = int(history_list[0])
    history_list[1] = int(history_list[1])
    if operation[0] == '-':
        solution = history_list[0] - history_list[1]
    if operation[0] == '+':
        solution = history_list[0] + history_list[1]
    if operation[0] == '/':
        solution = history_list[0] / history_list[1]
    if operation[0] == 'x':
        solution = history_list[0] * history_list[1]
    print(solution)
    input_text.delete('0', 'end')
    input_text.insert('0', str(solution))
    history_list[0] = str(solution)
    history_list.pop()
    input_text.xview_moveto(len(input_text.get()))

def numbers_keyboard(app, screen_frame):
    history_list = []
    operation = ['']
    font_x21 = ctk.CTkFont(family='JetBrains Mono', size=21)
    font_x42 = ctk.CTkFont(family='JetBrains Mono', size=42)
    input_text = ctk.CTkEntry(master=screen_frame, font=font_x42, justify='right', insertofftime=99999)
    input_text.pack(fill='x')
    frame = ctk.CTkFrame(master=app)
    frame.pack(side='left', fill='both', expand=True)
    frame_for_frame = ctk.CTkFrame(master=frame)
    frame_for_frame.pack(side='left', fill='both', expand=True)
    buttons = []
    numbers_frame = ctk.CTkFrame(master=frame_for_frame)
    numbers_frame.pack(side='top', expand=True)
    ce_button = ctk.CTkButton(master=numbers_frame, text='CE', font= font_x21, width=80, height=80,
                                command=lambda: handle_ce(input_text))
    ce_button.pack(side='left', fill='both', padx=5, pady=5)
    c_button = ctk.CTkButton(master=numbers_frame, text='C', font= font_x21, width=80, height=80,
                                command=lambda: handle_c(input_text, history_list, operation))
    c_button.pack(side='left', fill='both', padx=5, pady=5)
    delete_button = ctk.CTkButton(master=numbers_frame, text='⟵', width=80, height=80,
                                    command=lambda: delete_last_digit(input_text), font=font_x21)
    delete_button.pack(side='top', padx=5, pady=5)
    for _ in range(9):
        if _ % 3 == 0:
            numbers_frame = ctk.CTkFrame(master=frame_for_frame)
            numbers_frame.pack(side='top', expand=True)
        create_button(numbers_frame, buttons, _, input_text, font_x21)
    numbers_frame = ctk.CTkFrame(master=frame_for_frame)
    numbers_frame.pack(side='left', expand=True)
    plus_minus_button = ctk.CTkButton(master=numbers_frame, text='+\\-', width=80, height=80,
                                        command=lambda: negate(input_text), font=font_x21)
    plus_minus_button.pack(side='left', fill='both', padx=5, pady=5)
    create_button(numbers_frame, buttons, -1, input_text, font_x21)
    dot_button = ctk.CTkButton(master=numbers_frame, text='.', width=80, height=80,
                                command=lambda: make_float(input_text), font=font_x21)
    dot_button.pack(side='left', fill='both', padx=5, pady=5)
    right_frame = ctk.CTkFrame(master=frame)
    right_frame.pack(side='right', expand=True, fill='both')
    div_button = ctk.CTkButton(master=right_frame, text='/', width=80, height=80,
                                command=lambda: handle_div_operator(input_text, history_list, operation), font=font_x21)
    div_button.pack(side='top', pady=5, padx=5)
    mul_button = ctk.CTkButton(master=right_frame, text='x', width=80, height=80,
                                command=lambda: handle_mul_operator(input_text, history_list, operation), font=font_x21)
    mul_button.pack(side='top', pady=5, padx=5)
    minus_button = ctk.CTkButton(master=right_frame, text='-', width=80, height=80,
                                command=lambda: handle_minus_operator(input_text, history_list, operation), font=font_x21)
    minus_button.pack(side='top', pady=5, padx=5)
    plus_button = ctk.CTkButton(master=right_frame, text='+', width=80, height=80, 
                                command=lambda: handle_plus_operator(input_text, history_list, operation), font=font_x21)
    plus_button.pack(side='top', pady=5, padx=5)
    sol_button = ctk.CTkButton(master=right_frame, text='=', width=80, height=80, 
                                command=lambda: handle_solution_operator(input_text, history_list, operation), font=font_x21)
    sol_button.pack(side='top', pady=5, padx=5)

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
