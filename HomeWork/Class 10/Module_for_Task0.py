import time
import functools

def time_work(func):
    start = time.time()
    def wrapper(*args,**kwargs):        
        func (*args,**kwargs)
        print ('Время работы функции: {}'.format(time.time()-start))
        return func 
    return wrapper

def time_name(func):
    start = time.time()
    def wrapper(*args,**kwargs):
        func (*args,**kwargs)
        with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 10/Files/File_for_Task0.txt",'w') as file:   
            parametr = 'Переданные параметры: {} {}'.format(args,kwargs)      
            function_name = 'Имя функции: {}'.format(func.__name__)
            vremya = 'Время работы функции: {}'.format(time.time()-start)
            file.write (vremya+'\n'+function_name+'\n'+parametr)
        return func
    return wrapper

def args_type(func):
    def wrapper(*args,**kwargs):
        func (*args,**kwargs)
        print('Типы переданных декорируемой функции аргументов:')
        for i in args:
            print(i,type(i))
        for k,v in kwargs.items():
            print(k,type(k))
            print(v,type(v))
        return func
    return wrapper

def cash (func):
    @functools.lru_cache(maxsize=None)
    def wrapper(*args,**kwargs):
        if not wrapper.has_run:             # обеспечивает единственный вызов функции
            wrapper.has_run = True            
            func(*args,**kwargs)
            print('Результат работы функции был успешно кэширован')
        return func
    wrapper.has_run = False        
    return wrapper