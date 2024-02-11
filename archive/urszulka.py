import random

list_of_students_to_fuck_up = ["Szymon", "Jeremi", "Piotr C", "Piotr K"]

def round_quart(val, reso):
    return round (val/reso) * reso

def print_Urszulka():
    for i in range(len(list_of_students_to_fuck_up)):
        print(f'{list_of_students_to_fuck_up[i]}:')
        for _ in range(5):
            print(round_quart(round(random.uniform(0.0, 4.0), 2), 0.25))

if __name__ == "__main__":
    print_Urszulka()
