# class Phone:
#     # простой метод
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#
#     def check_sim(self, mobile_operator):
#         if self.model == '1785' and mobile_operator == "MTS":
#             print('You mobile operator is MTS')
#         else:
#             print('You mobile operator is A1')
#
#
#
#     @staticmethod#Статический метод
#     def model_hash(model):
#         if model == "1785":
#             return 34565
#         elif model == "7":
#             return 45567
#         else:
#             return None
#
#
# Phone.model_hash('1785')
# my_phone = Phone('red', '1785')
# my_phone.check_sim('MTS')
# print(Phone.model_hash('1785')) #34565
# my_phone = Phone('red', '1785')
#
# my_phone.check_sim('MTS')
# print(my_phone.color, my_phone.model)
# my_phone_2 = Phone('black', '7')
# my_phone_2.check_sim('A1')
# print(my_phone_2.color, my_phone_2.model)


# class Human:
#     default_name = None
#     default_age = None
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = "no"
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name)
#         print(Human.default_age)
#
#     def earn_money(self, arg):
#         self.__money += arg
#
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money >= price:
#             self.__make_deal(house, price)
#         else:
#             print('Not enough money!')
#
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house
#
# class House:
#
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def final_price(self, discount):
#         final_price = self.price * (100 - discount)/100
#         print(f'Final prise: {final_price}')
#         return final_price
#
# class SmallHouse(House):
#
#     default_area = 40
#
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)
#
#
# if __name__ == '__main__':
#
#     Human.default_info()
#     alex = Human('Sasha', 45)
#     alex.info()
#
#     small_house = SmallHouse(8500)
#
#     alex.buy_house(small_house, 5)
#
#     alex.earn_money(5000)
#     alex.buy_house(small_house, 5)
#
#     alex.earn_money(10000)
#     alex.buy_house(small_house, 5)
#     alex.info()


# class Phone:
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#     # Если телефон включен, делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')
#
# # унаследованный класс
# class MobilPhone(Phone):
#
#     # добавляем новое устройство, батарею
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
# # заряжаем телефон на величину переданного значения
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to...{self.battery} %')
#
#     def info(self):
#         print(f'Class name: {MobilPhone.__name__}')
#         print(f'If mobile phone is On: {self.is_on}')
#         print(f'Battery level: {self.battery}')
#
# my_mobile_phone = MobilPhone()
# dir(my_mobile_phone)
# print(my_mobile_phone.charge(50))
# my_mobile_phone.info()
#Родительский класс может иметь несколько дочерних
#создаём класс Vehicle
# class Vehicle:
#    def vehicle_method(self):
#         print('Это родительский метод из класса Vehicle')
#
# #создаём сласс Car, который наследует Vehicle
# class Car(Vehicle):
#     def car_method(self):
#         print('Это дочерний метод из класса Car')
#
# #создаём сласс Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def cycle_method(self):
#         print('Это дочерний метод из класса Cycle')
#
# car_a = Car()
# car_a.vehicle_method()#вызов метода родительского класса
# car_b = Car()
# car_b.vehicle_method()#вызов метода родительского класса
#
# #Дочерний класс может иметь несколько родительских
# class Camera:
#    def camera_method(self):
#         print('Это родительский метод из класса Camera')
#
#
# class Radio:
#     def radio_method(self):
#         print('Это родительский метод из класса Radio')
#
#
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print('Это дочерний метод из класса CellPhone')
#
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()

#Перегрузка метода
# class Car:
#     def start(selfs, a, b=None):
#         if b is not None:
#             print(a+b)
#         else:
#             print(a)
#
# car_a = Car()
# car_a.start(10)
# car_a.start(10, 5)
# # Если метод start() вызывается передачей одного аргумента, то параметр будет выведен на экран. Если мы переададим два
# # аргумента методу start(), то он внесёт оба аргумента и выведет результат суммы
#
# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def getCarModel(self):
#         return "Год выпуска модели: " + str(self.model)
#
# carA = Car(2088)
# print(carA.getCarModel())


# import string
#
# # Алфавит
# class Alphabet:
#
#     def __init__(self, language, letters_str):
#         self.lang = language
#         self.letters = list(letters_str)
#
#     # Печатаем все буквы алфавита
#     def print(self):
#         print(self.letters)
#
#     # Возвращаем количество букв в алфавите
#     def letters_num(self):
#         len(self.letters)
#
#
# # Английский алфавит
# class EngAlphabet(Alphabet):
#
#     __letters_num = 26
#
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#
#     # Проверяем, относится ли буква к английскому алфавиту
#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         return False
#
#     # Возвращаем количество букв в алфавите
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     # Печатаем пример текста на английском языке
#     @staticmethod
#     def example():
#         print("English Example:\nDon't judge a book by it's cover.")
#
#
# if __name__ == '__main__':
#     eng_alphabet = EngAlphabet()
#     eng_alphabet.print()
#     print(eng_alphabet.letters_num())
#     print(eng_alphabet.is_en_letter('F'))
#     print(eng_alphabet.is_en_letter('Щ'))
#     EngAlphabet.example()

class Tomato:

    # Стадии созревания томата
    states = {0: 'Cаженец', 1: 'Цветок', 2: 'Зелёный', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переходим к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверяем степень зрелости
    def is_ripe(self):
        if self._state == 3:
            return True
        return False


    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    # Создадим список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим  томаты на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли томаты созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Садовник получает растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживает за растением
    def work(self):
        print('Садовник работает')
        self._plant.grow_all()
        print('Работа закончена')

    # Собирает урожай томатов
    def harvest(self):

        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Уражай томатов собран!')
        else:
            print('Томаты ещё не созрели')

    # Используем статический метод, который выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Если плоды покраснели, их можно собирать. Урожай с детерминантных сортов помидор можно собрать лишь 
        один раз, в то время как индетерминантные сорта плодоносят непрерывно. Тома́ты склонны трескаться при обильных 
        дождях, поэтому урожай лучше собирать до начала дождей.''')



if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Макс', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()