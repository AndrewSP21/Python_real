"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """


class WareHouse:
    pass


class OfficeEquipment(WareHouse):
    def __init__(self, name, maker, production_date, serial_number):
        self.name = name
        self.maker = maker
        self.production_date = production_date
        self.serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, name, maker, production_date, serial_number, type, speed_print):
        self.type = type
        self.speed_print = speed_print
        super().__init__(name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.type}\n{self.speed_print}'


class Scanner(OfficeEquipment):
    def __init__(self, name, maker, production_date, serial_number, view, color_type):
        self.view = view
        self.color_type = color_type
        super().__init__(name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.view}\n{self.color_type}'


class Сopier(OfficeEquipment):
    def __init__(self, name, maker, production_date, serial_number, paper_type):
        self.paper_type = paper_type
        super().__init__(name, maker, production_date, serial_number)

    def __str__(self):
        return f'{self.name}\n{self.maker}\n{self.production_date}\n{self.serial_number}\n{self.paper_type}'


a = Printer('HP LaserJet 5000', 'HP', '12.12.2021', 'JJGFDRTERTER-342', 'Лазерный', '500 стр/мин')
b = Scanner('HP ScanJet 3200', 'HP', '12.12.2021', 'RTWWTWETRWE-r2', 'Настольный', 'Цветной')
c = Сopier('Xerox 1219', 'Xerox', '12.12.2021', 'DFHTYRTY-34-dgsf', 'Толстая бумага')
print(a)
print(b)
print(c)