class Student:
    def __init__(self, name, roll):
        self._name = name
        self.roll = roll

    def introduce(self):
        print(f"আমি {self.name}, আমার আইডি {self.roll}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

student1 = Student("Miftahul Islam", "1")

print(student1.get_name())
student1.set_name("Abdullah")