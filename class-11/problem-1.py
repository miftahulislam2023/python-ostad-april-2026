"""
Create a nested loop to simulate:
Daily schedule like:

Morning session → 3 tasks
Evening session → 3 tasks

Print:
Morning Task 1
Morning Task 2
Morning Task 3
Evening Task 1
Evening Task 2 
Evening Task 3
"""

for order in range(1, 3):
    if order == 1:
        for i in range(3):
            print(f"Morning Task {i + 1}")
    else:
        for i in range(3):
            print(f"Evening Task {i + 1}")
