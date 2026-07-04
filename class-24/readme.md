# Class 24

## Today's Topic

- Mini Project – Function-based calculator
- Map & Filter

## Higher Order Function

- If a function takes another function as input i.e. argument or parameter or returns a function as a result then it is called a higher order function.
- For example, `map()` and `filter()` are higher order functions.

## Map & Filter

- পাইথনে `map()` এবং `filter()` হলো দুটি অত্যন্ত শক্তিশালী **Built-in Higher-Order Functions**। সহজ কথায়, এগুলো কোনো লিস্ট বা টাপলের মতো ডাটার প্রতিটি উপাদানের ওপর লুপ না চালিয়ে সরাসরি কোনো কাজ করতে সাহায্য করে।

নিচে সহজ উদাহরণসহ এ দুটি ফাংশনের বিস্তারিত আলোচনা করা হলো:

---

### ১. map() ফাংশন

`map()` ফাংশন ব্যবহার করা হয় যখন আপনি কোনো একটি নির্দিষ্ট লিস্ট (বা অন্য কোনো ইটারেবল) এর **প্রতিটি উপাদানের ওপর একই কাজ বা অপারেশন** চালাতে চান এবং ফলাফল হিসেবে একটি নতুন লিস্ট (বা ম্যাপ অবজেক্ট) পেতে চান।

#### সিনট্যাক্স:

```python
map(function, iterable)

```

- **function:** আপনি প্রতিটি উপাদানের ওপর যে কাজটি করতে চান (যেমন: স্কয়ার করা, টেক্সট বড় হাতের করা ইত্যাদি)।
- **iterable:** আপনার মূল ডাটা (যেমন: list, tuple)।

#### সহজ উদাহরণ:

ধরুন, আপনার কাছে কিছু সংখ্যার একটি লিস্ট আছে এবং আপনি প্রতিটি সংখ্যাকে দ্বিগুণ করতে চান।

```python
# প্রতিটি সংখ্যাকে দ্বিগুণ করার জন্য একটি সাধারণ ফাংশন
def double(number):
    return number * 2

# আমাদের মূল লিস্ট
numbers = [1, 2, 3, 4, 5]

# map() ব্যবহার করে লিস্টের প্রতিটি সংখ্যাকে দ্বিগুণ করা
result = map(double, numbers)

# map অবজেক্টকে লিস্টে রূপান্তর করে প্রিন্ট করা
final_list = list(result)
print(final_list)
# আউটপুট: [2, 4, 6, 8, 10]

```

#### Lambda ব্যবহার করে আরও সহজে:

আমরা আলাদা করে ফাংশন না লিখে `lambda` (এক লাইনের ছোট ফাংশন) ব্যবহার করেও এটি করতে পারি:

```python
numbers = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x * 2, numbers))
print(final_list)
# আউটপুট: [2, 4, 6, 8, 10]

```

---

### ২. filter() ফাংশন

`filter()` ফাংশন ব্যবহার করা হয় যখন আপনি কোনো নির্দিষ্ট **শর্তের (Condition) ওপর ভিত্তি করে একটি লিস্ট থেকে কিছু উপাদান বেছে নিতে** বা ছেঁকে আলাদা করতে চান। এটি শুধুমাত্র সেই উপাদানগুলোকে রাখবে যা শর্তটি পূরণ করে (অর্থাৎ শর্তটি `True` হয়)।

#### সিনট্যাক্স:

```python
filter(function, iterable)

```

- **function:** একটি শর্তযুক্ত ফাংশন যা `True` অথবা `False` রিটার্ন করে।
- **iterable:** আপনার মূল ডাটা।

#### সহজ উদাহরণ:

ধরুন, একটি লিস্ট থেকে আপনি শুধুমাত্র জোড় সংখ্যা (Even Numbers) গুলোকে আলাদা করতে চান।

```python
# সংখ্যাটি জোড় কিনা তা পরীক্ষা করার ফাংশন
def is_even(number):
    return number % 2 == 0

# আমাদের মূল লিস্ট
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() ব্যবহার করে জোড় সংখ্যাগুলো আলাদা করা
result = filter(is_even, numbers)

# filter অবজেক্টকে লিস্টে রূপান্তর করে প্রিন্ট করা
even_numbers = list(result)
print(even_numbers)
# আউটপুট: [2, 4, 6, 8, 10]

```

#### Lambda ব্যবহার করে আরও সহজে:

`filter()` ফাংশনেও `lambda` ব্যবহার করে কোড অনেক ছোট করা যায়:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# আউটপুট: [2, 4, 6, 8, 10]

```

---

### map() এবং filter() এর মধ্যে মূল পার্থক্য

| বিষয়             | map()                                                     | filter()                                           |
| ---------------- | --------------------------------------------------------- | -------------------------------------------------- |
| **মূল উদ্দেশ্য** | প্রতিটি উপাদানকে পরিবর্তন বা মডিফাই করা।                  | শর্ত সাপেক্ষে উপাদান বেছে নেওয়া বা ফিল্টার করা।    |
| **আউটপুট সাইজ**  | মূল লিস্টে যতগুলো উপাদান ছিল, আউটপুটেও ঠিক ততগুলোই থাকবে। | মূল লিস্টের সমান বা তার চেয়ে কম উপাদান থাকবে।      |
| **ফাংশনের কাজ**  | যেকোনো মান রিটার্ন করতে পারে (যেমন: গুণফল, যোগফল)।        | শুধুমাত্র `True` বা `False` (Boolean) রিটার্ন করে। |

সংক্ষেপে বলতে গেলে, লিস্টের **সব উপাদানকে পরিবর্তন করতে** `map()` এবং লিস্ট থেকে **নির্দিষ্ট কিছু উপাদান বেছে নিতে** `filter()` ব্যবহার করা হয়।

## Homework

1. Use map() function to convert a list of numbers into a list of strings.
2. Use map() function to create namota of the list [1, 2, 3, 4, 5]
3. Use filter() function to filter strings in a list which length is greater than 10
4. Use filter() function to filter even numbers from a list of numbers
