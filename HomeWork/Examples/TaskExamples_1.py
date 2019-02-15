with open("/home/ben/Документы/Python_Developer/HomeWork/Class 8/Test1.txt",'r') as file:
    a = ''.join(file).split()       # получаем список из всех слов в файле
    print (a)
    
#    b = []
#    for i in file:
#        a = ''.join(i).split()
#        for j in a:
#            b.append (j)
#    print (b)

#   b = []
#    c = file.readline()
#    while c:
#        a = ''.join(c).split()
#        for j in a:
#            b.append (j)
#        c = file.readline()
#    print (b)


#    b = {}                         Делаем словарь из файла: построково читаем и добавляем Ключ и Список значений 
#    data = file.readline()
#    while data:
#        a = (data.split())
#        b[a[0]]=a[1:]
#        data = file.readline()    
#    print(b)

