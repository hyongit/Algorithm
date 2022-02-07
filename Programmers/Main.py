import sys

n = int(input())
data_list = []

for _ in range(n):
    data_list.append(sys.stdin.readline().strip())

#중복 제거
data_list = list(set(data_list))

data_list.sort() #data_list 알파벳 순으로 정렬
data_list.sort(key=lambda x: len(x))

for i in data_list:
    print(i)