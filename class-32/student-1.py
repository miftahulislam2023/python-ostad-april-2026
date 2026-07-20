class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def introduce(self):
        print(f"আমি {self.name}, আমার আইডি {self.roll}")

student1 = Student("Miftahul Islam", "1")

print(student1.name)
print(student1.roll)

student1.introduce()