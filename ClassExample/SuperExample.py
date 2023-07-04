class Area:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        


class Square(Area):

    def __init__(self, x, y):
        super().__init__(x, y)

    def square(self):
        return self.x * self.y


class Rectangle(Area):
    def __init__(self, x, y, o):
        super().__init__(x, y)
        self.o = o

    def rectangle(self):
        return self.x * self.y * self.o


sqr = Square(5, 5)
rec = Rectangle(3,5,6)


print(sqr.square())
print(rec.rectangle())
