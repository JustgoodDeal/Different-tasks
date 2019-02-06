# Пользователь вводит строку и символ. В строке найти все вхождения
# этого символа и перевести его в верхний регистр, а также удалить часть строки, 
# начиная с последнего вхождения этого символа и до конца.

def up_grade (x,y):
    niz = y.lower()
    verx = y.upper()
    if niz not in x and verx not in x:
        return x
    last=0
    last2=0
    if niz in x:
        last = x.rfind(niz)
    if verx in x:
        last2 = x.rfind(verx)
    if last>last2:
        last3=last
    else:
        last3=last2
    c = list(x)
    for i in range (len(c)):
        if c[i] == niz: 
            c[i] = c[i].upper()
    grade = c[0:last3]
    tt=''.join(grade)
    return tt

def Test_up_grade():
    assert up_grade ('tre4fg sa','g') == 'tre4f', 'Тест провален'
    assert up_grade ('Life is my love','i') == 'LIfe ', 'Тест провален'
    assert up_grade ('BestMe to dor','R') == 'BestMe to do', 'Тест провален'

a = input()
b = input()
tt = up_grade (a,b)
print(tt)
Test_up_grade()