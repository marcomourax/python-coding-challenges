import random
# Write your code below this line
# Hint: Remember to import the random module first.
print("1 means Heads\n0 means Tails")
side = input("Heads or Tails? \n").lower()

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
