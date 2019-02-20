# Реализовать программу подсчета площади, периметра, объема геометрических фигур 
# (треугольник, прямоугольник, квадрат, трапеция, окружность). Если одна из фигур не поддерживает вычисление одного из свойств, 
# в программе должно быть вызвано исключение с человеко-читабельным сообщением и корректно обработано.

from Classes.Class_for_Task0 import Quadrate
from Classes.Class_for_Task0 import Rectangle
from Classes.Class_for_Task0 import Triangle
from Classes.Class_for_Task0 import Trapeze

print('Выберите геометрическую фигуру: 1 - квадрат, 2 - прямоугольник, 3 - треугольник, 4 - трапеция, 5 - окружность')
figura = input()
if figura == '5':
    print('У данной фигуры невозможно вычислить площадь, периметр и объем')
elif figura != '1' and figura != '2' and figura != '3' and figura != '4':
    print ('Данные введены некорректно')
else:
    print('Что необходимо вычислить для выбранной фигуры? 1 - площадь, 2 - периметр, 3 - объем')
    action = input()
    if action == '3':
        instanse = Quadrate (1)
        print(instanse.volume())
    elif action != '1' and action != '2':
        print ('Данные введены некорректно')
    else:
        if figura == '4' and action == '1':
            print('Введите длину 2-х оснований, после - длину 2-х боковых сторон')
        else:
            print("Введите длину всех сторон выбранной фигуры")
        try:            
            sides = [int(i) for i in input().split()]
            if figura == '1':
                if len(sides) == 1:
                    instanse = Quadrate (sides[0])
                    if action == '1':                    
                        print(instanse.square())
                    if action == '2':
                        print(instanse.perimetr())
                else:
                    print ('Данные введены некорректно')    
            if figura == '2':
                if len(sides) == 2:
                    instanse = Rectangle (sides[0],sides[1])
                    if action == '1':                    
                        print(instanse.square())
                    if action == '2':
                        print(instanse.perimetr())
                else:
                    print ('Данные введены некорректно')
            elif figura == '3':
                if len(sides) == 3:
                    instanse = Triangle (sides[0],sides[1],sides[2])
                    if action == '1':                    
                        print(instanse.square())
                    if action == '2':
                        print(instanse.perimetr())
                else:
                    print ('Данные введены некорректно')
            elif figura == '4':
                if len(sides) == 4:
                    instanse = Trapeze (sides[0],sides[1],sides[2],sides[3])
                    if action == '1':                    
                        print(instanse.square())
                    if action == '2':
                        print(instanse.perimetr())
                else:
                    print ('Данные введены некорректно') 
        except ValueError:
            print ('Данные введены некорректно') 








    
    

 


