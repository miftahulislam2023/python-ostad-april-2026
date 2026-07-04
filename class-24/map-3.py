names = ["Miftah", "Ridita", 'Tasin', "Zuhan", "Shihab", "Nayeem", "Fahim", "Rishat", "Roni", "Shovon"]
def greetPeople(name):
    return f"Congratulations, {name}"

greetings = list(map(greetPeople, names))

lambda_greetings = list(map(lambda name: f"Congratulations, {name}!", names))

print(greetings)
print(lambda_greetings)