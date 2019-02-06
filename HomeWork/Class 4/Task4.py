# Начальный вклад в банке равен 1000 BYN. Через каждый месяц размер вклада
# увеличивается на P-процентов (P - вещественное число, 0 < P < 25). 
# Значение P запрашивается у пользователя. По данному P определить, 
# через сколько месяцев размер вклада превысит 1100 BYN и вывести найденное 
# количество месяцев и итоговый размер вклада.

def month_count (vklad, procent):
    month = 0
    while vklad<=1100:
        month+=1
        b = vklad*procent/100
        vklad = vklad+b
        if vklad>1100:
            return month, vklad

def Test_month_count():
    assert month_count (1000, 5) == (2,1102.5), 'Тест провален'
    assert month_count (1000, 10) == (2,1210), 'Тест провален'

start = 1000
P = int(input())
if 0 < P < 25:
    month, vklad = month_count(procent=P,vklad=start)
    if month == 1:
        print ('Через', month, 'месяц, итоговый размер вклада -',vklad, 'BYN')
    elif 2<=month <= 4:
        print ('Через', month, 'месяца, итоговый размер вклада -',vklad, 'BYN')
    else:
        print ('Через', month, 'месяцев, итоговый размер вклада -',vklad, 'BYN')
else:
    print ('Несуществующий процент')
Test_month_count()





