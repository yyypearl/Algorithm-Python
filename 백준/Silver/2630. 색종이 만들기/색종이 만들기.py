import sys

n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for i in range(n)]


white_count = 0
blue_count = 0

def findPaper(n, papers):
    global white_count, blue_count

    # 페이지 내 모두 같은 색상일 경우
    flattened = [item for row in papers for item in row]
    unique = set(flattened)

    if len(unique)==1:
        if flattened[0]==1:
            blue_count += 1
        else:
            white_count +=1

    else:
        mid = n // 2
        findPaper(mid, [row[:mid] for row in papers[:mid]])
        findPaper(mid, [row[mid:] for row in papers[:mid]])
        findPaper(mid, [row[:mid] for row in papers[mid:]])
        findPaper(mid, [row[mid:] for row in papers[mid:]])

    return (f"{white_count}\n{blue_count}")

print(findPaper(n, papers))