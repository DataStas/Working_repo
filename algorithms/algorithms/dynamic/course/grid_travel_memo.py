def grid_memo(fun):
    stack = {}

    def wrapper(*args, **kwrgs):
        k = '_'.join(str(x) for x in args)
        if k in stack.keys():
            return stack[k]
        else:
            res = fun(*args, **kwrgs)
            stack[k] = res
            return res
    return wrapper

@grid_memo
def grid_travel(x: int, y: int):
    if x == 1 and y == 1:
        return 1
    if x == 0 or y == 0:
        return 0
    return grid_travel(x, y-1) + grid_travel(x-1, y)


def grid_travel_memo(x: int, y: int, memo={}):
    k = str(x) + '_' + str(y)
    if k in memo:
        return memo[k]
    if x == 1 and y == 1:
        return 1
    if x == 0 or y == 0:
        return 0
    memo[k] = grid_travel_memo(x, y-1, memo) + grid_travel_memo(x-1, y, memo)
    return memo[k]


if __name__ == "__main__":
    c = grid_travel(2, 3)
    print(c)
    c = grid_travel_memo(200, 39)
    print(c)