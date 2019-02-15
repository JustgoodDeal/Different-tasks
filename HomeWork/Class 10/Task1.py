# Реализовать программу, которая отображает дерево каталогов. Путь к целевому каталогу запрашивается у пользователя. 
# В программе не должно использоваться циклов. Вывод результата программы должен быть следующего вида:
# |__ Folder 1
# |___ Folder 2
# |___ File 2.1
# |___ File 2.2
# |__ File 1.1
# |__ File 1.2
import os

def decor(func):
    def wrapper(directory):
        try:
            result = sorted(func(directory))
            result[0]='|___ '+result[0]
            result = '\n|___ '.join(result)
            if directory[-1]=='/':
                directory = directory[:-1]
            ind = directory.rfind('/')
            print('|__ '+directory[ind+1:])
            print(result)
        except FileNotFoundError:
            print('Путь к целевому каталогу не существует')
        except IndexError:
            print('Указанный каталог пустой')
        except NotADirectoryError:
            print('Вы указали путь не к каталогу, а к файлу')                
        return func
    return wrapper

print('Укажите путь к целевому каталогу:')
catalog_name = input()
@decor
def catalog_tree(directory):
    return os.listdir(directory)

catalog_tree(catalog_name)

