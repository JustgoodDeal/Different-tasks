# Если среди трех чисел А,В,С имеется хотя бы одно четное вычислить максимальное, иначе - минимальное

a = [int (input()),int (input()),int (input())]
for i in a:
    if i%2==0:
        print(max(a))
        break
else:
    print(min(a))

