class Worker :
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

def set_income(self, wage, bonus):
    self.__income = {"wage": wagr, "bonus": bonus}

def get_income(self):
    return set.__income

class Position(Worker) :
    def __init__(self, name ,surname, position, income):
        super().__init__(name, surname, position,income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        total_income = self._Worker__income['wage'] + self._Worker__income['bonus']
        return total_income

employee1 = Position("Иван" ,"Иванов","Менеджер", {"wage": 500, "bonus": 100})
employee2 = Position("Елена", "Смирнова", "Разработчик", {"wage": 60000, "bonus": 12000})

print(employee1.get_full_name())
print(employee1.get_total_income())
print(employee2.get_total_income())
print(employee2.get_full_name())