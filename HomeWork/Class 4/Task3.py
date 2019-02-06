# Вводятся строки. Определить самую длинную строку и вывести ее номер на экран. 
# Если самая длинная строка повторяется несколько раз, то вывести номера всех таких строк.
def longest_string (x):
    e = sorted(x)
    max_element = e[len(e)-1]
    max = [i+1 for i in range (len(x)) if x[i]==max_element]
    return max

def Test_longest_string():
    assert longest_string ([6,10,3,2,10]) == [2,5], 'Тест провален'
    assert longest_string ([1,1]) == [1,2], 'Тест провален'
    assert longest_string ([1,1,1,2,2,2,2]) == [4,5,6,7], 'Тест провален'


d = []
while True:
    a = input()             # Для неизвестного количества строк, который пользователь введет с клавиатуры. 
    if a == '':             # После ввода пустой строки цикл прерывается (2 раза подряд нажать Enter)
        break
    d.append(len(a)) 
max = longest_string (d)
print (*max, sep='\n')
Test_longest_string()