class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def set(self,length=None,width=None):
        if length: self._length = length
        if width: self._width = width

    def get(self):
        return self._length, self._width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2*(self._length + self._width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self._length = length

    def area(self):
        return self._length ** 2
