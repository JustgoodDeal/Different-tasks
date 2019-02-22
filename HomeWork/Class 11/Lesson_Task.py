# Написать методы, производящие следующие операции с векторами: сложение, вычитание, умножение; 
# а также методы, осуществляющие проверку на равенство/ не равенство векторов,

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y    
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __ne__(self,other):
        return self.x != other.x or self.y != other.y

a = Vector(5,9)
b = Vector (5,0)
d = Vector(5,9)
c = a*b
print(c.x,c.y)
e = a+b+d
print(e.x,e.y)



