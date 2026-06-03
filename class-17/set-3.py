A = {
    1, 2, 3, 4, 5
}

B = {
    3, 4, 5
}

C = {
    1, 3, 5, 7
}

"""
A u B = { 1, 2, 3, 4, 5 }
A n B = { 3, 4, 5}
A - B = A \\ B = { 1, 2 }
B - A = B \\ A = { } -> Null set -> ফাঁকা সেট
C - B = { 1, 7 }
B - C = { 4 }
"""

# Set Union | (pipe symbol)
## A ∪ B = {x: x ∈ A or x ∈ B}
print(A | B)

# Set Intersection & (ampersand)
## A ∩ B = {x: x ∈ A and x ∈ B}
print(A & B)

# Set Difference - (hyphen, dash)
print(A - B)
print(B - A)
print(C - B)
print(B - C)


#Set Symmetric Difference ^ (caret)