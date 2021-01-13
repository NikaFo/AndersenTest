number = input('Введите число: \n')

try:
    if int(number) > 7:
        print('Привет')
except ValueError:
    print('Допустимо вводить только числа')
