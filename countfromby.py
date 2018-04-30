class CountFromBy:
    def __repr__(self) -> str:
        return str(self.val)

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increse(self) -> None:
        self.val += self.incr

i = CountFromBy()

print(i.val)
print(i.incr)

i.increse()
print(i.val)