import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PhotoViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Click the button to open a photo.")
        self.label.pack(pady=10)

        # Button to open photo
        self.button = tk.Button(self.root, text="Open Photo", command=self.open_photo)
        self.button.pack(pady=10)

    def open_photo(self):
        # Open file dialog to select an image
        filename = filedialog.askopenfilename()

        # Check if a file was selected
        if filename:
            # Open the image using PIL
            image = Image.open(filename)

            # Resize the image if needed
            max_size = (300, 300)
            image.thumbnail(max_size)

            # Convert PIL Image to Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(image)

            # Update the label's image
            self.label.config(image=tk_image)
            self.label.image = tk_image  # Keep a reference to prevent garbage collection

def main():
    root = tk.Tk()
    app = PhotoViewerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
