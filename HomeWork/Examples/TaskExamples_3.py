# Устанавливаем атрибут floor только на чтение

class Elevator:
    def __init__(self, floor = 1):
        self._floor = floor     #  Так как есть '_', то при иницализации __init__ (сразу при создании экземпляра) заходит в getter(@propety),
                                #  а в setter не заходит. Если бы подчеркиания '_' не было, сразу бы искало setter и выдавало ошибку, так как
                                #  setterа нет.
    
    @property
    def floor(self):
        return self._floor     # '_' - обязательно ставить перед floor
    
e = Elevator(50)
print(e.floor) 

# для floor можно задавать значение при условии, что это значение не превысит 10

#class Elevator:
    #def __init__(self, floor = 1):
        #self.floor = floor         #   Если поставить '_',то при иницализации __init__ (сразу при создании экземпляра) в setter не зайдет.
                                    #   и позволит установить для floor любое значение. После этого всегда будет заходить в setter.
                                    #       floor без подчеркивания '_' сразу заходит в setter, что и требуется

    #@property
    #def floor(self):
        #return self._floor

    #@floor.setter
    #def floor(self, value):
        #if value > 10:
            #raise ValueError('Так нельзя')
        #self._floor =  value

