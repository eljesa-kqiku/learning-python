def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


print(add(1, 2, 46, 45))
print(add(9, 10, 23, 10))


# **kwargs is a dictionary
# use kwargs.get('key') instead of kwargs['key'] to prevent error if data is not set
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculator(3, add=2, multiply=4)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')


car = Car(make='Nissan', color="Black")
print(car.make)  # Nissan
print(car.model)  # None
print(car.color)  # Black
