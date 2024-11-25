import sys
import itertools

input = sys.stdin.readline

while 1:
    try:
        line = list(map(int, input().split()))
        if line == [0]: 
            break
        n = line[0]
        number = line[1:]
        
        for i in itertools.combinations(number, 6):
            print(*i)
        print()
    except EOFError:
        break