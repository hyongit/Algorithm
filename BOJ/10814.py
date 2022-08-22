# [백준] 나이순 정렬

n = int(input())
people = []

for i in range(n):
    tmp = list(input().split())
    tmp.append(i)
    people.append(tmp)

people.sort(key = lambda x : (int(x[0]), x[2]))

for j in people:
    print(j[0], j[1])