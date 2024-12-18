import sys

input = sys.stdin.readline

n = int(input())

def bridge(s, t):
    top = 1
    down = 1
    while(s>0):
        top *= t
        down *= s
        t -= 1
        s -= 1
    return int(top/down)

for i in range(n):
    a, b = map(int, input().split())
    print(bridge(a, b))