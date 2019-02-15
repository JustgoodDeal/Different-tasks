# Реализовать модуль, содержащий следующие функции декораторы:
# 1.декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
# 2. декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
# 3. декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
# 4. декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
import Module_for_Task0

argument1 = ['Wow',3,'Next']
argument2 = 'Hi' 
argument3 = "Let's go"  

@Module_for_Task0.args_type
@Module_for_Task0.time_work
@Module_for_Task0.time_name
def printer (*args,**kwargs):
    print (args,kwargs)
printer(argument1, argument2)

def printer_add (*args,**kwargs):
    print ('\n'+str(args)+str(kwargs)+'  !!!!!')
printer_add = Module_for_Task0.cash (printer_add)
try:
    printer_add (argument3)
except TypeError:
    print('\nТак как аргументы декорируемой функции не поддерживают хеширование, результат работы функции не был кэширован')






