import sys

input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    pair = list(map(int,(input()).strip().split(" ")))
    li.append(pair)
li.sort()

for i in range(n):
    print(li[i][0], li[i][1])