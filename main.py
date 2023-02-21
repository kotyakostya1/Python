import sys

def sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC):
    CNT = START_INDEX
    END_INDEX = -1
    TEXT_LENGTH = len(TEXT)
    if CNT == TEXT_LENGTH + 1:
        print('Строки разделены')
        quit()
    if TEXT_LENGTH - CNT < INDEX_INC:
            print_string(TEXT_LENGTH, MAX_INDEX, TEXT, START_INDEX, INDEX_INC)
    while ((CNT != MAX_INDEX) and CNT != TEXT_LENGTH):
        if TEXT[CNT] == '@':
            temp = TEXT.find(':', CNT, MAX_INDEX - 1)
            if temp < (MAX_INDEX - 1) and temp != -1:
                CNT = temp + 1
            elif temp == -1:
                CNT += 1
            else:
                print('Невозможно разделить следующую строку')
                quit()
        if TEXT[CNT] == ' ':
            END_INDEX = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1

        elif TEXT[CNT] == '\n':
            END_INDEX = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1
        else:
            CNT += 1
    if END_INDEX == -1:
        print('Невозможно разделить строку')
        quit()
    print_string(END_INDEX, MAX_INDEX, TEXT, START_INDEX, INDEX_INC)

def print_string(END_INDEX, MAX_INDEX, TEXT, START_INDEX, INDEX_INC):
    FINAL_STR = TEXT[START_INDEX:END_INDEX]
    print(FINAL_STR)
    print('\n')
    START_INDEX = END_INDEX + 1
    MAX_INDEX += INDEX_INC
    sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC)

def main(args: list[str]):
    # input()
    # Нужно сделать какой-то while чтобы постоянно спрашивал -f

    if len(sys.argv) == 1:
         print('Введите -f путь к файлу')
    else:
         PARAM_NAME = sys.argv[1]
    if PARAM_NAME == '-f':
         FILE_PATH = sys.argv[2]
    else:
         print(f'Неизвесный параметр {PARAM_NAME}')

    # Как спросить про -n?
    MAX_INDEX = int(sys.argv[4]) + 1
    INDEX_INC = MAX_INDEX

    file = open(sys.argv[2])
    TEXT = file.read()
    START_INDEX = 0
    # print(text)
    sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC)

if __name__=='__main__':
    main(sys.argv)
