
if __name__ == '__main__':
    n = int(input())
    prev = 0
    current = 1
    while current < n:
        old_prev = prev
        prev = current
        current = old_prev + prev
    if n > 3:
        print(current-prev, prev)
    else:
        print(prev, current)