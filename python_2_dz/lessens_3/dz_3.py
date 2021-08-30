"""
    1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. 
        При вызове функции в качестве аргумента должно передаваться имя файла с расширением. 
        В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import os

def dz_1(arg_path):
    name = os.path.basename(arg_path)
    print(name.split('.')[0])

# dz_1('/home/dqipb/lessens_3/dz_3.py')

"""
    2. Написать программу, которая запрашивает у пользователя ввод числа. 
        На введенное число она отвечает сообщением, целое оно или дробное. 
        Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. 
        Если они совпадают, программа должна возвращать значение True, иначе False.
"""
def dz_2(user_str):
    list_arg = user_str.split('.')
    print(f' дробное.\n совпадают {int(list_arg[0]) == int(list_arg[1])}') if len(list_arg) == 2 else print('целое')

# dz_2(input(' введите число '))

"""
    3. Создать два списка с различным количеством элементов. 
        В первом должны быть записаны ключи, во втором — значения. 
        Необходимо написать функцию, создающую из данных ключей и значений словарь. 
        Если ключу не хватает значения, в словаре для него должно сохраняться значение None. 
        Значения, которым не хватило ключей, необходимо отбросить.
"""
def dz_3(key_list, val_list):
    ensw_dict = {}

    for val, key in enumerate(key_list):
        if val < len(val_list):
            ensw_dict.update({key: val_list[val]})
        else:
            ensw_dict.update({key: None})
    
    print(ensw_dict)

# dz_3(['k_1', 'k_2', 'k_3', 'k_4', 'k_5'], ['v_1', 'v_2', 'v_3', 'v_4'])

"""
    4. Написать программу, в которой реализовать две функции. 
        В первой должен создаваться простой текстовый файл. 
        Если файл с таким именем уже существует, выводим соответствующее сообщение. 
        Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. 
        Для создания списков использовать генераторы. Применить к спискам функцию zip(). 
        Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, 
            чтобы каждая строка файла содержала текстовое и числовое значение. 
        Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. 
        Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. 
        Вся программа должна запускаться по вызову первой функции.

    5. Усовершенствовать первую функцию из предыдущего примера. 
        Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число). 
        Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных). 
        Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений. 
        Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок, 
            состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
import os


def dz_4_5():
    def print_file(path_file, find_text = ''):
        # Чтение из файла построчно
        with open(path_file) as file:
            for el in file:
                text = el.rstrip('\n')

                # ищем индекс текста(find_text) в строке(text), переназначаем переменные(first_idx, count_find_text)
                if text.find(find_text) - 2 < 0:
                    first_idx = 'Нет вхождений'
                    count_find_text = 'Нет вхождений'
                else:
                    first_idx = text.find(find_text) - 2
                    count_find_text = text.count(find_text)

                print(f'{text} Индекс первого вхождения - {first_idx}; Колличество вхождений - {count_find_text};')

    
    def create_file(text_list, int_list):
        # создаем путь в директорию + название файла
        path_file = os.path.join(os.getcwd(), 'text.txt')

        if os.path.exists(path_file):
            print('существует')
        else:
            # создаем текст и записываем в файл
            text = ''
            for el in zip(text_list, int_list):
                text += f'{el}\n'

            with open('text.txt', 'w') as file:
                file.write(text)

        # Выводим значения из файла (путь до файла, ищим текств в файле)
        print_file(path_file, 'l')

    create_file(['alex_1','piter','celli','loe_3'],[10, 11, 12, 13])

dz_4_5()


