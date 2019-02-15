# Даны 2 объекта, один из них словарь. Необходимо, используя декоратор, записать эти 2 объекта в разные файлы.
#  Словарь передать с помощью метода json, а второй объект записать в другой файл обычным способом.

import json

def decorator(any_func):
    def wrapper (obj_1, obj_2): # Не совсем корректно открывать файл с расширением json в режиме 'a+' (дозапись), так как он после дозаписи
                                # выдает ошибку "End of file expected". Но с него можно легко считывать (loads) каждый словарь 
                                # по отдельности (TaskExamples_2.py). Если же дозаписывать в файл с расширением txt, то ошибок не выскочит
                                # и с него тоже можно считывать каждый словарь по отдельности
        with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 10/Files/File_for_Lesson_Task.json",'a+') as file:
            file.seek(0)
            data = file.readlines()
            if len (data):                  # Если файл, в который мы будем передавать словарь, не пустой, мы переводим строку.
                file.write('\n')            # Если же файл пустой - строку не переводим (иначе 1-я строка будет пустая)
            if type (obj_1) == dict:
                json.dump(obj_1,file)
            else:
                json.dump(obj_2,file)
        with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 10/Files/File_for_Lesson_Task.txt",'a+') as file:
            if len (data):
                file.write('\n')
            if type (obj_1) == dict:
                file.write(obj_2)
            else:
                file.write(obj_1)        
    return wrapper

first = {'a':'2','b':'5'}
second = 'My stroka'

@decorator
def prosto_vivod(a, b):
    return a, b

prosto_vivod(first, second)



