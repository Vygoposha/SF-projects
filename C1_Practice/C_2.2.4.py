class Square:
    def __init__(self, side):
        self.side = side

    @property
    def get_side(self):
        return self.side

    @property
    def get_square(self):
        return self.side * self.side

    @get_side.setter
    def get_side(self, value):
        if value >= 0:
            return self.side
        raise ValueError('Число должно быть больше 0')

class SquareFactory:
    @staticmethod
    def create_side(side):
        return Square(side)

s1 = SquareFactory.create_side(22)
# print(s1.side, type(s1.side), type(s1))
S1 = Square(10)
print(S1.get_square)
S1.get_side = 20
print(S1.get_square)
