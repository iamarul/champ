__author__ = 'arul'


class Myclass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class calci(Myclass):
    def mul(self):
        return self.b * self.a

x = calci(4, 6)
print x.add()
print x.mul()