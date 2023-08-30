def sum_of_str(k1: int, first: str, second: str) -> str:
    out = ''
    for a, b in zip(first, second):
        out += a
        out += b
    return out


if __name__ == '__main__':
    k1 = int(input())
    st1 = input()
    st2 = input()
    print(sum_of_str(k1, st1, st2))
    # with open('output.txt', 'w') as f:
    #     f.write(sum_of_polinoms(*test_1))