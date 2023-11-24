import random


def MaxPairwiseProduct(count, array: list):
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
    # print(f'Highest {highest_prod_of_2}')
    tmp = []
    for cur in array:
        try:
            div = highest_prod_of_2/cur
        except ZeroDivisionError:
            continue
        if div in array:
            tmp.append(div)
    print(f"To return {tmp}")
    if len(tmp) == 2:
        return tmp
    else:
        ans = list(set(tmp))
        if len(ans) == 1:   
            return [ans[0], ans[0]]
        else:
            return [ans[0], ans[1]]


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
    positive, negative = extract_min_max(array, 4)
    all = positive+negative
    if len(set(all)) == len(all):
        # print(all)
        ans = []
        m1, m2 = MaxPairwiseProduct(len(all), all)
        # print(f'First to delete {[m1, m2]}')
        ans.extend([m1, m2])
        all.remove(m1)
        all.remove(m2)
        m3, m4 = MaxPairwiseProduct(len(all), all)
        ans.extend([m3, m4])
        mul = 1
        for cur in ans:
            mul *= cur
        return mul
    else:
        all = list(set(all))
        print(all)
        if len(all) > 3:
            m1, m2 = MaxPairwiseProduct(len(all), all)
        else:
            sorted(all)
            m1, m2 = all[-1], all[-2]
        print(f'First to delete {[m1, m2]}')

def test(min: int, max: int, size: int, test_num: int):
        a_test = [random.randint(min, max) for _ in range(size)]
        correct_ans = MaxProduct(len(a_test), a_test)
        return correct_ans


if __name__ == '__main__':
    cur_test = 0
    tests = []
    test_num = 100
    n = [random.randint(4, 5) for _ in range(test_num)]
    while cur_test < test_num:
        print(f'Test {cur_test}')
        res = test(0, 10, n[cur_test], cur_test)
        cur_test += 1
        print(res)
        print()