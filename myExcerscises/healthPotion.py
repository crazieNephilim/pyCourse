# modules
import random

# header
print("***Health Potion***")

# variables
difficulty = eval(raw_input("Enter difficulity (1-3): "))
health = 50
potion_health = int(random.randint(25, 50) / difficulty)


# print variable values
if difficulty == 1:
    print("Difficulty is EASY")
elif difficulty == 2:
    print("Difficulty is MEDIUM")
elif difficulty == 3:
    print("Difficulty is HARD")
else:
    print("Difficulty must be numeric value between 1 and 3")
    exit()

print("Current Health: ", health)
print("Potion Health: ", potion_health)

# using health potion
health = health + potion_health
print("You used health potion !")
print("Current Health: ", health)
