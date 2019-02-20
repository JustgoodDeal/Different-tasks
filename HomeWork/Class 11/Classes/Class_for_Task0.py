class Quadrate:
    def __init__(self, side_1):
        self.side_1 = side_1
    def perimetr(self):
        sum = self.side_1 * 4
        return sum
    def square(self):
        ploshad = self.side_1 ** 2
        return ploshad
    def volume (self):
        try:
            raise Exception ('Возникла проблема!!!\n')
        except Exception as e:
            return str(e) + 'У данной фигуры нет объема'

class Rectangle(Quadrate):
    def __init__(self, side_1, side_2):
        super().__init__(side_1)
        self.side_2 = side_2
    def perimetr(self):
        sum = (self.side_1 + self.side_2) * 2
        return sum
    def square(self):
        ploshad = self.side_1 * self.side_2
        return ploshad

class Triangle(Rectangle):
    def __init__(self, side_1, side_2, side_3):
        super().__init__(side_1, side_2)
        self.side_3 = side_3
    def perimetr(self):
        sum = self.side_1 + self.side_2 + self.side_3
        return sum
    def square(self):
        p = (self.side_1 + self.side_2 + self.side_3)/2
        kva = p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3)
        ploshad = kva**.5
        return ploshad

class Trapeze(Triangle):
    def __init__(self, side_1, side_2, side_3, side_4):
        super().__init__(side_1, side_2, side_3)
        self.side_4 = side_4
    def perimetr(self):
        sum = self.side_1 + self.side_2 + self.side_3 + + self.side_4
        return sum
    def square(self): 
        if self.side_1 == self.side_2:
            return 'Данная фигура не является трапецией'
        else:
            kva = self.side_3**2 - (((self.side_2 - self.side_1)**2 + self.side_3**2 - self.side_4**2)/(2*(self.side_2 - self.side_1)))**2       
            ploshad = kva**.5 * (self.side_1 + self.side_2)/2
        return ploshad

