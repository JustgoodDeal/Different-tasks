# Реализовать программу с базой учащихся группы (данные хранятся в файле). 
# Записи по учащемуся: имя, фамилия, пол, возраст. 
# Программа должна предусматривать поиск по одному или нескольким полям базы. 
# Результат выводить в удобочитаемом виде с порядковым номером записи.

def pol(data):
    list_slovar = []
    for i in data:
        slovar = {}
        i = i.split()
        slovar[' '.join(i[1:3])] = i[0:1]+i[3:]
        list_slovar.append(slovar)
    names = []
    for j in range(len(list_slovar)):
        for k,v in list_slovar[j].items():
            if v[1]=='муж':
                names.append((v[0],k))   
    return names
        
with open("/home/ben/Документы/Python_Developer/HomeWork/Class 8/Test3.txt",'r') as file:
    data = file.readlines()
    names = pol(data)
print('Мужчины, учащиеся в группе:')
for i in range (len(names)):
    print(names[i][0],names[i][1])
