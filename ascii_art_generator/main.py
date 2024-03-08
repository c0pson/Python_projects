from PIL import Image
import os

def get_luminace(image_path: str, details: int) -> list[int]:
    image = Image.open(image_path)
    width, height = image.size
    image_lum_data = []
    for y in range(0, height, 2 * details):
        for x in range(0, width, details):
            r, g, b = image.getpixel((x, y))
            luminance = 0.299 * r + 0.587 * g + 0.114 * b
            image_lum_data.append(round(luminance, 2))
        image_lum_data.append(9999)
    return image_lum_data

def image_path(image_name: str) -> str:
    working_dir = os.path.dirname(__file__)
    image_path = os.path.join(working_dir, image_name)
    return image_path

def get_details_info() -> int:
    details_level = int(input('Enter details level from 1 to 100: '))
    details_level = int(101 - details_level)
    return details_level

def print_ascii_art(luminance_data: list[int]) -> None:
    characters: list[str] = ['#', '$', '&', '%', '!', '+', '"', '=', '\'', '_', '-', ',', '.']
    line_list: list[str] = []
    for item in luminance_data:
        if item != 9999:
            index = int(item // 13)
            line_list.append(characters[int(item // 15)] if index < 13 else characters[12])
        else:
            print(''.join(line_list))
            line_list = []

def main() -> None:
    path = image_path('aigeneratedpotion.png')
    details = get_details_info()
    luminance_data: list[int] = get_luminace(path, details)
    os.system('cls')
    print_ascii_art(luminance_data)

if __name__ == "__main__":
    main()
