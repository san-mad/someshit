import random
random = random.randint(1, 10)
for i in range(10):
    print(i)
    if i == random:
        break
    if i % 2 == 0:
        continue