from tkinter import Tk, filedialog
import tkinter
from PIL import Image, ImageTk
import os

def open_file(): 
    filename = filedialog.askopenfilename()
    check_if_correct_extension(filename)

def check_if_correct_extension(filename):
    while True:
        extensions_list = [".jpg", ".png", ".jpeg"]
        _, extension = os.path.splitext(str(filename))
        if extension.lower() in extensions_list:
            resize_image(filename)
        else:
            filename = open_file()

def open_image(image):
    img = ImageTk.PhotoImage(Image.open(image))
    return img

def resize_image(file):
    max_size = 600
    image = Image.open(file)
    width, height = image.size

    aspect_ratio = width / height

    if width > height:
        new_width = max_size
        new_height = int(max_size / aspect_ratio)
    else:
        new_height = max_size
        new_width = int(max_size * aspect_ratio)
    
    resized_image = image.resize((new_width, new_height), Image.BILINEAR)
    return ImageTk.PhotoImage(resized_image)

def save_file():
    pass

def button_click():
    print("Nigga")

def main():   
    root = Tk(className = "Pixelator",)
    root.geometry("1280x720")
    root.resizable(False, False)

    button = tkinter.Button(root, text="Open File", command=open_file)
    button.pack(side=tkinter.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
