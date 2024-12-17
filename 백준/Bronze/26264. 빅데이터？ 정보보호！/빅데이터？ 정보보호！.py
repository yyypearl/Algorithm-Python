import sys

input = sys.stdin.read

str = input()

security = 0
bigdata = 0

for s in str:
    if "s" in s:
        security += 1
    elif "b" in s:
        bigdata += 1

if bigdata > security:
    print("bigdata?")
elif bigdata < security:
    print("security!")
else:
    print("bigdata? security!")