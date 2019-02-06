#Написать программу “Калькулятор“, которая умеет выполнять простые арифметические операции
#  (сложение, вычитание, умножение, деление) над двумя числами. Числа запрашиваются у пользователя
#  “Enter first operand:“, “Enter second operand:“. Операция также запрашивается “Enter operator:” 
# где указывается ‘+’, ‘-’, ‘/’, ‘*’. Результат вывести в виде, например, “Result: 12". 
# Если пользователь ввел, отличную от разрешенных, операцию результат должен быть ‘Result: NaN’ (NaN - сокр. от Not a Number).

print('Enter first operand:')
a = int (input())
print('Enter second operand:')
b = int (input())
print ('Enter operator:')
c = input ()
if c == '+':
    print('Result:', a+b)
elif c == '-':
    print('Result:', a-b)
elif c == '/':
    print('Result:', a/b)
elif c == '*':
    print('Result:', a*b)
else:
    print ('Result: NaN')
