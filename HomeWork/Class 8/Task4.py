# Реализовать программу, которая выводит содержимое каталога в файловой системе. 
# Путь к каталогу запрашивается у пользователя.

import os

def catalog_context (dirName):
    if '/' in dirName:
        try:
            names = os.listdir(dirName)
        except (FileNotFoundError, NotADirectoryError):
            return 0
        ways = []
        for i in names:
            fullname = os.path.join(dirName, i) # получаем полное имя
            if os.path.isfile(fullname):
                ways.append(fullname)
            else:
                return 1
        return ways
    else:
        try:
            dirName = os.listdir(dirName)
            return dirName
        except FileNotFoundError:
            return 0  

context = catalog_context (input())
if context == 0:
    print('Такого каталога не существует')
elif context == 1:
    print('В данном каталоге нет файлов - только подкаталоги')
else:
    for i in sorted(context):
        print(i)
    

            

    