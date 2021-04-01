class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_S(self):
        return self.width * self.length



r1 = Rectangle(14,16)
print('Длина:',r1.length, 'Ширина:',r1.width, 'Площадь:', r1.get_S())

r2 = Rectangle(123, 900)
print('Длина:',r2.length, 'Ширина:',r2.width, 'Площадь:', r2.get_S())