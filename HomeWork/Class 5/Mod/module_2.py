def count_if(A,p1,p2):
    count_sum = 0
    for i in A:
        for j in i:
            if p1<=j<=p2:
                count_sum += 1
    return count_sum


def Test_count_if():
    assert count_if([[4,10,3,6],[8,7,-3,-5],[4,-8,6,-1]],5,15)== 5,'Тест провален'
    assert count_if([[4,10,3,6],[8,7,-3,-5],[4,-8,6,-1]],0,100)== 8,'Тест провален'