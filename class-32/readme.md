# Class 32

## Today's Topic
- APIE Part 2

## Study Topics
- Instance Variable, Class Variable

### টপিক ৭৭: এনক্যাপসুলেশন (Encapsulation) – নিরাপত্তার চাদর

Encapsulation মানে হলো ডেটাকে একটি ক্যাপসুলের ভেতরে লুকিয়ে রাখার মতো, যাতে বাইরে থেকে কেউ সরাসরি চেঞ্জ করতে না পারে।
পাইথনে এটি `_` (Protected) এবং `__` (Private) দিয়ে করা হয়।
- **Public**: সবাই এক্সেস করতে পারে (যেমন: `name`)।
- **Protected (_)**: শুধু নিজের ক্লাস এবং সাব-ক্লাস এক্সেস করতে পারে (Convention)।
- **Private (__)**: ক্লাসের বাইরে থেকে একদমই এক্সেস করা যায় না।

#### Public Access:
```python
class Car:
    def __init__(self, make, model):
        # Public attributes
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.make} {self.model} is now at {self.speed} km/h.")

# Creating an object
my_car = Car("Toyota", "Camry")

# Direct access (read and modify) to public attributes is allowed
print(f"Initial Model: {my_car.model}") # Access
my_car.speed = 50                       # Modify
print(f"New Speed: {my_car.speed} km/h")

# Calling a public method
my_car.accelerate(10)
```

#### Protected Method:
```python
class Company:
    def __init__(self, name, budget):
        self.name = name
        # Protected attribute (convention: intended for internal use)
        self._annual_budget = budget

    def get_budget(self):
        return self._annual_budget

    def _internal_audit(self):
        # Protected method (convention: intended for internal use)
        print(f"Performing internal audit for {self.name}...")

# Creating an object
tech_co = Company("TechCorp", 1000000)

# Accessing the budget through a public method (the *recommended* way)
print(f"Company Budget: {tech_co.get_budget()}")

# Direct, *discouraged* access to the protected attribute
print(f"Discouraged direct access: {tech_co._annual_budget}")
tech_co._annual_budget = 1200000 # *Discouraged* direct modification

# Calling the protected method (Discouraged)
tech_co._internal_audit()
```

#### Private Access:
```python
class BankAccount:
    def __init__(self, initial_balance):
        # Private attribute due to name mangling
        self.__balance = initial_balance

    # Public Getter method to read the private attribute
    def get_balance(self):
        return self.__balance

    # Public Setter method to modify the private attribute (with validation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.get_balance()}")
        else:
            print("Deposit amount must be positive.")

# Creating an object
account = BankAccount(500)

# Recommended access via public getter
print(f"Current Balance: {account.get_balance()}")

# Recommended modification via public setter (with controlled logic)
account.deposit(100)
account.deposit(-50) # The validation logic prevents this

# Attempting direct access (will fail)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error accessing private member directly: {e}")

# Accessing via name mangling (possible, but still discouraged)
print(f"Accessing via name mangling: {account._BankAccount__balance}")
```

#### সব উদাহরণ একসাথে:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public
        self.__balance = balance # Private (বাইরে থেকে দেখা যাবে না)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} টাকা জমা হয়েছে।")

    def get_balance(self):
        return self.__balance # সিকিউর ওয়েতে ব্যালেন্স দেখা

acc = BankAccount("Mr. X", 1000)
# acc.__balance = 500000  <-- এটি কাজ করবে না (Error দিবে)
acc.deposit(500)
print(acc.get_balance())
```

#### Getter and Setter Methods
```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute

    # --- 1. The GETTER Method ---
    def get_age(self):
        """Returns the value of the private __age attribute."""
        print("Accessing the age...")
        return self.__age

    # --- 2. The SETTER Method ---
    def set_age(self, new_age):
        """Sets the value of the private __age attribute with validation."""
        if isinstance(new_age, int) and new_age > 0:
            print(f"Age successfully updated to {new_age}.")
            self.__age = new_age
        else:
            print(f"ERROR: Cannot set age to '{new_age}'. Age must be a positive integer.")

# --- Usage ---

# 1. Create the object
student1 = Student("Alice", 20)
print(f"Initial Age: {student1.get_age()}")

print("-" * 20)

# 2. Use the SETTER to modify the value (with success)
student1.set_age(21)

print("-" * 20)

# 3. Use the SETTER to modify the value (with failure due to validation)
student1.set_age(-5)

print("-" * 20)

# 4. Use the GETTER to confirm the current, valid value
print(f"Final Valid Age: {student1.get_age()}")

# 5. Attempting direct access to the private variable will fail
try:
    print(student1.__age)
except AttributeError as e:
    print(f"\nDirect access attempt failed: {e}")
```

### টপিক ৭৮: ইনহেরিট্যান্স (Inheritance) – কোডের বংশগতি

#### ১. তাত্ত্বিক ধারণা (Theoretical Concept)
ইনহেরিট্যান্স (Inheritance) অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)-এর অন্যতম শক্তিশালী একটি স্তম্ভ। সহজ কথায়, এটি হলো "উত্তরাধিকার সূত্রে বৈশিষ্ট্য পাওয়া"।

বাস্তব জীবনে যেমন সন্তান তার বাবা-মায়ের ডিএনএ বা গুণাবলী (যেমন– চোখের রঙ, উচ্চতা) পেয়ে থাকে, তেমনি প্রোগ্রামিংয়ে একটি নতুন ক্লাস (Child Class) তৈরি করার সময় আমরা বিদ্যমান একটি পুরনো ক্লাসের (Parent Class) সব বৈশিষ্ট্য ও মেথডগুলো নিয়ে নিতে পারি।

**কেন ইনহেরিট্যান্স ব্যবহার করব?**
- **DRY Principle (Don't Repeat Yourself)**: একই কোড বারবার লেখার প্রয়োজন হয় না। প্যারেন্ট ক্লাসে একবার কোড লিখলে চাইল্ড ক্লাসে তা অটোমেটিক চলে আসে।
- **Code Reusability**: আগের লেখা কোড পুনরায় ব্যবহার করা যায়।
- **Relationship**: এটি ক্লাসগুলোর মধ্যে সম্পর্ক তৈরি করে (Parent-Child Relationship)।

#### ২. মূল পরিভাষা (Key Terms)
- **Parent Class (Base Class/Super Class)**: যে class থেকে বৈশিষ্ট্য নেওয়া হয়।
- **Child Class (Derived Class/Sub Class)**: যে class-টি বৈশিষ্ট্য গ্রহণ করে।

#### ৩. উদাহরণ ও ব্যাখ্যা
##### উদাহরণ ১: সাধারণ ইনহেরিট্যান্স
ধরি, আমাদের একটি `Vehicle` (যানবাহন) ক্লাস আছে। সব যানবাহনেরই ব্র্যান্ড এবং মডেল থাকে। এখন আমরা যদি `Car` নামে নতুন ক্লাস বানাই, তবে ব্র্যান্ড ও মডেলের কোড পুনরায় লেখার দরকার নেই।

```python
# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}-এর ইঞ্জিন চালু হয়েছে...")

# Child Class (Vehicle কে ইনহেরিট করছে)
class Car(Vehicle):
    def honk(self):
        print("পিপ পিপ!")

# অবজেক্ট তৈরি
my_car = Car("Toyota", "Corolla")

# প্যারেন্ট ক্লাসের মেথড ব্যবহার
my_car.start_engine()  # আউটপুট: Toyota Corolla-এর ইঞ্জিন চালু হয়েছে...

# নিজের মেথড ব্যবহার
my_car.honk()          # আউটপুট: পিপ পিপ!
```

**ব্যাখ্যা**: `Car` ক্লাসের ভেতরে `start_engine` মেথড লেখা নেই, তবুও সে এটি ব্যবহার করতে পারছে কারণ সে `Vehicle` এর সন্তান।

##### উদাহরণ ২: `super()` এর ব্যবহার (অ্যাডভান্সড)
অনেক সময় চাইল্ড ক্লাসে নিজস্ব কিছু অতিরিক্ত বৈশিষ্ট্য যোগ করতে হয়। তখন `super()` ফাংশন ব্যবহার করে প্যারেন্ট ক্লাসের ইনিশিয়ালাইজার কল করা হয়।

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        # প্যারেন্ট ক্লাসের name সেট করার দায়িত্ব super() কে দেওয়া হলো
        super().__init__(name)
        self.student_id = student_id  # নতুন বৈশিষ্ট্য

s1 = Student("Rahim", 101)
print(f"Name: {s1.name}, ID: {s1.student_id}")
```

### টপিক ৭৯: পলিমরফিজম (Polymorphism) – এক নামের বহু রূপ

#### ১. তাত্ত্বিক ধারণা (Theoretical Concept)
পলিমরফিজম শব্দটি গ্রিক শব্দ থেকে এসেছে। 'Poly' মানে অনেক (Many) এবং 'Morph' মানে রূপ (Form)। অর্থাৎ, "বহুরূপিতা"।

প্রোগ্রামিংয়ের ভাষায়, যখন একটি মেথড বা ফাংশন ভিন্ন ভিন্ন ক্লাসে বা ভিন্ন পরিস্থিতিতে ভিন্ন ভিন্ন আচরণ করে, তাকে পলিমরফিজম বলে।

**বাস্তব জীবনের উদাহরণ:**
- ধরুন, "বাজানো" একটি কাজ।
- আপনি যখন বাঁশি বাজান, তখন এক রকম শব্দ হয়।
- যখন গিটার বাজান, তখন অন্য রকম শব্দ হয়।
- কাজ একটাই ("বাজানো"), কিন্তু যন্ত্রভেদে ফলাফল ভিন্ন। এটাই পলিমরফিজম।

#### ২. মেথড ওভাররাইডিং (Method Overriding)
পলিমরফিজমের সবচেয়ে বড় উদাহরণ হলো মেথড ওভাররাইডিং। যখন প্যারেন্ট ক্লাসে একটি মেথড থাকে, কিন্তু চাইল্ড ক্লাস সেই মেথডটিকে নিজের মতো করে পরিবর্তন করে নেয়, তখন তাকে মেথড ওভাররাইডিং বলে।

#### ৩. উদাহরণ ও ব্যাখ্যা
##### উদাহরণ ১: বিভিন্ন প্রাণীর ডাক (ক্লাসিক উদাহরণ)
```python
# Parent Class
class Animal:
    def speak(self):
        print("প্রাণীটি শব্দ করছে...")  # ডিফল্ট আচরণ

# Child Class 1
class Dog(Animal):
    def speak(self):  # মেথড ওভাররাইডিং (পলিমরফিজম)
        print("ঘেউ ঘেউ!")

# Child Class 2
class Cat(Animal):
    def speak(self):  # মেথড ওভাররাইডিং
        print("মিউ মিউ!")

# ব্যবহার
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()

# আউটপুট:
# ঘেউ ঘেউ!
# মিউ মিউ!
# প্রাণীটি শব্দ করছে...
```

**ব্যাখ্যা**: সবার মেথডের নাম `speak()`, কিন্তু `Dog` ক্লাসের জন্য এটি একভাবে কাজ করছে এবং `Cat` ক্লাসের জন্য অন্যভাবে।

##### উদাহরণ ২: শেইপ বা আকৃতির ক্ষেত্রফল (বাস্তব প্রজেক্ট উদাহরণ)
ধরি, আমাদের বিভিন্ন জ্যামিতিক আকৃতি আছে। সব আকৃতিরই `area()` বা ক্ষেত্রফল বের করার পদ্ধতি আছে, কিন্তু সূত্র ভিন্ন।

```python
import math

class Shape:
    def area(self):
        pass # খালি রাখা হলো, চাইল্ড ক্লাস এটি পূরণ করবে

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# পলিমরফিজম টেস্ট
shapes = [Circle(5), Rectangle(4, 6)]

for x in shapes:
    print(f"Area: {x.area():.2f}")

# আউটপুট:
# Area: 78.54
# Area: 24.00
```

##### উদাহরণ ৩: বিল্ট-ইন পলিমরফিজম
পাইথনের `len()` ফাংশন বা `+` অপারেটরও পলিমরফিজমের উদাহরণ।

```python
# প্লাস (+) অপারেটর সংখ্যার ক্ষেত্রে যোগ করে
print(10 + 20)  # আউটপুট: 30

# প্লাস (+) অপারেটর স্ট্রিংয়ের ক্ষেত্রে জোড়া লাগায় (Concatenation)
print("Hello" + " World")  # আউটপুট: Hello World
```

এখানে `+` চিহ্নটি পরিস্থিতির ওপর ভিত্তি করে নিজের রূপ বা কাজ বদলে ফেলেছে।

> **Inheritance**: "বাবা ধনী হলে সন্তান যেমন অটোমেটিক সম্পদের মালিক হয়, ইনহেরিট্যান্সে চাইল্ড ক্লাস প্যারেন্টের কোডের মালিক হয়।"
>
> **Polymorphism**: "আপনার মোবাইল ফোনের পাওয়ার বাটনটি ভাবুন। কল আসলে চাপলে কল রিসিভ হয়, আর কল চলাকালীন চাপলে কল কেটে যায়। বাটন একটাই, কিন্তু পরিস্থিতি অনুযায়ী কাজ ভিন্ন—এটাই পলিমরফিজম।"

### টপিক ৮০: মাল্টিপল ইনহেরিট্যান্স ও MRO (Multiple Inheritance & MRO)

মাল্টিপল ইনহেরিট্যান্স হলো এমন একটি ব্যবস্থা যেখানে একটি চাইল্ড ক্লাস (Child Class) একাধিক প্যারেন্ট ক্লাস (Parent Class) থেকে বৈশিষ্ট্য বা মেথড উত্তরাধিকার সূত্রে পায়। অর্থাৎ, সন্তানের বাবা এবং মা উভয়ের গুণাবলীই থাকবে।

তবে সমস্যা দেখা দেয় যখন বাবা এবং মা—উভয়ের কাছেই একই নামের মেথড থাকে। তখন পাইথন কনফিউজড হতে পারে যে কার মেথডটি কল করবে। এই সমস্যার সমাধান দেয় MRO (Method Resolution Order)।

#### উদাহরণ ১: বেসিক মাল্টিপল ইনহেরিট্যান্স
নিচের উদাহরণে `Child` ক্লাস `Father` এবং `Mother` দুটি ক্লাসকেই ইনহেরিট করেছে।
```python
class Father:
    def gardening(self):
        print("বাবার বাগান করার শখ আছে।")

class Mother:
    def cooking(self):
        print("মা খুব ভালো রান্না করেন।")

class Child(Father, Mother):
    def sports(self):
        print("সন্তান খেলাধুলা পছন্দ করে।")

# অবজেক্ট তৈরি
c = Child()

c.gardening() # বাবার মেথড কল হবে
c.cooking()   # মায়ের মেথড কল হবে
c.sports()    # নিজের মেথড কল হবে
```

#### উদাহরণ ২: মেথড কনফ্লিক্ট এবং MRO এর জাদুকরী ভূমিকা
ধরুন, বাবা এবং মা দুজনেরই `gift()` নামে একটি মেথড আছে। সন্তান যখন `gift()` চাইবে, সে কার কাছ থেকে পাবে?

এখানে পাইথন বাম থেকে ডানে (Left to Right) এবং নিচ থেকে উপরে (Bottom to Up) নীতি অনুসরণ করে। একেই MRO বলে।

```python
class Father:
    def gift(self):
        print("বাবা গিফট হিসেবে একটি সাইকেল দিলেন।")

class Mother:
    def gift(self):
        print("মা গিফট হিসেবে একটি ল্যাপটপ দিলেন।")

# এখানে Father ক্লাসটি বাম পাশে আছে
class Child(Father, Mother): 
    pass

c = Child()
c.gift() 
# আউটপুট: বাবা গিফট হিসেবে একটি সাইকেল দিলেন।
```

**ব্যাখ্যা**: যেহেতু `class Child(Father, Mother):` লিখা হয়েছে এবং `Father` বামে আছে, তাই পাইথন আগে বাবার ক্লাসে gift খুঁজবে। যদি সেখানে না পেত, তবে মায়ের ক্লাসে খুঁজত।

যদি আমরা `class Child(Mother, Father):` লিখতাম, তবে মায়ের মেথডটি আগে কল হতো।

#### MRO চেক করার উপায়
আপনি কোডের মাধ্যমে দেখতে পারেন পাইথন কোন অর্ডারে মেথড খুঁজবে। এর জন্য `mro()` মেথড বা `__mro__` অ্যাট্রিবিউট ব্যবহার করা হয়।
```python
print(Child.mro())
# অথবা
# print(Child.__mro__)
```

আউটপুট হবে: `[Child, Father, Mother, object]`। এর মানে পাইথন প্রথমে `Child`-এ খুঁজবে, তারপর `Father`-এ, তারপর `Mother`-এ, এবং শেষে `object` ক্লাসে (যা সব ক্লাসের মূল)।

### টপিক ৮১: অ্যাবস্ট্রাকশন (Abstraction)

অ্যাবস্ট্রাকশন মানে হলো জটিলতা লুকিয়ে রাখা এবং শুধুমাত্র প্রয়োজনীয় অংশ ব্যবহারকারীর সামনে তুলে ধরা।

**বাস্তব জীবনের উদাহরণ:**
- **ATM মেশিন**: আমরা কার্ড দিই, পিন দিই এবং টাকা পাই। কিন্তু ভেতরে সার্ভারের সাথে কীভাবে যোগাযোগ হচ্ছে বা টাকা কীভাবে গণনা হচ্ছে—তা আমাদের জানার প্রয়োজন নেই।
- **গাড়ি চালানো**: আমরা স্টিয়ারিং ঘুরালে গাড়ি ঘুরে, ব্রেক চাপলে থামে। কিন্তু ভেতরে ইঞ্জিনের পিস্টন কীভাবে কাজ করছে তা ড্রাইভারের জানার দরকার নেই।

প্রোগ্রামিংয়ে, আমরা Abstract Base Class (ABC) ব্যবহার করি একটি টেমপ্লেট বা নিয়ম তৈরি করার জন্য।

**কেন ব্যবহার করবো?**
ধরুন আপনি একটি গেম বানাচ্ছেন যেখানে অনেক ধরনের শত্রু (Enemy) আছে। সব শত্রুরই `attack()` করার ক্ষমতা থাকতে হবে। আপনি একটি অ্যাবস্ট্রাক্ট ক্লাস বানিয়ে নিয়ম করে দিতে পারেন যে, কেউ যদি `Enemy` ক্লাসকে ইনহেরিট করে, তবে তাকে অবশ্যই `attack()` মেথড বানাতেই হবে। না বানালে এরর দিবে।

#### উদাহরণ ১: পেমেন্ট সিস্টেম (বাস্তবমুখী উদাহরণ)
ধরুন আপনার একটি শপ আছে যেখানে বিকাশ এবং নগদে পেমেন্ট নেওয়া হয়।

```python
from abc import ABC, abstractmethod

# এটি আমাদের ব্লু-প্রিন্ট বা টেমপ্লেট
class PaymentSystem(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass  # এখানে কোড লেখার দরকার নেই, শুধু নিয়ম বানালাম
    
    def receipt(self):
        print("পেমেন্ট রিসিট তৈরি হচ্ছে...") # সাধারণ মেথডও থাকতে পারে

# বিকাশ ক্লাস
class Bkash(PaymentSystem):
    def pay(self, amount):
        print(f"বিকাশ দিয়ে {amount} টাকা পেমেন্ট করা হলো।")

# নগদ ক্লাস
class Nagad(PaymentSystem):
    def pay(self, amount):
        print(f"নগদ দিয়ে {amount} টাকা পেমেন্ট করা হলো।")

# ব্যবহার
user1 = Bkash()
user1.pay(500)
user1.receipt()

user2 = Nagad()
user2.pay(1000)
```

#### উদাহরণ ২: জ্যামিতিক শেপ এবং এরর হ্যান্ডলিং
অ্যাবস্ট্রাক্ট মেথড ইমপ্লিমেন্ট না করলে কী হয় তা দেখি।

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # আমরা ইচ্ছা করে area মেথডটি লিখলাম না
    # def area(self):
    #     return 3.1416 * self.radius * self.radius

# অবজেক্ট তৈরির চেষ্টা
# c = Circle(5) 
# এটি রান করলে TypeError দিবে!
# কারণ: Circle ক্লাসটি Shape এর abstract method 'area' ইমপ্লিমেন্ট করেনি।
```

##### সঠিক কোড (ইমপ্লিমেন্টেশন সহ):
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

c = Circle(5)
print(f"বৃত্তের ক্ষেত্রফল: {c.area()}")
```

#### অ্যাবস্ট্রাকশনের মূল নিয়মগুলো মনে রাখুন:
১. অ্যাবস্ট্রাক্ট ক্লাসের (যেমন `Shape` বা `PaymentSystem`) সরাসরি অবজেক্ট তৈরি করা যায় না।
২. চাইল্ড ক্লাসে অবশ্যই `@abstractmethod` যুক্ত মেথডগুলোকে ওভাররাইড (পুনরায় লেখা) করতে হবে।
৩. এটি বড় প্রজেক্টে ডেভেলপারদের একটি নির্দিষ্ট স্ট্রাকচার মেনে চলতে বাধ্য করে।

## HW
1. Class, object, getter and setter method, encapsulation