class Transport:
    def __init__(self, motor:int, door: int, wheel: int, horsepower: float):
        self.door = door
        self.wheel = wheel
        self.horsepower = horsepower
        self.motor = motor


    def calculate_way(self):
        if self.motor == 'electric':
            return (300 * self.horsepower)/self.wheel
        elif self.motor == 'gas':
            return (500 * self.horsepower)/self.wheel
        elif self.motor == 'diesel':
            return (400 * self.horsepower)/self.wheel

class Coupe(Transport):
    def doors_in_car(self):
        if self.door == 2:
            return 'Coupe'
        else:
            return 'sorry :0'
class Sedan(Transport):
    def doors_in_car(self):
        if self.door == 4:
            return 'Sedan'
        else:
            return 'again sorry :0'
class Miniwan(Transport):
    def doors_in_car(self):
        if self.door == 6:
            return 'Miniwan'
        else:
            return 'ha-hah sorry ;)'


class Sport_car(Transport):
    def calculate_way(self):
        if self.motor == 'gas':
            return 500 * self.horsepower * self.wheel
        else:
            return 'it is not sportcar'

class Family_car(Transport):
    def calculate_way(self):
        if self.motor == 'gas'
            return 200 * self.horsepower * self.wheel
        elif self.motor == 'electric':
            return 150 * self.horsepower * self.wheel



'''
продолжи идею об авто,
 
расход топлива в простых и спорткарах

+

создание 3-х ботов в тг 

+ 

работа с csv файлом о машинах
'''