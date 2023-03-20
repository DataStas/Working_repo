def find_substring(ans: set, s:  str, left_pointer: int) -> int:
    condition = True
    answer = 1
    while condition:
        answer += 1
        if s[left_pointer+1] in ans:
            left_pointer += 1
        else:
            ans.add(s[left_pointer+1])
            left_pointer += 1
        if 'a' in ans and 'b' in ans and 'c' in ans and 'd' in ans:
            return answer
        if left_pointer >= len(s) - 1:
            return -1


a = int(input())
in_string = input()
left_pointer = 0
answer = []
while left_pointer < len(in_string) - 3:
    if in_string[left_pointer] != in_string[left_pointer+1]:
        answer.append(find_substring(set(in_string[left_pointer]),
                                     in_string,
                                     left_pointer))
        left_pointer += 1
    else:
        left_pointer += 1

answer = set(answer)
if len(answer) > 1:
    answer.remove(-1)
    print(min(answer))
else:
    print(-1)
