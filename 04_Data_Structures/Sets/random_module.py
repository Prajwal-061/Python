import random

# a = random.randint(1, 6)
# a = random.randrange(1, 3)
# a = random.random()
# print(a)

l = [12, 13, 14, 567, 899, 234, 435, -12]
a = random.choice(l)
random.shuffle(l)
print(a)
print(l)
