l = [int(i) for i in input().split()]
if l == sorted(l) or l == sorted(l, reverse=True):
    print("Yes")
else:
    print("No")
print(l.sort())