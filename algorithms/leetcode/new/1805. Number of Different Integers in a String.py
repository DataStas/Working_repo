import re
def numDifferentIntegers(word):
    """
    :type word: str
    :rtype: int
    """
    l = 0
    r = 0
    nums = []
    while l < len(word):
        if word[l].isdigit():
            r = l
            while r < len(word) and word[r].isdigit():
                r += 1
            nums.append(int(word[l:r]))
            l = r
        l += 1
    return len(set(nums))
 
    
if __name__ == "__main__":
    print(numDifferentIntegers("a1b01c001"))