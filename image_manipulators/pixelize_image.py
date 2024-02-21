from string import ascii_letters
from PIL import Image
import random
import os

def print_error(message):
    print("\033[91mError: {}\033[0m".format(message))

def print_success(text):
    print("\033[92m{}\033[0m".format(text))

def check_extension(file, allowed_formats):
    for format in allowed_formats:
        if file.endswith(format):
            return True
        
def get_extension(file, allowed_formats):
    counter = 0
    for format in allowed_formats:
        if file.endswith(format):
            return allowed_formats[counter]
        counter += 1

def pixelize(resize_ratio, orginal_file):
    img = Image.open(orginal_file)
    small_image = img.resize((resize_ratio, resize_ratio), resample = Image.Resampling.BILINEAR)
    result = small_image.resize(img.size, Image.Resampling.NEAREST)
    return result

def check_overwrite(file, new_file):
    directory = os.path.dirname(file) + "\\"
    file_path = os.path.join(directory, new_file)
    return os.path.exists(file_path)

def save_image(result, file, allowed_formats):
    directory = os.path.dirname(file) + "\\"
    name = input("Enter name for a new file: ")
    format = get_extension(file, allowed_formats)
    if not name:
        name = ''.join(random.choice(ascii_letters) for _ in range(16))
        print(f"File saved to {directory}{name}{format}")
    save_path = os.path.join(directory, f"{name}{format}")
    name += str(format)
    if check_overwrite(file, name):
        overwrite = input(f"Do you want to overwrite existing file {save_path}? (press y to confirm): ")
        if overwrite != "y":
            print_error("Your file cant be saved!")
            exit()
    result.save(save_path)
    return save_path

def chose_ratio():
    ratios_list = 16, 32, 64, 128, 256, 512
    try:
        user_input = int(input((f"Choose ratio of pixelization - suggested ratios - {ratios_list}: ")))
        return user_input
    except ValueError:
        print_error("Invalid value! - should be integer.")
        exit()

def main():
    resize_ratio = chose_ratio()
    allowed_formats = [".jpg", ".png", ".jpeg"]
    filename = input("Drag your photo to the terminal window: ")
    if check_extension(filename, allowed_formats):
        result = pixelize(resize_ratio, filename)
    else:
        print_error("Invalid format!")
        exit()
    path = save_image(result, filename, allowed_formats)
    os.system(path)
    print_success("Program executed correctly!")

if __name__ == "__main__":
    main()

