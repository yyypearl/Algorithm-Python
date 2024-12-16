import sys

input = sys.stdin.readline

n, total = map(int, input().split())
str = list(input().split())
str.sort()

path = [0] * n       # 뽑은 알파벳
used = [0] * len(str) # 알파벳 사용 유무

vowels = ['a', 'e', 'i', 'o', 'u']
def dfs(level, start):
    if level == n:
        v_count = 0
        for v in vowels:
            if v in path:
                v_count += 1
        if(v_count >= 1 and n - v_count>=2):
            print(*path, sep='')
        return
    for i in range(start, len(str)):
        if used[i] == 0:
            path[level] = str[i]
            dfs(level+1, i+1)
            path[level] = 0

dfs(0, 0)
