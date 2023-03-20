
def get_sum(a, left: int, right: int) -> int:
    return a[right] - a[left]

cache = {0: 0, 1: 1}
def fibonacci_of(n):
    if n in cache: 
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)


a = [-1, 1, 2, -3, 6]
n = len(a)
sums = [0]
for ind in range(n):
    sums.append(sums[ind]+a[ind])
print(sums[1:], set(sums[1:]))

    


answer = {}
answer = answer.fromkeys(set(sums[1:]), 0)

for sum in sums[1:]:
    answer[sum] += 1

print(answer)

ans = 0
for key, value in answer.items():
    if key == 0:
        ans += len(sums[1:]) - 1
    if value > 1:
        left_pointer = 1
        right_pointer = len(sums) - 1 
        while left_pointer < right_pointer:
            if sums[left_pointer] == key:
                if sums[left_pointer] == sums[right_pointer]:
                    ans += left_pointer + (len(sums)-right_pointer) - 1
                    break
                else:
                    right_pointer -= 1
            else:
                left_pointer += 1
print(ans)