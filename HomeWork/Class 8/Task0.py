# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 8/Test0.txt",'w') as file:
    dannie = input()
    while dannie:
        file.write(dannie + '\n')
        dannie = input() 