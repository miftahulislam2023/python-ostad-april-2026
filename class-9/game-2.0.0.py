# Number guessing game
import random
n = random.randint(1, 100)
chance_left = 7

while chance_left != 0:
    x = int(input("Guess the number: "))
    if x < n:
        print("Too low")
    elif x > n:
        print("Too high")
    else: 
        print("Congratulations! You got it!")
        break
    
    chance_left -= 1 # chance_left = chance_left - 1
    
print("The number was", n)
print("Your score is", chance_left)