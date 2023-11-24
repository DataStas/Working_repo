import random
from collections import Counter

def sum_poly(count, array):
    ans_1 = max(array)
    array.remove(ans_1)
    ans_2 = max(array)
    return ans_1*ans_2


def MaxPairwiseProduct(count, array):
    m1 = array[0]
    m2 = array[1]
    if m2 > m1:
        m1, m2 = m2, m1
    i = 1
    for ind in range(2, count):
        if array[ind] > m1:
            m2 = m1
            m1 = array[ind]
            i += 1
        else:
            if array[ind] > m2:
                m2 = array[ind]
                i += 1
    return m1 * m2, i


def test(min: int, max: int, size: int, test_num: int):
        a_test = [random.randint(min, max) for _ in range(size)]
        a_test_sorted = sorted(a_test)
        correct_ans = a_test_sorted[-1]*a_test_sorted[-2]
        alg_ans, comparison = MaxPairwiseProduct(len(a_test), a_test)
        if correct_ans == alg_ans:
            print(f'Correct test {test_num} for array \n{a_test}\n{a_test_sorted}')
            print(f'Compare num {comparison}')
            return True
        else:
            print(f'Incorrect test {test_num} for array\n{a_test}\n{a_test_sorted}')
            print(correct_ans, alg_ans)
            return False


if __name__ == '__main__':
    # count = int(input())
    # array = list(map(int,input().split()))
    cur_test = 0
    tests = []
    while cur_test < 100:
        res = test(0, 100, 10, cur_test)
        if res:
            tests.append(res)
        cur_test += 1