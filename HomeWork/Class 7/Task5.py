# Реализовать программу, позволяющую осуществлять управление файлами: 
# копирование, создание, удаление, переименование. 
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 7/Test2.txt",'r') as file:
    slovar = {}
    for i in file:
        i = i.split()
        slovar[int(i[2])] = i[0]+' '+i[1]
    ball = 0
    count_pupil = 0
    for k in slovar.keys():
        ball += k
        count_pupil += 1
        if k<3:
            print (slovar[k])
    print('Средний балл по классу: '+str(ball/count_pupil))

