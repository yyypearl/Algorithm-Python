import sys;

def cantor(total):
    if (total==1):
        return "-"
    else:
        return cantor( total//3 )+" "*( total//3 )+cantor( total//3 )

test_case = sys.stdin.readlines()
for n in test_case:
    init = 3**int(n)
    print(cantor(init))
