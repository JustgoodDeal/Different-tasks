# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. 
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

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
    do_3, sum_ball = mark (data)
    if len(do_3):
        print ('Следующие учащиеся получили оценку ниже, чем 3 балла:')
        for i in do_3:
            print (i)
    else:
        print ('Оценку ниже, чем 3 балла, не получил никто.')
    print('Средний балл по классу: '+str(sum_ball/len(data)))
    
