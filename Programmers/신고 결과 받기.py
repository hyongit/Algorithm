id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = [0] * len(id_list)
dic = {id : [] for id in id_list}

for i in set(report):
    tmp = i.split(' ')
    dic[tmp[1]].append(tmp[0])

for key, value in dic.items():
    if len(value) >= k:
        for v in value:
            answer[id_list.index(v)] += 1

print(answer)
