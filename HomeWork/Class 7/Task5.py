# Реализовать программу, позволяющую осуществлять управление файлами: 
# копирование, создание, удаление, переименование. 
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

import os

print('Что вы хотите сделать с файлом? "copy" - копировать, "create" - создать новый, "del" - удалить, "rename" - переименовать')
action = 'copy'
if action == 'create':
    print ('Укажите имя файла, который необходимо создать')
    name = 'Test67'
    print ('Укажите директорию, в которой необходимо создать данный файл')
    dir = '/home/ben/Документы/Python_Developer/HomeWork/Class 7'+'/'
    try:
        with open(dir+name,'x') as file:
            print ('Файл успешно создан')
    except FileNotFoundError:
        print ('Данной директории не существует')
    except FileExistsError:
        print ('Файл уже существует')
elif action == 'copy':
    print ('Укажите имя файла, который необходимо копировать:')
    name = 'Test5.txt'
    print ('Укажите директорию, в которой находится данный файл')
    dir = '/home/ben/Документы/Python_Developer/HomeWork/Class 7'+'/'    
    try:
        with open(dir+name,'r') as file:
            print ('Укажите директорию, в которую необходимо копировать файл')
            dir_to = '/home/ben/Документы/Python_Developer/HomeWork'+'/'
            dostup = os.access(dir_to, os.F_OK)
            if not dostup:
                raise IndentationError
            data = file.read()                        
            with open(dir_to+name,'a') as file2:
                file2.write(data)
                print ('Файл успешно скопирован')
    except IndentationError:
        print ('Данной директории не существует')         
    except FileNotFoundError:
        print ('Данного файла не существует') 
      
            
    

