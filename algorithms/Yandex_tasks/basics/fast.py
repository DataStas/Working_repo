if __name__ == "__main__":
    n = int(input())
    m = int(input())
    t = int(input())
    mins = n * 60 + m - t
    hour = t // 60 + n
    mins = t - t // 60 * 60 + m
    hour = str(hour) if len(str(hour)) == 2 else '0' + str(hour)
    mins = str(mins) if len(str(mins)) == 2 else '0' + str(mins)
    print(f'{hour}:{mins}')
8