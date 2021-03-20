import random
items = ["*6", "*5", "*4", "*3"] # Contents
prob = [0.02, 0.08, 0.5, 0.4] # probability
N = 10 # times
n = random.choices(items, weights=prob, k=N)
print(n)