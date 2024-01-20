
def secondHighest(s):
    """
    :type s: str
    :rtype: int
    """
    print(dict.fromkeys(s).keys())
    digs = [x for x in set(s) if x.isdigit()]
    # digs = [x for x in dict.fromkeys(s).keys() if x.isdigit()]
    return sorted(digs, reverse=True)[1]


if __name__ == "__main__":
    print(secondHighest("ck077"))
    