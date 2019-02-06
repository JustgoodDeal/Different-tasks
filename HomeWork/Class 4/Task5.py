# Сжать список, удалив из него все 0 и заполнить
# освободившиеся справа элементы значениями -1.

def compress(s):
    bez_0 = []
    count_0=0
    for i in s:
        if i!=0:
            bez_0.append(i)
        else:
            count_0+=1    
    for i in range(count_0):
        bez_0.append(-1)
    return bez_0

def Test_compress():
    assert compress ([7,9,0,0,6,0,6]) == [7,9,6,6,-1,-1,-1], 'Тест провален'
    assert compress ([0,8,3,8,19,0]) == [8,3,8,19,-1,-1], 'Тест провален'

a = [int (i) for i in input().split()]
bez_0 = compress (a)
print(bez_0)
Test_compress()