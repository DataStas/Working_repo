def counter(fun):
    def wrapper(*args):
        global count
        fun(*args)
        count += 1
        return count
    return wrapper

@counter
def move(n, start=1, finish=3):
    if n == 1:
        # print("Перенести диск 1 со стержня", start, "на стержень", finish)
        print(f'{start} {finish}')
    else:
        temp = (6 - start) - finish
        move(n - 1, start, temp) 
        res = (n - 1, temp, finish)
        print(f'{start} {finish}')
        move(*res)


if __name__ == '__main__':
    count = 0
    n = int(input())
    print(2**n-1)
    move(n, 1, 4)
    print(count)
    ans = [1, 3, 5, 9, 13, 17, 25, 33, 41, 49, 65, 81, 97, 113, 129]
    print(2**3*1.5+1)