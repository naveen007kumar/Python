class Animal:

    isalive = True

    def eating(self):
        print("This animal is eating")

    def sleeping(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    pass
class Elephant(Animal):
    pass
class Lion(Animal):
    pass

rabbit = Rabbit()
elep = Elephant()
leo = Lion()

print(rabbit.isalive)
elep.eating()
leo.sleeping()