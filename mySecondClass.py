class MySecondClass:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary


if __name__ == '__main__':
    x = MySecondClass(1, -1)
    print(f'({x.r}, {x.i}j)')

