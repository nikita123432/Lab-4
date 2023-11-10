class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print("Запустить отрисовки ")

class Pen (Stationery):
    def drow(self):
        print(f"Используется ручка для отрисовки {self.title}")

class Pencil(Stationery):
    def drow(self):
        print(f"Используется карандаш для отсовки {self.title}")

class Handle(Stationery):
    def drow(self):
        print(f"Используется маркер для отрисовки {self.title}")

pen = Pen("Письма")
pencil = Pencil("рисунка")
handle = Handle("плаката")

pen.drow()
pencil.drow()
handle.drow()