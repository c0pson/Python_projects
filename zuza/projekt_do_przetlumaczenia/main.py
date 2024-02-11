def check_file(input_file, decision_file, output_file):
    valid_operators = ['<', '<=', '=<', '>', '>=', '=>']

    # decision file

    try:
        with open(decision_file, 'r') as dec:
            val = int(dec.readline())
            for line_num, line in enumerate(dec, start = 1):
                words = line.split()
                if (len(words) != 4):
                    print('File error dec')
                    print_instruction()
                    exit()
                if words[1] not in valid_operators:
                    print('test')
                    print_instruction()
                    exit()

            dec.close()
    except FileNotFoundError:
        print(f'Unable to open the following path: {decision_file}')
        print_instruction()
        exit()

    # input file

    try:
        with open(input_file, 'r') as inp:
            leng = int(inp.readline())
            line_count = sum(1 for line in inp)
    # sprawdzasz czy podana długość pliku jest prawidłowa
            if leng != line_count:
                print('Incorrect file lenght provided')
                exit()
    # sprawdzasz czy podana ilość danych dla jednej linijki jest prawidłowa
            for line_num, line in enumerate(inp, start = 1):
                words = line.split()
                if len(words) != val:
                    print('File error')
                    exit()
        inp.close() # tu sprawdzasz czy da się otworzyć plik a potem go zamykasz
    except FileNotFoundError:
        print(f'Unable to open the following path: {input_file}')
        print_instruction()
        exit() # jak nie da się to wyrzuca błąd i pisze instrukcję - dalej analogicnzie to samo, pewnie da się to skrócić ale nie mam czasu się bawić aż tak

    # output file

    try:
        with open(output_file) as out:
            out.close()
    except FileNotFoundError:
        print(f'Output file will be saved to non existing directory: {output_file}')

def print_instruction():
    print('Tutaj dajesz sobie instrukcje')
    # to jest ze względów estetyznych tylko i wyłącznie bo to będzie długie i skopiowane to trzy razy będzie nieczytelne

def read_parameters():
    decision_file = input('Provide path to decision file: ')
    input_file = input('Provide path to input file: ')
    output_file = input('Proide path to output file: ')

    # to ma być inaczej ale mi się teraz nie chce + plus chat to ładnie robi w c++

    return decision_file, input_file, output_file

#========================================================================================================

def open_decision_file(decision_file):
    # setup matrixes for every atribute from file - czemu po angielsku to pisałem XD
    vector_of_dec_file = [] # tu masz plik ale w matrycy
    atribute = []
    sign = []
    value = []
    discipline = [] #w c++ wektory

    with open(decision_file, 'r') as decision_data:
        amount_of_decision_args = int(decision_data.readline(1))
        for line in decision_data:
            words = line.split()
            vector_of_dec_file.append(words)
        vector_of_dec_file = [sublist for sublist in vector_of_dec_file if sublist]

    for i in range(amount_of_decision_args):
        atribute.append(vector_of_dec_file[i][0])
        sign.append(vector_of_dec_file[i][1])
        value.append(vector_of_dec_file[i][2])
        discipline.append(vector_of_dec_file[i][3])

    return atribute, sign, value, discipline, amount_of_decision_args

def make_decision(amount_of_decision_args, discipline ,atribute, value, sign, input_file):
    vector_of_inp_file = []
    output = []
    with open(input_file, 'r') as input_file:
        lenght_of_input_file = int(input_file.readline().strip())
        for line in input_file:
            words = line.split()
            vector_of_inp_file.append(words)
        vector_of_inp_file = [sublist for sublist in vector_of_inp_file if sublist]

    for i in range(amount_of_decision_args):
        output.append(f'{discipline[i]}:')
        if sign[i] == '>':
            for j in range(lenght_of_input_file):
                if vector_of_inp_file[j][i] > value[i]:
                    formatted_data = ', '.join(vector_of_inp_file[j])
                    output.append(f'{formatted_data}: {atribute[i]} {sign[i]} {value[i]}')
                else:
                    continue
        elif sign[i] == '<':
            for j in range(lenght_of_input_file):
                if vector_of_inp_file[j][i] < value[i]:
                    formatted_data = ', '.join(vector_of_inp_file[j])
                    output.append(f'{formatted_data}: {atribute[i]} {sign[i]} {value[i]}')
                else:
                    continue
        elif sign[i] == '=<' or sign[i] == '<=':
            for j in range(lenght_of_input_file):
                if vector_of_inp_file[j][i] <= value[i]:
                    formatted_data = ', '.join(vector_of_inp_file[j])
                    output.append(f'{formatted_data}: {atribute[i]} {sign[i]} {value[i]}')
                else:
                    continue
        elif sign[i] == '=>' or sign[i] == '>=':
            for j in range(lenght_of_input_file):
                if vector_of_inp_file[j][i] >= value[i]:
                    formatted_data = ', '.join(vector_of_inp_file[j])
                    output.append(f'{formatted_data}: {atribute[i]} {sign[i]} {value[i]}')
                else:
                    continue
    return output

#========================================================================================================

def save_to_file(output, output_file):
    with open(output_file, 'w') as out:
        out.write('Results: \n')
        for line in output:
            out.write(f'{line}\n')

def main():
    decision_file, input_file, output_file = read_parameters()
    print(f'{decision_file} | {input_file} | {output_file}')
    # input_file = 'zuza\\projekt_do_przetlumaczenia\\input.txt'
    # decision_file = 'zuza\\projekt_do_przetlumaczenia\\decision.txt'
    # output_file = 'zuza\\projekt_do_przetlumaczenia\\output.txt'

    input_file = 'input.txt'
    decision_file = 'decision.txt'
    output_file = 'output.txt'

    check_file(input_file, decision_file, output_file)
    atribute, sign, value, discipline, amount_of_decision_args = open_decision_file(decision_file)
    output = make_decision(amount_of_decision_args, discipline ,atribute, value, sign, input_file)
    save_to_file(output, output_file)

if __name__ == '__main__':
    main()
