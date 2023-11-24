# lst = [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]
n = int(input())
lst = [int(i) for i in input().split()]
dic = {}
dic = dic.fromkeys(set(lst), 0)
for num in lst:
    dic[num] += 1
num_of_each_number = list(dic.values())
num_of_each_number = sorted(num_of_each_number, reverse=True)
# print(num_of_each_number)
sum = 0
working = True
while working:
    for ind in range(len(num_of_each_number)-1):
        if num_of_each_number[ind] != num_of_each_number[-1]:
            sum = sum + num_of_each_number[ind]
    if len(num_of_each_number)*num_of_each_number[-1] > sum:
        print(len(num_of_each_number) * num_of_each_number[-1] + 1)
        working = False
    else:
        num_of_each_number.pop()
        sum = 0