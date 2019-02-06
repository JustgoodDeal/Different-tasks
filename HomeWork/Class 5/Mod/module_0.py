def element_count (x):           # Решаем с использованием множества
    mno = set(x)
    mno.discard(' ')
    cort=[]
    for i in mno:
        count = 0
        for j in x:
            if j==i:
                count+=1
        cort.append((i,count))
    itog = sorted(cort, key=lambda tup: tup[1])
    if len (itog)==1:                             # В if/elif рассматриваем случай, если "самых частых" элементов несколько 
        return itog[-1]    
    elif itog[-1][1]==itog[-2][1]:              
        itog2=[]    
        for i, v in enumerate(itog):
                if v[1]==itog[-1][1]:    
                        itog2.append(v)
        itog2 = sorted(itog2, key=lambda tup: tup[0])
        return itog2
    else:
        return itog[-1]

def Test_element_count ():
    assert element_count (['5']) == ('5', 1), 'Тест провален'
    assert element_count (['s','t','o','p','o']) == ('o', 2) , 'Тест провален'
    assert element_count (['r','t','e','a','o']) == [('a', 1),('e', 1),('o', 1),('r', 1),('t', 1)] , 'Тест провален'