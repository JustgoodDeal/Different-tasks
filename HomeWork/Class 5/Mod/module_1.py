def srednee_arif(A,N):
    sum = 0
    for i in A:
        for j in i:
            sum+=j
    srednee = sum/(N*N)
    return srednee

def Test_srednee_arif ():
    assert srednee_arif ([[4,10,3],[7,-3,-5],[4,-8,6]],3)== 2.0 ,'Тест провален'
    assert srednee_arif ([[5,8,-3],[9,-5,3],[8,-2,4]],3)== 3.0 ,'Тест провален'