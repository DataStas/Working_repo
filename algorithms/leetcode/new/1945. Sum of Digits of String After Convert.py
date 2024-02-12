def getLucky(s: str, k: int):
    s = ''.join(str(ord(c)-96) for c in s)
    while k:
        s = str(sum(int(c) for c in s))
        k -= 1
    return s

if __name__ == "__main__":
    s = "zbax"
    k = 2
    print(getLucky(s, k))