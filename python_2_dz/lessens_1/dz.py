"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. 
    Первый и второй множитель должны задаваться в виде аргументов функции.
    Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
    После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
    Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""
def dz_1(arg_x, arg_y):
    tabl = [ [ str(x*y) for x in range(1, arg_x+1) ] for y in range(1, arg_y+1) ]
    [print( "\t".join(elem) ) for elem in tabl]

# dz_1(9,9) 

"""
2. Дополнить следующую функцию недостающим кодом:
    def print_directory_contents(sPath):
    '
        Функция принимает имя каталога и распечатывает его содержимое
        в виде «путь и имя файла», а также любые другие
        файлы во вложенных каталогах.
        Эта функция подобна os.walk. Использовать функцию os.walk
        нельзя. Данная задача показывает ваше умение работать с 
        вложенными структурами.
    '
"""
import os


def print_directory_contents(sPath):
    dir_path = os.path.abspath(sPath)
    dirs_list = [0]
    for el in os.listdir(sPath):
        if os.path.isdir(el):
            dirs_list.append(os.path.basename(el))

    
    for dirs in dirs_list:
        if dirs == 0:
            dir_path = os.path.abspath(sPath)
        else:
            dir_path = os.path.join(sPath, dirs)
            os.chdir(dir_path)

        for el in os.listdir(dir_path):
            if os.path.isfile(el):
                print(f'> путь - {dir_path}\n> имя - {os.path.basename(el)}')
        print()

# print_directory_contents(os.getcwd())

"""
3. Разработать генератор случайных чисел.
    В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
    Заполнить этими данными список и словарь.
    Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
    Вывести содержимое созданных списка и словаря.
"""
import random


def dz_3(start_int, end_int):
    gen_rand_list = [random.randint(start_int, end_int) for _ in range(12)]

    rand_list = [el for el in gen_rand_list]
    rand_dict = {f'elem_{idx}': el for idx, el in enumerate(gen_rand_list)}

    print(rand_list)
    print(rand_dict)

# dz_3(3,20)

"""
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
    Клиент банка делает депозит на определенный срок.
    В зависимости от суммы и срока вклада определяется процентная ставка: 
        1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
        10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
        100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
    Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
    Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
    Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
    В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной процентной ставке.
    Функция возвращает сумму вклада на конец срока.
5. Усовершенствовать программу «Банковский депозит».
    Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
    Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
    Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
    Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
    Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
        а главная функция — общую сумму по вкладу на конец периода.
"""
def dz_4_and_5(user_sum, user_time, user_repl_sum):
    product_1 = {'begin_sum':1000, 'end_sum':10000, '6':5, '12':6, '24':5}
    product_2 = {'begin_sum':10000, 'end_sum':100000, '6':6, '12':7, '24':6.5}
    product_3 = {'begin_sum':100000, 'end_sum':1000000, '6':7, '12':8, '24':7.5}

    # подсчет суммы пополнений
    def deposit_replenishment(user_repl_sum, prod_prosent):
        user_repl_sum = (user_repl_sum / 100 * prod_prosent[str(user_time)] + user_repl_sum) * (user_time - 2)
        return user_repl_sum
    
    # подсчет суммы без пополнений
    def calculation_sum_deposit(prod_prosent):
        product_user_sum = user_sum / 100 * prod_prosent[str(user_time)] + user_sum
        return product_user_sum

    if product_1['begin_sum'] < user_sum <= product_1['end_sum']:
        all_sum = calculation_sum_deposit(product_1) + deposit_replenishment(user_repl_sum, product_1)
    elif product_2['begin_sum'] < user_sum <= product_2['end_sum']:
        all_sum = calculation_sum_deposit(product_2) + deposit_replenishment(user_repl_sum, product_2)
    elif product_3['begin_sum'] < user_sum <= product_3['end_sum']:
        all_sum = calculation_sum_deposit(product_3) + deposit_replenishment(user_repl_sum, product_3)
    else:
        print('error')

    print(f"Cумму вклада на конец срока = { all_sum }")


# dz_4_and_5(10000, 12, 1000)
