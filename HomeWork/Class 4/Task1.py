# Определить, является ли введенное слово идентификатором, т.е. начинается ли оно
# с английской буквы в любом регистре или знака подчеркивания и не содержит других символов, 
# кроме букв английского алфавита (в любом регистре), цифр и знака подчеркивания.


def identificator (word):
    a = 'abcdefghijklmnopqrstuvwxyz_'
    b = a.upper()
    begin = set(a).union(set(b))
    contin = begin.union(set('0123456789'))
    c = word[0:1]
    if c not in begin:
        return 0
    else:
        d = set(word)
        if d.issubset(contin):
            return 1 
        else:
            return 0
   
def Test_identificator ():
    assert identificator('4fghgfh') == 0 , 'Тест провален'
    assert identificator('_ssdads') == 1 , 'Тест провален'
    assert identificator('A!fdg33') == 0 , 'Тест провален'

ide = identificator (input())
if ide:
    print('Идентификатор')
else:
    print('Не идентификатор')
Test_identificator ()