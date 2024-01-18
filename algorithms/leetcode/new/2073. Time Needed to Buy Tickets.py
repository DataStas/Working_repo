def timeRequiredToBuy(tickets, k):
    """
    :type tickets: List[int]
    :type k: int
    :rtype: int
    """
    time = 0
    while tickets[k] != 0:
        cur = tickets.pop(0)
        if cur != 0:
            tickets.append(cur-1)
            time += 1
        k = len(tickets)-1 if k == 0 else k - 1
    return time

if __name__ == "__main__":
    print(timeRequiredToBuy([5, 1, 1, 1], k=0))