# Даны 2 объекта, один из них словарь. Необходимо, используя декоратор, записать эти 2 объекта в разные файлы.
#  Словарь передать с помощью метода json, а второй объект записать в другой файл обычным способом.

import json

def decorator(any_func):
    def wrapper (obj_1, obj_2):
        if type (obj_1) == dict:
            with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 9/Test_Lesson.json",'a+') as file:
                file.seek(0)
                data = file.readlines()
                if len (data):                  # Если файл, в который мы будем передавать словарь, не пустой, мы переводим строку.
                    file.write('\n')            # Если же файл пустой - строку не переводим (иначе 1-я строка будет пустая)
                json.dump(obj_1,file)
            with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 9/Test_Lesson.txt",'a+') as file:
                if len (data):
                    file.write('\n')
                file.write(obj_2)
        else:
            with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 9/Test_Lesson.json",'a') as file:
                file.write('\n')
                json.dump(obj_2,file)
            with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 9/Test_Lesson.txt",'a') as file:
                file.write('\n'+obj_1)
        return any_func(obj_1, obj_2)
    return wrapper


first = {'a':'2','b':'5'}
second = 'My stroka'

@decorator
def prosto_vivod(a, b):
    return a, b

prosto_vivod(first,second)



