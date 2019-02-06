# Написать программу поиска суммы минимального и максимального из трех введенных чисел

a = [int (input()),int (input()),int (input())]
min=a[0]
max=a[0]
for i in a:
    if i < min:
        min=i
    elif i > max:
        max=i
print(min+max)
