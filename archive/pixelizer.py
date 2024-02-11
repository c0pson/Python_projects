from tkinter import Tk, filedialog
from PIL import Image
import re

root = Tk(className = "Pixelizer")
root.geometry("1280x720")

def openImage():
    filename = filedialog.askopenfilename()
    print(filename)
    match = re.search(r'(\.[^\.]+)$', filename)
    if match:
        new_filename = str(filename.replace(match.group(1), "_new" + match.group(1)))
        print(new_filename)
    else:
        print("No \".\" in path")

    for i in range(len(filename)):
        if "." in filename[i]:
            filename[i]

    img = Image.open(filename)
    imgSmall = img.resize((128, 128), resample = Image.Resampling.BILINEAR)
    result = imgSmall.resize(img.size, Image.Resampling.NEAREST)
    result.save(new_filename)
    return filename

openImage()
root.mainloop()
