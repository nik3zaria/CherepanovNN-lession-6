import sys


def adding_prices(new_entry):
    with open('bakery.cvs', 'a', encoding='utf-8') as file:
        file.write(f'{new_entry}\n')


if __name__ == '__main__':
    _script_name, new_price = sys.argv
    adding_prices(new_price)



