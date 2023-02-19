import sys

def sort_string(text, MAX_INDEX, start, INDEX_INC):
    INDEX_INC = MAX_INDEX
    CNT = start
    end = -1
    LEN = len(text)
    if CNT == LEN + 1:
        print('Строки разделены')
        quit()
    if LEN - CNT < INDEX_INC:
            print_string(LEN, MAX_INDEX, text, start,  INDEX_INC)
    while ((CNT != MAX_INDEX) and CNT != LEN):
        if text[CNT] == '@':
            temp = text.find(':', CNT, MAX_INDEX - 1)
            if temp < (MAX_INDEX - 1) and temp != -1:
                CNT = temp + 1
            else:
                print('Невозможно разделить следующую строку')
                quit()
        if text[CNT] == ' ':
            end = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1

        elif text[CNT] == '\n':
            end = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1
        else:
            CNT += 1
    if end == -1:
        print('Невозможно разделить строку')
        quit()
    print_string(end, MAX_INDEX, text, start, INDEX_INC)

def print_string(end, MAX_INDEX, text, start, INDEX_INC):
    FINAL_STR = text[start:end]
    print(FINAL_STR)
    print('\n')
    start = end + 1
    MAX_INDEX += INDEX_INC
    sort_string(text, MAX_INDEX, start, INDEX_INC)

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
    text = file.read()
    start = 0
    # print(text)
    sort_string(text, MAX_INDEX, start, INDEX_INC)

if __name__=='__main__':
    main(sys.argv)
