in_info = [int(i) for i in input().split()]
jun, sen, check = in_info
store = []
for j in range(jun):
    store.append(2)
ind = 0
iter = 0
while sum(store) != 0:
    for _ in range(sen):
        if ind < jun:
            if store[ind] != 0:
                store[ind] -= 1
                ind += 1
            else:
                ind += 1
        else:
            ind = 0
            if store[ind] != 0:
                store[ind] -= 1
                ind += 1
    iter += 1
print(iter)