'''
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь. '''


class WareHouse:
    def __init__(self):
        self.table = {}

    def store(self, equip, counts):
        self.table[equip] = counts


class division:
    def __init__(self, name):
        self.name = name
        self.d_store = {}

    def division_store(self, equip, counts):

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