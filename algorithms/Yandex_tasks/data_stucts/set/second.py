def count_interesting_pairs(words):
    count = 0
    n = len(words[0])
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            diff_count = 0
            for k in range(n):
                if words[i][k] != words[j][k]:
                    diff_count += 1
                    if diff_count > 1:
                        break
            if diff_count == 1:
                count += 1
                
    return count


# if __name__ == '__main__':
    # n = int(input())
    # words = []
    # while n:
    #     words.append(set(input()))
    #     n -= 1
    # with open('Yandex_tasks/data_stucts/set/in2.txt', 'r') as f:
    #     info = f.read()
    #     count = 0
    #     print(info.split('\n')[1:-1])
    #     for w in info.split('\n')[1:-1]:
    #         for w2 in info.split('\n')[1:-1]:
    #             if w == w2:
    #                 continue
    #             w_set = set(w)
    #             w2_set = set(w2)
    #             dif = w_set.difference(w2_set)
    #             if len(dif) == 1 and w.count(str(dif)[2]) == 1:
    #                 count += 1

    #     print(count//2)
if __name__ == '__main__':
    n = int(input())
    words = []
    while n:
        words.append(input())
        n -= 1
    count = 0
    for w in words:
        for w2 in words:
            if w == w2:
                continue
            w_set = set(w)
            w2_set = set(w2)
            dif = w_set.difference(w2_set)
            if len(dif) == 1 and w.count(str(dif)[2]) == 1:
                count += 1

    print(count//2)