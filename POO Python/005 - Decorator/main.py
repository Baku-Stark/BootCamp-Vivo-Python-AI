class Decorator:
    def __init__(self, x = None) -> None:
        self._x = x

    @property # sem o decorator, o módulo não funciona e evitar uma inserção externa
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value : int):
        self._x += value

foo = Decorator(10)
print(foo.x)

foo.x = 100
print("New value: " + str(foo.x))