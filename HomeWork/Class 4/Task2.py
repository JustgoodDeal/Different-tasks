# Найти и вывести все гласные буквы (без повторений), которые встречаются 
# в самом коротком слове. Текст запрашивается у пользователя. Алфавит использовать любой. 

def del_znakov_prepinaniya (word):              # 1) удаляем знаки препинания
    for i in word:
        if i in znaki_prepinaniya:
            word = word.replace(i,'')
    return word

def min_dlina (x):                              # 3) определяем длину самой короткой строки
    min = len (x[0])
    for i in x:
        if len(i)<min:
            min=len(i)
    return min

def glasnie (y):                                # 5) приводим гласные к нижнему регистру и выводим их в отсортированном порядке.
    vsegla = set('aeiouy')                      
    y = y.lower ()
    y = set(y)
    glas = sorted(list(y.intersection(vsegla)))
    return glas

def Test_del_znakov_prepinaniya ():
    assert del_znakov_prepinaniya (',tor!twer.') == 'tortwer' , 'Тест провален'
    assert del_znakov_prepinaniya ('?,Y.') == 'Y' , 'Тест провален'

def Test_min_dlina ():
    assert min_dlina (['3','rt','bvvf','as']) == 1 , 'Тест провален' 
    assert min_dlina (['to','st','erot','gad']) == 2 , 'Тест провален'

def Test_glasnie ():
    assert glasnie ('tbAvra') == ['a'] , 'Тест провален'
    assert glasnie ('broEgorTa') == ['a','e','o'] , 'Тест провален'
    assert glasnie ('brgrT') == [] , 'Тест провален'

a = input().split()
znaki_prepinaniya = set(',?.!/;:')
for i in range (len(a)):
    a[i] = del_znakov_prepinaniya(a[i])         # 1)
b=[]
for i in a:
    if i:                                       # 2) удаляем из списка элементы с пустыми строками
        b.append(i)
mini = min_dlina (b)
b=set(b)
b=list(b)
count=0
for i in b:                                     # 4) ищем все строки, длина которых равна самой короткой
    if len(i)==mini:
        glas = glasnie (i)                      # 5)
        if len(glas)==0:                        # 6) проверяем, есть ли гласные хоть в одном из "самых коротких слов"
            pass
        else:
            print (' '.join(glas))              # 7) если гласные есть, выводим их для каждого "самого короткого слова"
            count+=1
if not count:
    print ('Гласных в самом коротком слове нет')
Test_del_znakov_prepinaniya ()
Test_min_dlina ()
Test_glasnie ()
