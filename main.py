import sys

def sort_string(text, MAX_NUM, start):
    CNT = start
    end = -1
    while (CNT != MAX_NUM):
        if text[CNT] == '@':
            temp = text.find(':', CNT, MAX_NUM - 1)
            if temp < (MAX_NUM - 1) and temp != -1:
                CNT = temp + 1
            else:
                print('Невозможно разделить строку')
                quit()
        if text[CNT] == ' ':
            end = CNT
            if CNT + 1 < MAX_NUM:
                CNT += 1
    if end == -1:
        print('Невозможно разделить строку')
        quit()
    print_string(end,MAX_NUM, text, start)

def print_string(end, MAX_NUM, text, start):
    FINAL_STR = text[start:end]
    print(FINAL_STR)
    print('\n')
    start = end + 1
    sort_string(text, MAX_NUM, start)

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
    MAX_NUM = sys.argv[4]

    file = open(sys.argv[2])
    text = file.read()
    start = 0
    # print(text)
    sort_string(text, MAX_NUM, start)

if __name__=='__main__':
    main(sys.argv)