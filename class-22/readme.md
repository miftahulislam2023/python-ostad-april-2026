# Class 22

## Today's Topic
- Functions
- parameters
- return values

## Python Functions: A to Z

Python-এ ফাংশন হলো একটি রিইউজেবল (reusable) কোড ব্লক, যা নির্দিষ্ট কোনো কাজ সম্পন্ন করার জন্য তৈরি করা হয়। ফাংশন ব্যবহারের প্রধান সুবিধা হলো কোডের পুনরাবৃত্তি কমানো এবং কোডকে সহজে পরিচালনা করা।

---

## ১. ফাংশন তৈরি এবং কল করার বেসিক সিনট্যাক্স (Basic Syntax)

Python-এ ফাংশন তৈরি করার জন্য `def` কিওয়ার্ড ব্যবহার করা হয়।

### সিনট্যাক্স:

```python
def function_name(parameters):
    """docstring (ঐচ্ছিক)"""
    # ফাংশন বডি / স্টেটমেন্টস
    return value # (ঐচ্ছিক)

```

* **def:** ফাংশন ডিফাইন করার কিওয়ার্ড।
* **function_name:** ফাংশনের নাম (এটি ইউনিক হতে হবে)।
* **parameters:** ফাংশনে পাস করা ভেরিয়েবল (ঐচ্ছিক)।
* **docstring:** ফাংশনটি কী কাজ করে তার বিবরণ (ঐচ্ছিক)।
* **return:** ফাংশন থেকে কোনো আউটপুট বা মান ফেরত পাঠানোর জন্য ব্যবহৃত হয়।

---

## ২. ইউজার-ডিফাইন্ড ফাংশন (User-defined Functions)

ব্যবহারকারী নিজের প্রয়োজন অনুযায়ী যে ফাংশন তৈরি করে, তাকে ইউজার-ডিফাইন্ড ফাংশন বলে।

### উদাহরণ ১: প্যারামিটার ছাড়া সাধারণ ফাংশন

```python
def greet_user():
    print("Python প্রোগ্রামিংয়ে আপনাকে স্বাগতম।")

# ফাংশন কল
greet_user()

```

### উদাহরণ ২: প্যারামিটারসহ ফাংশন

```python
def calculate_area(length, width):
    area = length * width
    print("আয়তক্ষেত্রের ক্ষেত্রফল:", area)

# ফাংশন কল
calculate_area(10, 5)

```

---

## ৩. আর্গুমেন্ট এবং প্যারামিটারের প্রকারভেদ (Types of Arguments)

ফাংশন ডিক্লেয়ার করার সময় ব্র্যাকেটের ভেতরের ভেরিয়েবলকে **প্যারামিটার (Parameter)** বলে এবং ফাংশন কল করার সময় যে মান পাঠানো হয় তাকে **আর্গুমেন্ট (Argument)** বলে।

### ক) পজিশনাল আর্গুমেন্ট (Positional Arguments)

এই ক্ষেত্রে আর্গুমেন্টগুলো সঠিক ক্রমানুসারে পাস করতে হয়।

#### উদাহরণ ১:

```python
def display_info(name, age):
    print(f"নাম: {name}, বয়স: {age}")

# সঠিক ক্রমানুসারে আর্গুমেন্ট পাস
display_info("রাকিব", 25)

```

#### উদাহরণ ২:

```python
def subtract_numbers(a, b):
    return a - b

# পজিশন পরিবর্তন হলে আউটপুট বদলে যাবে
result = subtract_numbers(20, 5)
print("বিয়োগফল:", result)

```

### খ) কিওয়ার্ড আর্গুমেন্ট (Keyword Arguments)

এই পদ্ধতিতে আর্গুমেন্ট পাস করার সময় প্যারামিটারের নাম উল্লেখ করে দেওয়া হয়। ফলে ক্রমানুসারে না লিখলেও সমস্যা হয় can।

#### উদাহরণ ১:

```python
def display_info(name, age):
    print(f"নাম: {name}, বয়স: {age}")

# ক্রমানুসারে না লিখে নাম উল্লেখ করে পাস করা
display_info(age=30, name="আরিফ")

```

#### উদাহরণ ২:

```python
def introduction(country, city):
    print(f"আমি {country}-এর {city} শহরে থাকি।")

introduction(city="ঢাকা", country="বাংলাদেশ")

```

### গ) ডিফল্ট আর্গুমেন্ট (Default Arguments)

যদি ফাংশন কল করার সময় কোনো আর্গুমেন্ট না দেওয়া হয়, তবে ফাংশনটি তার ডিফল্ট মান ব্যবহার করে।

#### উদাহরণ ১:

```python
def greet(name="ইউজার"):
    print(f"হ্যালো {name}!")

# আর্গুমেন্ট ছাড়া কল
greet()
# আর্গুমেন্টসহ কল
greet("সাকিব")

```

#### উদাহরণ ২:

```python
def calculate_bill(price, tax=0.05):
    total = price + (price * tax)
    return total

print("ডিফল্ট ট্যাক্সসহ বিল:", calculate_bill(100))
print("কাস্টম ট্যাক্সসহ বিল:", calculate_bill(100, 0.10))

```

### ঘ) আর্বিট্রারি আর্গুমেন্ট (Arbitrary Arguments - *args)

যখন ফাংশনে কতটি আর্গুমেন্ট পাস করা হবে তা আগে থেকে জানা থাকে না, তখন প্যারামিটারের আগে একটি স্টার `*` চিহ্ন ব্যবহার করা হয়। এটি ডেটাগুলোকে টাপল (Tuple) হিসেবে গ্রহণ করে।

#### উদাহরণ ১:

```python
def sum_all_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("যোগফল:", sum_all_numbers(10, 20, 30, 40))

```

#### উদাহরণ ২:

```python
def show_fruits(*fruits):
    for fruit in fruits:
        print("ফলের নাম:", fruit)

show_fruits("আম", "কলা", "লিচু")

```

### ঙ) আর্বিট্রারি কিওয়ার্ড আর্গুমেন্ট (Arbitrary Keyword Arguments - kwargs)

যখন ফাংশনে কতটি কিওয়ার্ড আর্গুমেন্ট পাস করা হবে তা জানা থাকে না, তখন দুটি স্টার `` চিহ্ন ব্যবহার করা হয়। এটি ডেটাগুলোকে ডিকশনারি (Dictionary) হিসেবে গ্রহণ করে।

#### উদাহরণ ১:

```python
def show_user_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_user_details(Name="তামিম", Age=35, Profession="Cricketer")

```

#### উদাহরণ ২:

```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile("নাহিদ", "হাসান", location="রাজশাহী", hobby="কোডিং")
print(profile)

```

---

## ৪. রিটার্ন স্টেটমেন্ট (The return Statement)

ফাংশন থেকে কোনো ফলাফল বা মান মেইন প্রোগ্রামে ফেরত পাঠানোর জন্য `return` ব্যবহার করা হয়। `return` এক্সিকিউট হওয়ার পর ফাংশনের কাজ শেষ হয়ে যায়।

### উদাহরণ ১: একক মান রিটার্ন করা

```python
def square(number):
    return number * number

result = square(5)
print("বর্গফল:", result)

```

### উদাহরণ ২: একাধিক মান রিটার্ন করা (Tuple আকারে)

```python
def get_min_max(numbers):
    low = min(numbers)
    high = max(numbers)
    return low, high  # একাধিক মান রিটার্ন

minimum, maximum = get_min_max([12, 45, 2, 67, 8])
print("সর্বনিম্ন:", minimum, "সর্বোচ্চ:", maximum)

```

---

## ৫. ভেরিয়েবলের স্কোপ (Scope of Variables)

ফাংশনের ভেতরে এবং বাইরে ভেরিয়েবলের দৃশ্যমানতা বা কার্যকারিতাকে স্কোপ বলে।

### ক) লোকাল স্কোপ (Local Scope)

ফাংশনের ভেতরে ডিক্লেয়ার করা ভেরিয়েবল কেবল সেই ফাংশনের ভেতরেই কাজ করে।

#### উদাহরণ ১:

```python
def my_function():
    local_var = 50  # লোকাল ভেরিয়েবল
    print("ফাংশনের ভেতর থেকে:", local_var)

my_function()
# ফাংশনের বাইরে প্রিন্ট করতে গেলে Error আসবে
# print(local_var) 

```

#### উদাহরণ ২:

```python
def calculate_salary(basic):
    allowance = 5000  # লোকাল ভেরিয়েবল
    return basic + allowance

print("মোট বেতন:", calculate_salary(30000))

```

### খ) গ্লোবাল স্কোপ (Global Scope)

ফাংশনের বাইরে ডিক্লেয়ার করা ভেরিয়েবল যেকোনো স্থান থেকে অ্যাক্সেস করা যায়। ফাংশনের ভেতরে গ্লোবাল ভেরিয়েবল পরিবর্তন করতে `global` কিওয়ার্ড ব্যবহার করতে হয়।

#### উদাহরণ ১: গ্লোবাল ভেরিয়েবল অ্যাক্সেস করা

```python
global_var = 100  # গ্লোবাল ভেরিয়েবল

def read_global():
    print("ফাংশনের ভেতর থেকে গ্লোবাল ভেরিয়েবল:", global_var)

read_global()
print("ফাংশনের বাইরে থেকে গ্লোবাল ভেরিয়েবল:", global_var)

```

#### উদাহরণ ২: `global` কিওয়ার্ড ব্যবহার করে মান পরিবর্তন

```python
counter = 0

def increment():
    global counter  # গ্লোবাল ভেরিয়েবল ব্যবহারের ঘোষণা
    counter += 1

increment()
increment()
print("কাউন্টার বর্তমান মান:", counter)

```

---

## ৬. ল্যাম্বডা ফাংশন (Lambda Function / Anonymous Function)

নামহীন বা একক লাইনের ছোট ফাংশনকে ল্যাম্বডা ফাংশন বলা হয়। এটি তৈরি করতে `lambda` কিওয়ার্ড ব্যবহার করা হয়।

### সিনট্যাক্স:

```python
lambda arguments: expression

```

### উদাহরণ ১: দুটি সংখ্যার যোগফল নির্ণয়

```python
add = lambda a, b: a + b

print("ল্যাম্বডা ফাংশনের যোগফল:", add(15, 25))

```

### উদাহরণ ২: সংখ্যার জোর-বিজোড় পরীক্ষা (Conditional Expression)

```python
check_even = lambda x: "জোড়" if x % 2 == 0 else "বিজোড়"

print("৮ সংখ্যাটি:", check_even(8))
print("৭ সংখ্যাটি:", check_even(7))

```

---

## ৭. ডকস্ট্রিং (Docstrings)

ফাংশনটি কী উদ্দেশ্যে তৈরি করা হয়েছে তা ব্যাখ্যা করার জন্য ট্রিপল কোটেশন (`"""`) ব্যবহার করে ডকস্ট্রিং লেখা হয়। এটি কোডের রিডাবিলিটি বাড়ায়।

### উদাহরণ ১:

```python
def multiply(a, b):
    """
    এই ফাংশনটি দুটি সংখ্যার গুণফল রিটার্ন করে।
    আর্গুমেন্ট: a (int/float), b (int/float)
    রিটার্ন: গুণফল
    """
    return a * b

# ডকস্ট্রিং প্রিন্ট করা
print(multiply.__doc__)

```

### উদাহরণ ২:

```python
def is_prime(n):
    """একটি সংখ্যা মৌলিক কিনা তা যাচাই করে।"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime.__doc__)

```