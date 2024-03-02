import customtkinter

app = customtkinter.CTk()
app.geometry('400x400')
list = ['']
flag = [0]

def options(frame):
    button_1 = customtkinter.CTkButton(master=frame, command=lambda: print('test'), text='', width=96)
    button_1.pack(side='top', padx=2, pady=2)
    button_2 = customtkinter.CTkButton(master=frame, command=lambda: print('test'), text='', width=96)
    button_2.pack(side='top', padx=2, pady=2)
    button_3 = customtkinter.CTkButton(master=frame, command=lambda: print('test'), text='', width=96)
    button_3.pack(side='top', padx=2, pady=2)
    button_4 = customtkinter.CTkButton(master=frame, command=lambda: print('test'), text='', width=96)
    button_4.pack(side='top', padx=2, pady=2)

def test(event, flag, list, app):
    label = customtkinter.CTkFrame(app, width=100, height=100)
    if flag[0] == 0:
        print(app.winfo_width())
        if event.x+150 > app.winfo_width():
            label.place(x=event.x-101, y=event.y-1)
        else:
            label.place(x=event.x+1, y=event.y+1)
        options(label)
        list[0] = label
        flag[0] = 1
    else:
        list[0].destroy()
        list[0] = ''
        flag[0] = 0

def idk(event, label):
    if label[0] != '':
        label[0].destroy()
        label[0] = ''
        flag[0] = 0

app.bind("<Button-1>", lambda event: idk(event, list))
app.bind("<Button-3>", lambda event: test(event, flag, list, app))

app.mainloop()

