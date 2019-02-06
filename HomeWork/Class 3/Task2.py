# Дана строка ‘Hello!Anthony!Have!A!Good!Day!’. Создать список, 
# состоящий из отдельных слов [‘HELLO’, ‘ANTHONY’, ‘HAVE’, ‘A’, ‘GOOD’, ‘DAY’].

a = 'Hello!Anthony!Have!A!Good!Day!'.upper().split('!')
b = a[:len(a)-1]
print (b)
