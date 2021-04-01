class Rectangle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Метод, расчитывающий площадь
    def __str__(self):
        return f'x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}'

testRectangle = Rectangle(5, 10, 50, 100)
print(testRectangle)