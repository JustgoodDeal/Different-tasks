# Реализовать программу с базой учащихся группы (данные хранятся в файле). Записи по учащемуся должны быть представлены 
# отдельным классом с полями: имя, фамилия, пол, возраст. Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи. Скрипт программы должен принимать параметр, 
# который определяет формат хранения и реализации БД: в текстовом файле с определенной структурой; в файле json.

from Classes.Class_for_Task1 import Baza

parametr = input('В файле какого формата хранятся данные: json либо txt ? \n')
parametr2 = input('В файл какого формата записывать результат работы программы: json либо txt ? \n')

if parametr == 'json':
    all_instanses = Baza.open_json()
elif parametr == 'txt':
    all_instanses = Baza.open_txt()

Baza.search_for_men(all_instanses,parametr2)
