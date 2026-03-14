"""
    Obejct-Oriented Programming Classes:


    class className:

        # instance attribute : self.xxxxx
        # class attribute: xxxx


        # initializer
        def __init__(self, arguments):
            #self.argument1 = ...
            #self.argument2 = ...

        # method
        def functionName(self, arguments):
            #method body
            pass

    create an object:
        objectName = className(arguments)
"""


class Car:

    # class attribute
    wheel = 4

    # initializer
    def __init__(self, c_name, c_age):
        self.name = c_name
        self.age = c_age

    # method
    def car_name(self):
        return self.name

    # magic method
    def __str__(self):
        return f"Car name: {self.name}. Car age: {self.name}"



if __name__ == '__main__':
    car = Car("x56",13)
    print(car)
    print(car.wheel)
    print(car.car_name())
