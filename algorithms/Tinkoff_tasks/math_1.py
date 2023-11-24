import random
sum = 0
for i in range(201):
    if random.randint(0, 1) > 0.5:
        sum = sum + i
    else:
        sum = sum + i + 1
print(sum)

print(2**6)