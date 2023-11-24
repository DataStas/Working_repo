if __name__ == '__main__':
    count = int(input())
    if count > 6:
        print('Yes')
        part_1 = [count]
        part_2 = [ind for ind in range(1, count)]
        ans = part_1+part_2
        print(*ans)
    else:
        print('No')