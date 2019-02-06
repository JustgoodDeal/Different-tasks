# Дан список А1..AN. Найти элемент, который чаще всего встречается, вывести его значение и количество повторений.

import Mod.module_0 

a = list (input())
final = Mod.module_0.element_count (a)
if type(final[1]) is int:
    print('Самый частый элемент - "{}"'.format(final[0]) +' . Он встречается '+ str(final[1])+' раз(а)')
else:
    d = final[0][1]
    print('Самые частые элементы, которые встречаются ' + str(d) + ' раз(а):')   
    for i in final:
        print('"{}"'.format(i[0]))
Mod.module_0.Test_element_count ()

