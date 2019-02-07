with open("/home/ben/Документы/Python_Developer/HomeWork/Class 7/Test.txt",'r') as file:
    
    b = {}
    data = file.readline()
    while data:
        a = (data.split())
        b[a[0]]=a[1:]
        data = file.readline()    
    print(b)
    