import random

print("This program simulates 2 dice being rolled")

def die_roll():
    return random.randint(1, 6)

def calculate_roll():
    total = 0
    for turn in range(2):
        total += die_roll()
    return total
    
print("Result: " + str(calculate_roll()))