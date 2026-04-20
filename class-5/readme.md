# Class - 5

## Topics to Be Covered:
- Nested conditions
- Truthy/falsy values
- Debugging

## Falsy value
- 0, 0.0
- "", '', {}, [], ()

## HW
### **Section 1: Truthy and Falsy Values**

**Question 1: The Identity Crisis**
In Python, many objects have an inherent "truthiness." Look at the following list of variables. Which of these will evaluate to `True` when passed into a boolean check like `if variable:`?

* `a = 0.0`
* `b = " "` (a string containing a single space)
* `c = []`
* `d = -1`
* `e = None`

**Question 2: Short-Circuit Logic**
What will be the exact output of the following code snippet?
```python
x = []
y = "Hello"

if x or y:
    print(f"Result: {y}")
else:
    print("Result: Nothing")
```

### **Section 2: Nested Conditions**

**Question 3: The Admission Gate**
Analyze the logic below. What will the code print if `age = 17` and `has_permission = True`?

```python
age = 17
has_permission = True

if age >= 18:
    if has_permission:
        print("Full Access")
    else:
        print("Limited Access")
else:
    if has_permission:
        print("Youth Access")
    else:
        print("No Access")
```

**Question 4: Debug the Nest**
A developer wants to write a script that checks if a number is **even and greater than 10**. They wrote the following nested structure, but it has a logic flaw. 

**Identify the flaw:** If the user inputs `7`, what does the script print, and why is the `else` placement problematic?

```python
num = 7

if num > 10:
    if num % 2 == 0:
        print("Winner!")
    else:
        print("Odd but big.")
else:
    print("Too small.")
```

### **Quick Reference Table**

| Category | Falsy Values (Evaluate to `False`) | Truthy Values (Evaluate to `True`) |
| :--- | :--- | :--- |
| **Numbers** | `0`, `0.0` | Any non-zero number (e.g., `1`, `-5`, `3.14`) |
| **Strings** | `""` (Empty string) | `" "`, `"False"`, `"0"` (Non-empty) |
| **Collections** | `[]`, `{}`, `set()`, `()` | Any collection with at least one item |
| **Other** | `None`, `False` | `True` |