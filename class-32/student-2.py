class Student:
    def __init__(self, name, roll):
        self._name = name
        self.roll = roll

    def introduce(self):
        print(f"আমি {self.name}, আমার আইডি {self.roll}")

student1 = Student("Miftahul Islam", "1")

student1._name = "Abdullah"

print(student1.__name)