import sys
input = sys.stdin.readline

def findPaper(x, y, size):
    global w, b

    color = papers[y][x]
    mid = size // 2

    for i in range (y, y+size):
        for j in range (x, x+size):
            if color != papers[i][j]:
                findPaper(x, y, mid)
                findPaper(x+mid, y, mid)
                findPaper(x, y+mid, mid)
                findPaper(x+mid, y+mid, mid)
                return

    if color:
        b+=1
    else:
        w+=1
        
w, b = 0, 0

n = int(input())
papers = [list(map(int, input().split())) for i in range(n)]

findPaper(0, 0, n)
print(w)
print(b)