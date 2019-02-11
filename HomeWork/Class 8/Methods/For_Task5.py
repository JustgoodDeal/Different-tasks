import os

def copy():
    print ('Укажите имя файла, который необходимо копировать:')
    name = input()
    print ('Укажите директорию, в которой находится данный файл')
    dir = input()+'/'    
    try:
        with open(dir+name,'r') as file:
            print ('Укажите директорию, в которую необходимо копировать файл')
            dir_to = input()+'/'
            dostup_dir = os.access(dir_to, os.F_OK)
            if not dostup_dir:
                raise IndentationError
            dostup_file = os.access(dir_to+name, os.F_OK)
            if dostup_file:
                raise IndexError
            data = file.read()                        
            with open(dir_to+name,'a') as file2:
                file2.write(data)
                print ('Файл успешно скопирован')
    except FileNotFoundError:
        print ('Данного файла не существует')
    except IndentationError:
        print ('Данной директории не существует')         
    except IndexError:
        print ('В указанной директории уже существует файл с таким именем')

def create():
    print ('Укажите имя файла, который необходимо создать')
    name = input()
    print ('Укажите директорию, в которой необходимо создать данный файл')
    dir = input()+'/'
    try:
        file = open(dir+name,'x')
        file.close()
        print ('Файл успешно создан')
    except FileNotFoundError:
        print ('Данной директории не существует')
    except FileExistsError:
        print ('Файл с таким именем уже существует')

def remove():
    print ('Укажите имя файла, который необходимо удалить')
    name = input()
    print ('Укажите директорию, в которой находится данный файл')
    dir = input()+'/'
    try:
        os.remove (dir+name)
        print ('Файл успешно удален')
    except FileNotFoundError:
        print ('В указанной директории нет данного файла')

def rename():
    print ('Укажите имя файла, который необходимо переименовать')
    name = input()
    print ('Укажите директорию, в которой находится данный файл')
    dir = input()+'/'
    dostup_file = os.access(dir+name, os.F_OK)
    if not dostup_file:
        print (dostup_file)
        print ('В указанной директории нет данного файла')
    else:
        print ('Укажите имя нового файла')
        new_name = input()
        os.rename (dir+name, dir+new_name)
        print ('Файл успешно переименован')
    
    
    