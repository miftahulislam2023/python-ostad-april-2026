t2 = (1, 2, 3, 4, 5)

# Case-1: যতগুলো item ততগুলো variable লাগবে
one, two, three, four, five = t2

print(one)

# Case-2: যতগুলো item ততগুলো variable না থাকলে * ইউজ করে একই variable এ একাধিক মান রাখব
one, *numbers, five = t2

print(numbers)