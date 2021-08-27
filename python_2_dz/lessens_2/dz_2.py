"""
    1. Проверить механизм наследования в Python. Для этого создать два класса. 
        Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену. 
        Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), 
            отвечающую за отображение информации о товаре в одной строке. 
        Проверить работу программы, создав экземпляр (объект) родительского класса.
"""
def num_1():
    class ItemDiscount:
        def __init__(self, prise, name):
            self.prise = prise
            self.name = name

    class ItemDiscountReport(ItemDiscount):
        def get_parent_data(self):
            print(f' Имя - { self.name }\n Цена { self.prise }')


    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apple')
    print(a.name, a.prise)
    b.get_parent_data()

# num_1()


"""
    2. Инкапсулировать оба параметра (название и цену) товара родительского класса. 
        Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""
def num_2():
    class ItemDiscount:
        def __init__(self, prise, name):
            self.__prise = prise
            self.__name = name

    class ItemDiscountReport(ItemDiscount):
        def get_parent_data(self):
            print(f' Имя - { self.__name }\n Цена { self.__prise }')


    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apple')
    print(a.__name, a.__prise)
    b.get_parent_data()

# num_2()


"""
    3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. 
        Результат выполнения заданий 1 и 2 должен быть идентичным.
"""
def num_3():
    class ItemDiscount:
        def __init__(self, prise, name):
            self.__prise = prise
            self.__name = name
        
        def get_info(self):
            return self.__prise, self.__name

    class ItemDiscountReport(ItemDiscount):
        def get_parent_data(self):
            name, prise = self.get_info()
            print(f' Имя - { name }\n Цена { prise }')

    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apple')
    print( a._ItemDiscount__prise, a._ItemDiscount__name )
    b.get_parent_data()


# num_3()


"""
    4. Реализовать возможность переустановки значения цены товара. 
        Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены. 
        Следует проверить это, вызвав соответствующий метод родительского класса 
            и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""
def num_4():
    class ItemDiscount:
        def __init__(self, prise, name):
            def dz_2_test():
                self.prise = prise
                self.name = name

    class ItemDiscountReport(ItemDiscount):
        def get_parent_data(self):
            print(f' Имя - { self.name }\n Цена { self.prise }')


    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apol')

    ItemDiscount.prise, ItemDiscount.name = 100, '???'

    print(a.name, a.prise)
    b.get_parent_data()

# num_4()


"""
    5. Реализовать расчет цены товара со скидкой. 
        Величина скидки должна передаваться в качестве аргумента в дочерний класс. 
        Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная — скидка), 
            и перегрузку метода str дочернего класса. 
        В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой. 
        Чтобы все работало корректно, не забудьте инициализировать дочерний 
            и родительский классы (вторая и третья строка после объявления дочернего класса).
"""
def num_5():
    class ItemDiscount:
        def __init__(self, prise, name):
            self.prise = prise
            self.name = name

    class ItemDiscountReport(ItemDiscount):
        def __init__(self, prise, name, sale):
            self.prise = (prise / 100 * sale) - prise
            self.name = name
 
        def get_parent_data(self):
            print(f' Имя - { self.name }\n Цена { self.prise }')


    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apple', 5)
    
    print(a.name, a.prise)
    b.get_parent_data()
    

# num_5()


"""
    6. Проверить на практике возможности полиморфизма. 
        Необходимо разделить дочерний класс ItemDiscountReport на два класса. 
        Инициализировать классы необязательно. 
        Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. 
        Далее реализовать выполнение каждой из функции тремя способами.
"""
def num_6():
    class ItemDiscount:
        def __init__(self, prise, name):
            self.prise = prise
            self.name = name

    class ItemDiscountReport_1(ItemDiscount):
        def get_info(self):
            print(f' Имя - { self.name }')

    class ItemDiscountReport_2(ItemDiscount):
        def get_info(self):
            print(f' Цена - { self.prise }')


    a = ItemDiscount(1, 'banana')
    b = ItemDiscountReport(10, 'apple')

    print(a.name, a.prise)
    b.get_parent_data()


# num_6()
