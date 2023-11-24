if __name__ == '__main__':
    n = int(input())
    k = [0.5, 1, 1.5, 2] + [x for x in range(3, 11)]
    print(k)
    print(int(2**3*k[n-3]+1))
    
    