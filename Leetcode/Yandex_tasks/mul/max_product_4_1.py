import random


def MaxProduct(count, array: list):
    highest = max(array[0], array[1])
    lowest = min(array[0], array[1])

    highest_product_of_2 = array[0] * array[1]
    lowest_product_of_2 = array[0] * array[1]

    highest_product_of_3 = array[0] * array[1] * array[2]
    lowest_product_of_3 = array[0] * array[1] * array[2]

    highest_product_of_4 = array[0] * array[1] * array[2] * array[3]

    for current in array[2:]:
        highest_product_of_4 = max(
            highest_product_of_4,
            current * highest_product_of_3,
            current * lowest_product_of_3)

        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        lowest_product_of_3 = min(
            lowest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_4

def test(min: int, max: int, size: int, test_num: int):
        a_test = [random.randint(min, max) for _ in range(size)]
        print(f'Test for {a_test}')
        correct_ans = MaxProduct(len(a_test), a_test)
        return correct_ans


if __name__ == '__main__':
    cur_test = 0
    tests = []
    test_num = 100
    n = [random.randint(4, 5) for _ in range(test_num)]
    while cur_test < test_num:
        print(f'Test {cur_test}')
        res = test(-10, 10, n[cur_test], cur_test)
        cur_test += 1
        print(res)
        print()