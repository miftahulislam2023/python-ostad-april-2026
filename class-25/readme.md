# Class 25: File Handling in Python (বাংলা নোট)
- আজকের ক্লাসের মূল বিষয় হলো **Python File Handling (ফাইল হ্যান্ডলিং)**। ফাইল হ্যান্ডলিংয়ের মাধ্যমে আমরা হার্ডডিস্কে থাকা কোনো ফাইল পড়তে (Read), নতুন ফাইল তৈরি করতে (Write) বা বিদ্যমান ফাইলে নতুন ডেটা যোগ (Append) করতে পারি। এর সাথে আমরা শিখবো কীভাবে **CSV (Comma Separated Values)** ফাইলের সাথে কাজ করতে হয়।

---

## সূচিপত্র (Table of Contents)
1. [ফাইল হ্যান্ডলিং কী এবং কেন প্রয়োজন?](#১-ফাইল-হ্যান্ডলিং-কী-এবং-কেন-প্রয়োজন)
2. [ফাইল ওপেন করা এবং মোডসমূহ (File Modes)](#২-ফাইল-ওপেন-করা-এবং-মোডসমূহ)
3. [ফাইল রিড করা (Reading Files)](#৩-ফাইল-রিড-করা)
4. [ফাইলে রাইট বা অ্যাপেন্ড করা (Writing and Appending)](#৪-ফাইলে-রাইট-বা-অ্যাপেন্ড-করা)
5. [ফাইল ক্লোজ করা এবং `with` স্টেটমেন্ট (Context Manager)](#৫-ফাইল-ক্লোজ-করা-এবং-with-স্টেটমেন্ট)
6. [CSV ফাইলের সাথে কাজ করা (Working with CSV)](#৬-csv-ফাইলের-সাথে-কাজ-করা)

---

## ১. ফাইল হ্যান্ডলিং কী এবং কেন প্রয়োজন?
সাধারণত আমরা পাইথন প্রোগ্রামে যে ভেরিয়েবল বা ডেটা নিয়ে কাজ করি, প্রোগ্রাম শেষ হওয়ার সাথে সাথে তা মেমোরি (RAM) থেকে মুছে যায়। ডেটাকে স্থায়ীভাবে সংরক্ষণ করার জন্য আমরা ফাইল (যেমন: `.txt`, `.csv`, `.json` ইত্যাদি) ব্যবহার করি। পাইথনে ফাইল নিয়ে কাজ করার জন্য কোনো এক্সটার্নাল লাইব্রেরি লাগে না, বিল্ট-ইন ফাংশন দিয়েই তা করা যায়।

---

## ২. ফাইল ওপেন করা এবং মোডসমূহ
পাইথনে ফাইল ওপেন করার জন্য `open()` ফাংশন ব্যবহার করা হয়। এর সিনট্যাক্স হলো:
```python
file_object = open("filename.txt", "mode")
```

### ফাইল ওপেন করার বিভিন্ন মোড (Modes):
*   **`'r'` (Read - ডিফল্ট মোড):** ফাইলটি শুধুমাত্র পড়ার জন্য ওপেন হয়। ফাইলটি আগে থেকেই থাকতে হবে, না থাকলে `FileNotFoundError` দেখাবে।
*   **`'w'` (Write):** ফাইলে লেখার জন্য ওপেন হয়। ফাইলটি আগে থেকে থাকলে তার আগের সব ডেটা মুছে (Overwrite) যায়। ফাইল না থাকলে নতুন ফাইল তৈরি হয়।
*   **`'a'` (Append):** ফাইলের শেষে নতুন ডেটা যোগ করার জন্য ওপেন হয়। আগের ডেটা অক্ষুণ্ণ থাকে। ফাইল না থাকলে নতুন ফাইল তৈরি হয়।
*   **`'x'` (Exclusive Creation):** শুধুমাত্র নতুন ফাইল তৈরি করার জন্য ওপেন হয়। ফাইলটি আগে থেকে থাকলে প্রোগ্রাম এরর (`FileExistsError`) দেবে।
*   **`'t'` (Text Mode - ডিফল্ট):** টেক্সট ফাইলের জন্য।
*   **`'b'` (Binary Mode):** বাইনারি ফাইলের জন্য (যেমন- ছবি, অডিও, পিডিএফ ইত্যাদি)।

---

## ৩. ফাইল রিড করা (Reading Files)
ধরি, আমাদের কাছে `demo.txt` নামের একটি ফাইল আছে যাতে নিচের লেখাগুলো আছে:
```text
Hello Python!
Welcome to Class 24.
Let's learn file handling.
```

### পদ্ধতি ১: সম্পূর্ণ ফাইল একসাথে পড়া (`read()`)
```python
# ফাইল ওপেন করা
file = open("demo.txt", "r")

# সম্পূর্ণ ফাইল রিড করা
content = file.read()
print(content)

# ফাইল ক্লোজ করা (খুবই গুরুত্বপূর্ণ)
file.close()
```

### পদ্ধতি ২: নির্দিষ্ট সংখ্যক ক্যারেক্টার পড়া
```python
file = open("demo.txt", "r")
print(file.read(5)) # প্রথম ৫টি ক্যারেক্টার প্রিন্ট করবে (Hello)
file.close()
```

### পদ্ধতি ৩: লাইন বাই লাইন পড়া
*   **`readline()`:** একটি করে একক লাইন পড়ে।
*   **`readlines()`:** সব লাইন পড়ে একটি লিস্ট (List) হিসেবে রিটার্ন করে।

```python
file = open("demo.txt", "r")

# প্রথম লাইন
print("Line 1:", file.readline())

# সব লাইন একসাথে লিস্ট হিসেবে
file.seek(0) # ফাইলের শুরু থেকে রিড করার জন্য কার্সার ০-তে নেয়া
lines = file.readlines()
print("All Lines as List:", lines)

file.close()
```

### পদ্ধতি ৪: লুপ ব্যবহার করে লাইন বাই লাইন পড়া (সবচেয়ে ভালো উপায়)
```python
file = open("demo.txt", "r")
for line in file:
    print(line.strip()) # strip() দিয়ে লাইনের শেষের এক্সট্রা স্পেস/নিউলাইন সরানো হয়
file.close()
```

---

## ৪. ফাইলে রাইট বা অ্যাপেন্ড করা

### Write মোড (`'w'`) - নতুন ফাইল বা আগের ডেটা মুছে লেখা:
```python
file = open("output.txt", "w")
file.write("This is a new file.\n")
file.write("All previous data will be overwritten if this file existed.")
file.close()
```

### Append মোড (`'a'`) - আগের ডেটার সাথে নতুন ডেটা যোগ করা:
```python
file = open("output.txt", "a")
file.write("\nThis line is appended to the file.")
file.close()
```

---

## ৫. ফাইল ক্লোজ করা এবং `with` স্টেটমেন্ট (Context Manager)
সবসময় ফাইল ব্যবহারের পর `file.close()` করা জরুরি। যদি কোনো কারণে প্রোগ্রামে এরর আসে, তাহলে ফাইলটি ওপেন অবস্থায় থেকে যেতে পারে এবং মেমোরি নষ্ট হতে পারে। 

এই সমস্যা এড়ানোর জন্য পাইথনে **`with` স্টেটমেন্ট** বা **Context Manager** ব্যবহার করা হয়। `with` ব্লকের কাজ শেষ হলে পাইথন নিজে থেকেই ফাইলটি ক্লোজ করে দেয়, কোনো এক্সপ্লিসিট `close()` লিখতে হয় না।

### উদাহরণ:
```python
with open("demo.txt", "r") as file:
    data = file.read()
    print(data)
# এখানে ব্লক থেকে বের হওয়ার সাথে সাথে ফাইলটি স্বয়ংক্রিয়ভাবে ক্লোজ হয়ে গেছে।
```

---

## ৬. CSV ফাইলের সাথে কাজ করা (Working with CSV)
CSV বা **Comma Separated Values** হলো টেবুলার ডেটা (যেমন এক্সেল শিট) সংরক্ষণের একটি জনপ্রিয় ফরম্যাট। পাইথনে বিল্ট-ইন `csv` মডিউল ব্যবহার করে খুব সহজে CSV ফাইল রিড ও রাইট করা যায়।

### CSV ফাইল রিড করা (`csv.reader`):
ধরি, আমাদের কাছে `students.csv` নামের একটি ফাইল আছে:
```csv
Name,Age,Class
Miftahul,23,Python
Rahim,22,Java
Karim,24,Python
```

আমরা এটি এভাবে রিড করতে পারি:
```python
import csv

with open("students.csv", mode="r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    
    # প্রথম (Header) রোটি স্কিপ বা রিড করতে চাইলে:
    header = next(csv_reader)
    print("Headers:", header)
    
    # বাকি ডেটা প্রিন্ট করা
    for row in csv_reader:
        print(f"Name: {row[0]}, Age: {row[1]}, Class: {row[2]}")
```

### CSV ফাইলে রাইট করা (`csv.writer`):
```python
import csv

data = [
    ["Name", "Age", "Class"],
    ["Miftahul", "23", "Python"],
    ["Rahim", "22", "Java"],
    ["Karim", "24", "Python"]
]

with open("new_students.csv", mode="w", newline="", encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    
    # একসাথে সব রো রাইট করা
    csv_writer.writerows(data)
    
    # অথবা একটি একটি করে রো রাইট করা:
    # csv_writer.writerow(["Miftahul", "23", "Python"])

print("CSV file created successfully!")
```

### ডিকশনারি ফরম্যাটে CSV রিড ও রাইট করা (Sleek & Recommended):
`DictReader` এবং `DictWriter` ব্যবহার করলে ডেটাগুলোকে ডিকশনারি ফরম্যাটে সরাসরি ফিল্ডের নাম দিয়ে অ্যাক্সেস করা যায়।

#### `csv.DictReader` ব্যবহার করে পড়া:
```python
import csv

with open("students.csv", mode="r", newline="", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(f"Student: {row['Name']} studies {row['Class']}")
```

#### `csv.DictWriter` ব্যবহার করে লেখা:
```python
import csv

fieldnames = ["Name", "Age", "Class"]

with open("dict_students.csv", mode="w", newline="", encoding="utf-8") as file:
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # হেডার রাইট করা
    dict_writer.writeheader()
    
    # রো রাইট করা
    dict_writer.writerow({"Name": "Miftahul", "Age": "23", "Class": "Python"})
    dict_writer.writerow({"Name": "Rahim", "Age": "22", "Class": "Java"})
```

---

## 💡 মনে রাখার মতো কিছু টিপস:
1. **`newline=""`:** CSV ফাইল ওপেন করার সময় `newline=""` দেওয়া উচিত, অন্যথায় উইন্ডোজে ডাবল নিউলাইন বা ফাঁকা রো তৈরি হতে পারে।
2. **`encoding="utf-8"`:** বাংলা বা অন্য কোনো ইউনিকোড ক্যারেক্টার নিয়ে কাজ করার সময় ফাইল ওপেন করার সময় অবশ্যই `encoding="utf-8"` ব্যবহার করবেন।
3. **`with` স্টেটমেন্ট:** ফাইলে কাজ করার জন্য সবসময় `with` ব্লক ব্যবহার করা বেস্ট প্র্যাকটিস।

## Homework
1. Create a python program to write down prime numbers from 1 to 1000 in a file called prime-numbers.txt
2. Create a python program to write 1 to 30 namota (counting table) in a file called namota.txt 