# Реализовать программу, позволяющую осуществлять управление файлами: 
# копирование, создание, удаление, переименование. 
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

import Methods.For_Task5

print('Что вы хотите сделать с файлом? "copy" - копировать, "create" - создать новый, "remove" - удалить, "rename" - переименовать')
action = input()
while action:
    if action == 'copy':
        Methods.For_Task5.copy()
    elif action == 'create':
        Methods.For_Task5.create()
    elif action == 'remove':
        Methods.For_Task5.remove()
    elif action == 'rename':
        Methods.For_Task5.rename()
    print('Что вы еще хотите сделать с файлом? "copy" - копировать, "create" - создать новый, "remove" - удалить, "rename" - переименовать')
    action = input()

