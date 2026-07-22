class Father:
    def gardening(self):
        print("বাবার বাগান করার শখ আছে।")

class Mother:
    def cooking(self):
        print("মা খুব ভালো রান্না করেন।")

class Child(Father, Mother):
    def sports(self):
        print("সন্তান খেলাধুলা পছন্দ করে।")

child1 = Child()

child1.gardening()
child1.cooking()
child1.sports()