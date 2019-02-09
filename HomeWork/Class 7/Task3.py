# Реализовать программу с базой учащихся группы (данные хранятся в файле). 
# Записи по учащемуся: имя, фамилия, пол, возраст. 
# Программа должна предусматривать поиск по одному или нескольким полям базы. 
# Результат выводить в удобочитаемом виде с порядковым номером записи.

def mark(data):
    slovar = {}
    do_3 = []
    for i in data:
        i = i.split()
        slovar[int(i[2])] = i[0]+' '+i[1]
    sum_ball = 0
    for k in slovar.keys():
        sum_ball += k
        if k<3:
            do_3.append(slovar[k])
    return do_3, sum_ball

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 7/Test2.txt",'r') as file:
    data = file.readlines()
    sum_ball, do_3 = mark (data)
    
    print (do_3)
    print (sum_ball)