class Auto:
    info_1 = "Автомобиль заведён"
    info_2 = ''
    def on_start(self):
        self.info_2 = "Автомобиль заведён***"

a = Auto()
a.on_start()
print(a.info_1)
print(a.info_2)
