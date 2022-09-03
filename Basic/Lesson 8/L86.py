'''6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
ООП. '''


class WareHouse:
    def __init__(self):
        self.table = {}

    def store(self, equip, counts):
        if not str(counts).isdigit():
            raise NotDigit(counts)
        else:
            self.table[equip] = counts


class division:
    def __init__(self, name):
        self.name = name
        self.d_store = {}

    def division_store(self, equip, counts):
        if not str(counts).isdigit():
            raise NotDigit(counts)
        else:
            self.d_store[equip] = counts



class OfficeEquipment(WareHouse):
    def __init__(self, type_equip, name, maker, production_date, serial_number):
        self.type_equip = type_equip
        self.name = name
        self.maker = maker
        self.production_date = production_date
        self.serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, type_equip, name, maker, production_date, serial_number, type, speed_print):
        self.type = type
        self.speed_print = speed_print
        super().__init__(type_equip, name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.type}\n{self.speed_print}'


class Scanner(OfficeEquipment):
    def __init__(self, type_equip, name, maker, production_date, serial_number, view, color_type):
        self.view = view
        self.color_type = color_type
        super().__init__(type_equip, name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.view}\n{self.color_type}'


class Сopier(OfficeEquipment):
    def __init__(self, type_equip, name, maker, production_date, serial_number, paper_type):
        self.paper_type = paper_type
        super().__init__(type_equip, name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.paper_type}'


class NotDigit(Exception):
    def __init__(self, current):
        self.current = current

    def __str__(self):
        return f"Допустим ввод только целых чисел. Введенные данные: {self.current} не являются целым числом"


a = Printer('Принтер', 'HP LaserJet 5000', 'HP', '12.12.2021', 'JJGFDRTERTER-342', 'Лазерный', '500 стр/мин')
b = Scanner('Сканер', 'HP ScanJet 3200', 'HP', '12.12.2021', 'RTWWTWETRWE-r2', 'Настольный', 'Цветной')
c = Сopier('Копир', 'Xerox 1219', 'Xerox', '12.12.2021', 'DFHTYRTY-34-dgsf', 'Толстая бумага')
# print(a)
# print(b)
# print(c)

stock = WareHouse()
stock.store(a.name, 3)
stock.store(b.name, 2)
stock.store(c.name, 4)



marketing = division('Маркетинг')


def moving_equip(divis, stocks, name_equip, count):
    var = stocks.table[name_equip]
    var -= count
    stocks.store(name_equip, var)
    divis.division_store(name_equip, count)


moving_equip(marketing, stock, 'HP LaserJet 5000', 1)

print(stock.table['HP LaserJet 5000'])
print(marketing.d_store['HP LaserJet 5000'])

try:
    stock.store(a.name, 'opo')
except NotDigit as exception:
    print(f"Ошибка ввода: {exception.current} не цифра")