# Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
# Вывести информацию об оценках по возрастанию в виде: ‘Hello Ann! Your grade is 9’

grade = [('Ann', 9), ('Jonn', 7), ('Smith',5), ('George', 6)]
a = sorted(grade, key=lambda tup: tup[1])
for i in a:
    print ('Hello {}! Your grade is {}'.format(i[0],i[1]))