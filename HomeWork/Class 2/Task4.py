# Запросить у пользователя строку. В строке должна содержаться минимум одна цифра.
#  Если цифры в введенной строке нет, завершить программу с сообщением об отсуствии цифры.
#  Если строка введена правильно запросить у пользователя цифру.
#  Результатом работы программы должно быть сообщение есть искомая цифра в исходной строке или нет.

def number_presence (stroka, tsifra):
    spi = list(stroka)
    spi2=[]    
    i=-1
    while i < len(spi)-1:                   # Рассматриваем вариант, при котором в заданной строке несколько чисел подряд образуют одно число.
        i+=1                                # Например, в строке "абв 246" нет числа 246, а есть отдельностоящие 2, 4 и 6.  
        if spi[i] in mnojestvo_iz_chisel:                     # Теперь же программа выведет ответ "Цифра есть", если пользователь введет 2, 4, 6 либо 246 
            spi2.append(spi[i])
            for j in range (i+1,len(spi)):
                if spi[j] in mnojestvo_iz_chisel:
                    spi2.append(spi[j])
                    if j==len(spi)-1:
                        i = j
                else:
                    spi2.append(' ')
                    i = j
                    break
    spi2=''.join(spi2)
    spi2=spi2.split()
    mno2 = set (spi2)
    mnojestvo.update(mno2)
    if tsifra in mnojestvo:
        return 0
    else:
        return 1

def Test_number_presence ():
    assert number_presence ('sdaasddsa88' , '88') == 0 , 'Тест провален'
    assert number_presence ('1tuo8cxv !%' , '8') == 0 , 'Тест провален'
    assert number_presence ('3tuo8cxv !%' , '89') == 1 , 'Тест провален'
    
stroka = input()
mnojestvo_iz_chisel = {'0','1','2','3','4','5','6','7','8','9'}
mnojestvo = set (stroka)
if len(mnojestvo.intersection(mnojestvo_iz_chisel))==0:
    print('Изначально цифры не было')    
else:
    tsifra = input()
    num = number_presence (stroka, tsifra)
    if num:
        print('Цифры нет')
    else:
        print('Цифра есть')
Test_number_presence ()










