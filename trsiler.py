class Person:
    age = 25

    @classmethod
    def printAge(cls):
        print('The age is:',cls.age)

P = Person()
P.printAge()