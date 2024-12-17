import sys

input = sys.stdin.read

n = int(input())

number = list(range(n+1))[1::]
path = [0] * n
used = [0] * n

for i in range(n):
   number.append(i)

def dfs(N):
   if N==n:
      print(*path)
      return
   for i in range(n):
      if used[i] == 0:
         path[N]=number[i]
         used[i]=1
         dfs(N+1)
         used[i]=0
         path[N]=0

dfs(0)