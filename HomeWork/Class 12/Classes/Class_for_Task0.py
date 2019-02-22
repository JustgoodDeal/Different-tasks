class Elevator:
    def __init__(self, count_up = 0, floor = 1, name = None):
        self.count_up = count_up
        self.name = name
        self.floor = floor
    
    def __repr__(self):
        return 'После сложения/вычитания экземпляров класса значение атрибута count_up равняется: {}'.format(self.count_up)
    @property
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self, value):
        if value > 9 or value < 1:
            raise ValueError('Лифт может находиться только на этажах с 1-го по 9-й')
        self._floor =  value
    def lift (self,value):
        if 0 < value < 10:
            if value > self.floor:
                Elevator.up(self, value - self.floor)
                return 'Лифт прибыл по вызову на '+ str(self.floor) + ' этаж'
            elif value < self.floor:
                Elevator.down(self, self.floor - value)
                return 'Лифт прибыл по вызову на '+ str(self.floor) + ' этаж'
            else:
                return 'Лифт был вызван с '+ str(self.floor) + ' этажа, на котором он и находился'
        else:
            return 'Ошибка!!! Лифт можно вызвать только с реально существующего этажа (с 1-го по 9-й)'
    def up(self,value):
        if self.floor + value < 10 and value>0:
            self.floor += value
            self.count_up +=1
        elif value<=0:
            return 'Ошибка!!! Необходимо вводить только положительные числа'
        else:
            if 9 - self.floor == 1:
                return 'Ошибка!!! Можно подняться максимум на один этаж, так как лифт находится на восьмом этаже'
            elif 2<=9 - self.floor<=4:
                return 'Ошибка!!! Можно подняться максимум на {} этажа, так как лифт находится на {} этаже'.format(9 - self.floor,self.floor)
            else:
                return 'Ошибка!!! Можно подняться максимум на {} этажей, так как лифт находится на {} этаже'.format(9 - self.floor,self.floor)
        return 'Поездка завершена. Этаж, на котором находится лифт: ' + str(self.floor) + ''
    def down(self,value):
        if self.floor - value > 0 and value>0:
            self.floor -= value
        elif value<=0:
            return 'Ошибка!!! Необходимо вводить только положительные числа'
        else:
            if self.floor == 2:
                return 'Ошибка!!! Можно спуститься максимум на один этаж, так как лифт находится на втором этаже'
            elif 2<self.floor<=5:
                return 'Ошибка!!! Можно спуститься максимум на {} этажа, так как лифт находится на {} этаже'.format(self.floor-1,self.floor)
            else:
                return 'Ошибка!!! Можно спуститься максимум на {} этажей, так как лифт находится на {} этаже'.format(self.floor-1,self.floor)
        return 'Поездка завершена. Этаж, на котором находится лифт: ' + str(self.floor)
    def __add__(self, other):
        return Elevator (self.count_up + other.count_up)
    def __sub__(self, other):
        if self.count_up==0:
            raise Exception ('Ошибка неправильной операции') 
        else:
            return Elevator (self.count_up - other.count_up)
    @classmethod
    def larger_up (cls, *args):
        often = args[0]
        for i in args:
            if i.count_up>often.count_up:
                often = i
        return 'Лифт, который совершил большее количество поднятий: ' + often.name
    @classmethod
    def sum_up (cls, *args):
        sum = 0
        for i in args:
            sum += i.count_up                
        return sum
    def info (self, *args):
        #self.name self.count_up
        sum = Elevator.sum_up (self,*args)
        procent = self.count_up/sum * 100
        return '{}: количество поднятий - {}, процент от общего количества поднятий всех лифтов - {}'.format(self.name,self.count_up,round(procent,1))    
    @classmethod
    def decor (cls, func):
        def wrapper(*args):
            return 'Общее количество поднятий всех лифтов: ' + str(func(*args))
        return wrapper
