# 백준 [듣보잡]

n, m = map(int, input().split())

dmp = set()
bmp = set()
ans = []

for _ in range(n):
    d_name = input()
    dmp.add(d_name)

for _ in range(m):
    b_name = input()
    bmp.add(b_name)

ans = sorted(dmp & bmp)

print(len(ans))
for a in ans:
    print(a)