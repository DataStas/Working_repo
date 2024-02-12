from collections import Counter
# def countWords(words1, words2):
#     ans = 0
#     for w in words1:
#         if w in words2 and words1.count(w) == 1 and words2.count(w) == 1:
#             ans += 1
#     return ans


def countWords(words1, words2):
    d = Counter(words1)
    d_1 = Counter(words2)
    ans = 0
    for w in d.keys():
        try:
            if d[w] == 1 and d_1[w] == 1:
                ans += 1
        except KeyError:
            continue
    return ans


if __name__ == "__main__":
    words1 = ["leetcode","is","amazing","as","is"]
    words2 = ["amazing","leetcode","is"]
    print(countWords(words1, words2))