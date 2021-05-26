import math
import sys


line_length = 20


def sales_withdrawal(start_of_sales_withdrawal=1, show_to_line=math.inf):
    with open('bakery.cvs', 'r', encoding='utf-8') as file:
        old_sales = file.read()
        for sales_old in old_sales:
            if len(sales_old) < line_length:
                sales_line = line_length - len(sales_old)
                sales = sales_old.zfill(sales_line)
    new_sales = sales_old.replace(sales_old, sales)

    with open('bakery.cvs', 'w', encoding='utf-8') as file:
        file.write(new_sales)
        file.close()
    if start_of_sales_withdrawal < 2:
        start_position_sales = 0
    else:
        start_position_sales = (start_of_sales_withdrawal - 1) * line_length

    end_position_sales = show_to_line * line_length

    with open('bakery.cvs', 'r', encoding='utf-8') as file:
        file.seek(start_position_sales)
        line = file.readline()
        while line:
            print(line.strip())
            if end_position_sales < file.tell():
                break
            line = file.readline()


if __name__ == '__main__':
    argument = (int(arg) for arg in sys.argv[1:])
    sales_withdrawal(*argument)