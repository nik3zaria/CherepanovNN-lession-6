import sys


line_length = 20


def replacing_a_line(line_from, new_rec):
    line_from -= 1
    with open('bakery.cvs', 'r+', encoding='utf-8') as file:
        file.seek(line_from * line_length)
        if not file.readline():
            print('Запись не найдена')
            return
        file.seek(line_from * line_length)
        file.write(new_rec)



