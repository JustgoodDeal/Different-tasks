# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 8/Test1.txt",'r') as file:
    # data = file.readlines()                       либо так
    string_num = 0          # print (len(data))
    for i in file:          # for i in data:        и так
        string_num += 1
        if not '\n' in i:
            print('Количество символов: '+ str(len(i)), end = '')
        else:
            print('Количество символов: '+ str(len(i)-1), end = '')
        words = i.split()
        print(', Количество слов: '+ str(len(words)))    
print ('Количество строк: '+str(string_num))


                                # Либо так:
#with open("/home/ben/Документы/Python_Developer/HomeWork/Class 7/Test1.txt",'r') as file:
#    data = file.readline()
#    string_num = 0
#    while data:
#        string_num += 1
#        if not '\n' in data:
#            print('Количество символов: '+ str(len(data)), end = '')
#        else:
#            print('Количество символов: '+ str(len(data)-1), end = '')
#        words = data.split()
#        print(', Количество слов: '+ str(len(words)))
#        data = file.readline()        
#print ('Количество строк: '+str(string_num))
