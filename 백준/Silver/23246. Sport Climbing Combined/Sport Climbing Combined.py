import sys

input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    line = list(map(int, input().strip().split(" ")))
    score = line[1]*line[2]*line[3]
    second = line[1]+line[2]+line[3]

    li.append([score, second, line[0]])

li.sort()

for i in range(3):
    print(li[i][2], end=" ")