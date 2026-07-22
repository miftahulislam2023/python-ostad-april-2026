class GrandFather:
    def farming(self):
        print("Grand Father is farming.")

    def nick_name(self):
        print("Abdul Matin")

class Father(GrandFather):
    def gardening(self):
        print("বাবার বাগান করার শখ আছে।")
    
    def nick_name(self):
        print("Abdullah")

class Mother(GrandFather):
    def cooking(self):
        print("মা খুব ভালো রান্না করেন।")
    
    def nick_name(self):
        print("Saifullah")

class Child(Mother, Father):
    def sports(self):
        print("সন্তান খেলাধুলা পছন্দ করে।")

    def nick_name(self):
        print("Argentina")

child1 = Child()

child1.nick_name()

print(Child.mro())