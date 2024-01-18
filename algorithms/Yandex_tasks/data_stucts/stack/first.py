if __name__ == '__main__':    
    n = int(input())
    commands = []
    while n:
        commands.append(input())
        n -= 1
    stack = []
    for inf in commands:
        if inf[0] == '1':
            x = int(inf.split(' ')[1])
            
            stack.append(x)
            print(stack[-1] if len(stack) > 0 else -1)
            
        if inf[0] == '2':
            stack.pop()
            print(stack[-1] if len(stack) > 0 else -1)