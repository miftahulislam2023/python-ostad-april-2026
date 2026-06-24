# Parameterized Function
# Parameter -> variable inside function definition
# Argument -> value inside function calling

def greet_user(name, age):
    """
    This function will greet the user and print their age
    Example:
        Enter a name: Rakib
        Enter an age: 25
        Hey Rakib, you are 25 years old.
    """
    print(f"Hey {name}, you are {age} years old.")

# Function Calling or Function Invocation
greet_user("Rakib", 25)
greet_user("Abdullah", 40)
greet_user("Zuhan", 9)