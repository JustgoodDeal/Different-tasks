# Реализовать программу с базой учащихся группы (данные хранятся в файле). 
# Записи по учащемуся: имя, фамилия, пол, возраст. 
# Программа должна предусматривать поиск по одному или нескольким полям базы. 
# Результат выводить в удобочитаемом виде с порядковым номером записи.

import json

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 8/Test3_with_json.json",'r') as file:
    people = json.load(file)

def men(people):
    muj=[]
    for i in range(len(people)):
        for v in people[i].values():
            if v=='male':
                muj.append (i+1)
                muj.append (people[i].get('Name'))
    return muj

print('Men in the group:')
muj = men(people)
for i in range(0,len(muj),2):
    print(muj[i],muj[i+1]) 