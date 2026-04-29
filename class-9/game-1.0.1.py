# Number guessing game
n = 75
chance_left = 3

while chance_left != 0:
    x = int(input("Guess the number: "))
    if x < n:
        print("Too low")
    elif x > n:
        print("Too high")
    else: 
        print("Congratulations! You got it!")
    chance_left -= 1 # chance_left = chance_left - 1
    