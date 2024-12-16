import sys

input = sys.stdin.readline

n, total = map(int, input().split())
str = list(input().split())
str.sort()

combi = [0] * n       # 뽑은 알파벳

vowels = ['a', 'e', 'i', 'o', 'u']
def dfs(level, start):
    if level == n:
        v_count = 0
        for v in vowels:
            if v in combi:
                v_count += 1
        if(v_count >= 1 and n - v_count>=2):
            print(*combi, sep='')
        return
    for i in range(start, len(str)):
        combi[level] = str[i]
        dfs(level+1, i+1)
        combi[level] = 0

dfs(0, 0)