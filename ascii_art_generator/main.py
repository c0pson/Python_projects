from PIL import Image
import os

def get_luminace(image_path: str, details: int) -> list[int]:
    image = Image.open(image_path)
    width, height = image.size
    image_lum_data = []
    for y in range(0, height, 2*details):
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

def input_info(ask: str) -> str:
    user_input = input(f'{ask}: ')
    return user_input

def show_path(user_input: str) -> None:
    if os.path.isabs(user_input) != '':
        dirname = os.path.dirname(__file__)
        print(f'Your file is saved in: {dirname}\\{user_input}')
    else:
        print(f'Your file is saved in: {user_input}')

def convert_to_int(user_input: str, ask: str) -> int:
    while isinstance(user_input, str):
        try:
            int(user_input)
            if 1 <= int(user_input) and int(user_input) <= 100:
                break
            else:
                input_info(ask)
        except ValueError as e:
            print(e)
            input_info(ask)
    return 101 - int(user_input)

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

def save_to_file(luminance_data: list[int], path_to_save: str) -> None:
    characters: list[str] = ['#', '$', '&', '%', '!', '+', '"', '=', '\'', '_', '-', '.', ' ']
    line_list: list[str] = []
    with open(path_to_save, 'w') as file:
        for item in luminance_data:
            if item != 9999:
                index = int(item // 13)
                line_list.append(characters[int(item // 15)] if index < 13 else characters[12])
            else:
                file.write(f'{''.join(line_list)}\n')
                line_list = []
    show_path(path_to_save)

def main() -> None:
    img_path = image_path(input_info('Enter path to image'))
    details = convert_to_int(input_info('Insert number from 1 to 100'), 'Insert number from 1 to 100')
    luminance_data: list[int] = get_luminace(img_path, details)
    os.system('cls')
    # print_ascii_art(luminance_data)
    save_path: str = input_info('Enter path where file will be saved')
    save_to_file(luminance_data, save_path)

if __name__ == "__main__":
    main()
