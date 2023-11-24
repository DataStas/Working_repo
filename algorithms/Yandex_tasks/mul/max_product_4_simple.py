import random


def HighestLowest(count, array: list):
    highest = max(array[0], array[1])
    lowest = min(array[0], array[1])
    highest_prod_of_2 = array[0] * array[1]

    for current in array[1:]:
        highest_prod_of_2 = max(
            highest_prod_of_2,
            current * highest,
            current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)
    # print(highest, lowest)
    return [highest, lowest]


def MaxPairwiseProduct(count, array):
    highest = max(array[0], array[1])
    lowest = min(array[0], array[1])
    highest_prod_of_2 = array[0] * array[1]

    for current in array[1:]:
        highest_prod_of_2 = max(
            highest_prod_of_2,
            current * highest,
            current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)
    return highest_prod_of_2


def extract_min_max(array: list, size: int):
    positive = []
    negative = []
    array_2 = array.copy()
    print(f'Array {array} to reduce with {size}')
    for _ in range(size):
        ans_1 = max(array)
        array.remove(ans_1)
        ans_2 = min(array_2)
        array_2.remove(ans_2)
        positive.append(ans_1)
        negative.append(ans_2)
    return positive, negative


def MaxProduct(count, array: list):
    if len(array) == 4:
        return array[0]*array[1]*array[2]*array[3]
    if len(set(array)) < 9:
        all = array.copy()
    else:
        positive, negative = extract_min_max(array, 4)
        all = positive+negative
    max_1 = []
    min_1 = []
    while len(max_1) < 2:
        m1, m2 = HighestLowest(len(all), all)
        max_1.append(max(m1, m2))
        min_1.append(min(m1, m2))
        all.remove(m1)
        all.remove(m2)
    ans = 1
    ans *= max(max_1[0]*max_1[1], min_1[0]*min_1[1])
    if max_1[0]*max_1[1] == ans:
        all += min_1
    else:
        all += max_1
    second_part = MaxPairwiseProduct(len(all), all)
    print(ans, second_part)
    ans *= second_part
    return ans


def test(min: int, max: int, size: int, test_num: int):
        a_test = [random.randint(min, max) for _ in range(size)]
        print(f'Cur array {a_test}')
        correct_ans = MaxProduct(len(a_test), a_test)
        return correct_ans


if __name__ == '__main__':
    cur_test = 0
    tests = []
    test_num = 100
    n = [random.randint(4, 100) for _ in range(test_num)]
    while cur_test < test_num:
        print(f'Test {cur_test}')
        res = test(-10, 10, n[cur_test], cur_test)
        cur_test += 1
        print(res)
        print()