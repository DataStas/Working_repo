import sys

lineIn = sys.stdin.readline().split(" ")
n = int(lineIn[0])
m = int(lineIn[1])

fibPrev = 0
fib = 1
cached = [fibPrev, fib]

for curr in range(1, n+2):
    fibOld = fib
    fib = (fib + fibPrev) % m
    fibPrev = fibOld

    if fibPrev == 0 and fib == 1:
        cached.pop()
        break
    else:
        cached.append(fib)

offset = n % len(cached)
sys.stdout.write(str(cached[offset]))