import sys
input=sys.stdin.readline

sum=0
total=0

n=int(input())
l=list(map(int, input().split()))
l.sort()
for i in l:
  sum+=i
  total+=sum
print(total)
