class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Ghew ghew")
    def speak(self):
        print("Woof woof")

class Cat(Animal):
    def meow(self):
        print("Meow meow")
    def speak(self):
        print("Meow meow")

dog1 = Dog("Tommy")
cat1 = Cat("Whiskers")

print(dog1.name)
print(cat1.name)

dog1.speak()
dog1.bark()

cat1.speak()
cat1.meow()