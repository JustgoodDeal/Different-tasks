# Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.  
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
# После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
# push n - Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
# pop    - Удалить из стека последний элемент. Программа должна вывести его значение. 
# back   - Программа должна вывести значение последнего элемента, не удаляя его из стека. 
# size   - Программа должна вывести количество элементов в стеке. 
# clear  - Программа должна очистить стек и вывести ok. 
# exit   - Программа должна вывести bye и завершить работу.

with open("/home/ben/Документы/Python_Developer/HomeWork/Class 7/Test_star.txt",'r') as file:
    stack = []
    stroka = file.readline()
    while stroka:
        item_stroka = stroka.split()
        if item_stroka[0] == 'push':
            stack.append(item_stroka[1])
            print('ok')
        elif item_stroka[0] == 'pop':
            print (stack.pop())
        elif item_stroka[0] == 'back':
            print(stack[-1])
        elif item_stroka[0] == 'size':
            print(len(stack))
        elif item_stroka[0] == 'clear':
            stack.clear()
            print('ok')
        elif item_stroka[0] == 'exit':
            print('bye')
            break
        stroka = file.readline()