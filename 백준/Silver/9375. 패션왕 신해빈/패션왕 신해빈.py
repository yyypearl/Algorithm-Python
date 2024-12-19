import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    n = int(input())
    clothes = []  # 카테고리별 옷 개수
    category = [] # 카테고리
    count = 1
    for i in range(n):
        wear = input().strip().split(' ')
        if wear[1] in category:
            clothes[category.index(wear[1])] += 1
        else:
            category.append(wear[1])
            clothes.append(1)
        
    for i in range(len(category)):
            count *= clothes[i]+1
        
    print(count-1)