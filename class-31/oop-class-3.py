class Cat:
    breed = "Persian"
    color = "White"
    age = 5
    
    def sound(self):
        print("Meow")

cat1 = Cat()
cat2 = Cat()

print(cat1.age)
print(cat2.age)

cat1.sound()
cat2.sound()

cat1.age = 3
cat2.color = "brown"

print(cat1.age)
print(cat2.color)