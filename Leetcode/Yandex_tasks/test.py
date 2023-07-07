import random

a = [random.randint(1, 100) for _ in range(50)]
tmp = a[0]
for ind in range(1, len(a)):
    if a[ind] > tmp:
        tmp1 = tmp
        tmp = a[ind]
print(tmp, tmp1)