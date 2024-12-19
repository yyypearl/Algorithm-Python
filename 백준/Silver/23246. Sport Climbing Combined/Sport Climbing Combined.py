import sys

input = sys.stdin.readline

n = int(input())

line = []
for _ in range(n):
    line.append(list(map(int, input().strip().split(" "))))

line.sort(key = lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for i in range(3):
    print(line[i][0], end=" ")