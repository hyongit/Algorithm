import sys
input = sys.stdin.readline

m = int(input().strip())
s = set()

for _ in range(m):
    com = input().strip().split()

    if len(com) == 1:
        if com[0] == 'all':
            s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        elif com[0] == 'empty':
            s = set()
        continue

    op = com[0]
    num = int(com[1])

    if op == 'add':
        if num in s:
            continue
        else:
            s.add(num)
    
    elif op == 'remove':
        if num in s:
            s.discard(num)
        else:
            continue

    elif op == 'check':
        if num in s:
            print(1)
        else:
            print(0)

    elif op == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)

    