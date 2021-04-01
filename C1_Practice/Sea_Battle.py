class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class BoardException(Exception):
    pass
class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы доски"
class BoardUsedException(BoardOutException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"
class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self, coor, l, orientation):
        self.coor = coor
        self.l = l
        self.orientation = orientation
        self.life = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            coor_x = self.coor.x
            coor_y = self.coor.y
            if self.orientation == 0:
                coor_x += 1
            elif self.orientation == 1:
                coor_y += 1
            ship_dots.append(Dot(coor_x, coor_y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid

        self.count = 0
        self.field = [["0"]*size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        res = ""
        res += "|1|2|3|4|5|6|"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " | "
        if self.hid:
            res = res.replace("■", "0")

b = Board()
print(b)