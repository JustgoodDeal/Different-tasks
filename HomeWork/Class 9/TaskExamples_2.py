# Если в файле записано несколько разных словарей (каждый в отдельной строке), которые необходимо по-отдельности передать через json.

import json

with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 9/Test_Lesson.json",'r') as file:
    data = file.readlines()
    b=[]
    for i in data:
        slovar = json.loads(i)
        b.append(slovar)
print (b)