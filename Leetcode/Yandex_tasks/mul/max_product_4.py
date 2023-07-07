import random


def MaxProduct(count, array):
    highest = max(array[0], array[1])
    lowest =  min(array[0], array[1])

    highest_product_of_2 = array[0] * array[1]
    lowest_product_of_2  = array[0] * array[1]

    highest_product_of_3 = array[0] * array[1] * array[2]
    lowest_product_of_3 = array[0] * array[1] * array[2]

    highest_product_of_4 = array[0] * array[1] * array[2] * array[3]

    for current in array[3:]:
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


# def test(min: int, max: int, size: int, test_num: int):
#         a_test = [random.randint(min, max) for _ in range(size)]
#         correct_ans = MaxProduct(len(a_test), a_test)
#         print(f'Correct test {test_num} for array \n{a_test}')


if __name__ == '__main__':
    # count = int(input())
    # array = list(map(int,input().split()))
    cur_test = 0
    tests = []
    while cur_test < 100:
        res = test(-100, 100, 10, cur_test)
        if res:
            tests.append(res)
        cur_test += 1