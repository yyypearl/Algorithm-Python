import sys

n = int(sys.stdin.readline())

def printStar(N):
    if N==1:
        return ["*"]
    
    lines = printStar(N//3)
    return [s*3 for s in lines] + [s + " " * (N // 3) + s for s in lines] + [s*3 for s in lines]

print("\n".join(printStar(n)))