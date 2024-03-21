import customtkinter as ctk

def reset(event, old_x, old_y):
    old_x[0] = None
    old_y[0] = None

def print_dot(event, canvas):
    canvas.create_oval(event.x-1, event.y-1, event.x+1, event.y+1, width=3, fill='black')

def paint_line(event, canvas, old_x, old_y):
    if old_x[0] and old_y[0]:
        canvas.create_line(old_x[0], old_y[0], event.x, event.y, width=6, fill='black', capstyle=ctk.ROUND, smooth=ctk.TRUE, splinesteps=1)
    old_x[0] = event.x
    old_y[0] = event.y

def main():
    app = ctk.CTk()
    old_x = [None]
    old_y = [None]
    canvas = ctk.CTkCanvas(app)
    canvas.pack(fill='both', expand=True)

    app.bind('<B1-Motion>', lambda event: paint_line(event, canvas, old_x, old_y))
    app.bind('<ButtonRelease-1>', lambda event: reset(event, old_x, old_y))
    app.bind('<Button-1>', lambda event: print_dot(event, canvas))

    app.mainloop()

if __name__ == "__main__":
    main()
