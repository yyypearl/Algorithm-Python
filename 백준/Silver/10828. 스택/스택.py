import sys


num = int(sys.stdin.readline().strip())

stack = []

for i in range(num):
    input = sys.stdin.readline().strip().split(' ')
    
    if (input[0] == 'push') :
        stack.append(input[1])
    elif (input[0] == 'pop') :
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif (input[0] == 'size') :
        print(len(stack))
    elif (input[0] == 'empty') :
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    elif (input[0] == 'top') :
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
