import sys
input = sys.stdin.readline().strip()

# 기존 코드
# import re
# split_list = re.split(r'([+-])', input)

# answer = int(split_list[0])
# for i in range(1, len(split_list), 2):
#     operator = split_list[i]
#     number = int(split_list[i+1])

#     if operator == '-':
#         minus = 1
    
#     if minus == 1:
#         answer-=number 
#     else:
#         answer+=number

# 시간 복잡도 개선 (정규식(O(n)) 대신 직접 구현)
minus = False
temp = ''
answer = 0

for item in input:
    if item.isdigit():
        temp += item
    else:
        if minus:
            answer -= int(temp)
        else:
            answer += int(temp)

        temp = ''

        if item == '-':
            minus = True

if minus:
    answer -= int(temp)
else:
    answer += int(temp)

print(answer)