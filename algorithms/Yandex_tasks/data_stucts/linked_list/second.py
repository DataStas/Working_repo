import random
# def find_min_max_pairs(arr: list):
#     max_index = arr.index(max(arr))
#     cur = max(arr)

#     if max_index == 0:
#         max_right_index = max_index + 1
#         min_right_index = arr.index(min(arr[max_index:]), max_index)+1
#         while arr.index(arr[0]) == arr.index(cur):
#             arr.pop(0)
#             cur = max(arr)
#             max_index = arr.index(cur)
#         max_left_index = max_index + 1
#         min_left_index = arr.index(min(arr[:max_index]))+1

#     if max_index == len(arr) - 1:
#         max_left_index = max_index + 1
#         min_left_index = arr.index(min(arr[:max_index]))+1
#         while arr.index(arr[-1]) == arr.index(cur):
#             arr.pop()
#             cur = max(arr)
#             max_index = arr.index(cur)
#         max_right_index = max_index + 1
#         min_right_index = arr.index(min(arr[max_index:]), max_index)+1
        
    
#     return (max_right_index, min_right_index), (min_left_index, max_left_index)

def slow(arr: list):
    # Инициализация переменных для минимального и максимального различий
    min_diff = float('inf')
    max_diff = float('-inf')
    min_pair = None
    max_pair = None

    # Поиск минимального и максимального различий
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_diff = arr[i] - arr[j]

            # Обновление минимального различия и пары
            if current_diff < min_diff:
                min_diff = current_diff
                min_pair = (i + 1, j + 1)

            # Обновление максимального различия и пары
            if current_diff > max_diff:
                max_diff = current_diff
                max_pair = (i + 1, j + 1)
    return max_pair, min_pair


def find_min_max_pairs(arr: list):
    max_index = arr.index(max(arr))
    cur = max(arr)

    if max_index == 0:
        # If the maximum is at the beginning of the array
        max_right_index = max_index + 1
        min_right_index = arr.index(min(arr[max_index+1:])) + 1
        counter = 1
        while arr.index(arr[0]) == arr.index(cur):
            arr.pop(0)
            cur = max(arr)
            max_index = arr.index(cur)
            counter += 1
        max_left_index = max_index + counter
        min_left_index = arr.index(min(arr[:max_index+1])) + 1

    elif max_index == len(arr) - 1:
        # If the maximum is at the end of the array
        max_left_index = max_index + 1
        min_left_index = arr.index(min(arr[:max_index])) + 1
        counter = 1
        while arr.index(arr[-1]) == arr.index(cur):
            arr.pop()
            cur = max(arr)
            max_index = arr.index(cur)
            counter += 1
        max_right_index = max_index + counter
        min_right_index = arr.index(min(arr[max_index+1:])) + 1

    else:
        # If the maximum is in the middle of the array
        max_left_index = max_index + 1
        min_left_index = arr.index(min(arr[:max_index])) + 1
        max_right_index = max_index + 1
        min_right_index = arr.index(min(arr[max_index+1:]), max_index) + 1
        while arr:
            arr.pop()

    return (max_right_index, min_right_index), (min_left_index, max_left_index)


def test(test_num: int):
    good = 0
    for _ in range(test_num+1):
        arr = [random.randint(1, 10**5) for p in range(10)]
        print(f'Test {_}')
        try:
            assert slow(arr) == find_min_max_pairs(arr)
            # print(slow(arr), find_min_max_pairs(arr))
            # print('Success')
            good += 1
        except AssertionError:
            print(arr)
            print(slow(arr), find_min_max_pairs(arr))
            print('Error')
        print('----------------------------------------------')
    print(f"Total: {good}/{test_num+1}")
if __name__ == '__main__':
    # Ввод данных
    # n = int(input())
    # test(10)
    find_min_max_pairs([64565, 78530, 31568, 70404, 82479, 41292, 51992, 14711, 79872, 22481])
