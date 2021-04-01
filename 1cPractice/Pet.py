class Pet:
    def __init__(self, name):
        self.name = name
        # self.age = age
        # self.gender = gender

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return '{0} waw'.format(self.name)

dog = Dog("Шарик", "Шпиц")
print(dog.name)
print(dog.breed)

dog = Dog("Бобик")
print(dog.name)
print(dog.breed)
print(dog.say())