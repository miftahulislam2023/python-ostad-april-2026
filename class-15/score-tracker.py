import random
scores = []
ans = -2
print("-------  Scroe Tracker -------")
print("Enter 0 to exit.")

while ans != 0:
    # generate two random numbers
    num1 = random.randint(20, 100)
    num2 = random.randint(20, 100)

    # take input from user
    print(f"{num1} + {num2} = ?")
    ans = int(input())
    
    # check if input is zero(0)
    if ans == 0:
        break

    # justify the answer
    elif ans == (num1 + num2):
        print("Correct!")
        scores.append(1)

    else:
        print("Wrong!")
        scores.append(-0.25)

print("Your scores are:")
print(scores)

total_score = 0
for x in scores:
    total_score += x

print(total_score)