# Написать программу нахождения простых чисел, используя решето Эратосфена. Для каждой из пользовательских функций написать функцию-тест.

def prostie_chisla (n):
    nums = []
    for i in range (2,n+1):
        for j in nums:
            if i%j==0:
                break
        else:
            nums.append(i)
    return nums    
def Test_prostie_chisla():
    assert prostie_chisla(7) == [2,3,5,7], 'Тест провален'
    assert prostie_chisla(199) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
    97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199], 'Тест провален'    
n = int(input())
easy = prostie_chisla (n)
print(' '.join([str(i) for i in easy]))
Test_prostie_chisla()
