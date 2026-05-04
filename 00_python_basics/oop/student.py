class Student:
    def __init__(self, name, age):
        self.name = name # init
        self.age = self.validate_age(age) # validating

    def validate_age(self, age):
        if age > 17 and age < 50:
            self.age = age
        else:
            self.age = 0

    @classmethod
    def getQWE(cls):
        pass

std1 = Student("Jason", 25)
