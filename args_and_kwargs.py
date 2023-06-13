def add(*args):
    sum_of_number = 0
    for n in args:
        sum_of_number += n
    print(sum_of_number)


add(2, 6, 4, 6, 7, 6, 435356, 443,)

# **kwargs example


def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)

    n *= kwargs["mul"]
    print(n)


calculate(2, add=98, mul=10)

# initializes **kw using class


class Car():
    def __init__(self, **kw):   
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


car = Car(make="nissan", model="GT - R", color="balck")
print(car.model)
