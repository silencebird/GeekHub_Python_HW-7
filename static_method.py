class Person:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last

    @staticmethod
    def isAdult(age):
        return age > 18