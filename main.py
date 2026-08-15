class Box:
    def __init__(self, v):
        self.v = v

    # def __eq__(self, other):
    #     return self.v == other.v

a = Box(10)
b = Box(10)
c = None

print(a==b, c is None)