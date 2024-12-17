import sys

input = sys.stdin.read

str = input()

security = str.count("security")
bigdata = str.count("bigdata")

if bigdata > security:
    print("bigdata?")
elif bigdata < security:
    print("security!")
else:
    print("bigdata? security!")