id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = [0] * len(id_list)
dict = {id : [] for id in id_list}

for i in set(reports):
    report = i.split(' ')
    dict[report[1]].append(report[0])

print(dict)

for key, value in dict.items():
    if len(value) >= k :
        for v in value:
            answer[id_list.index(v)] += 1

print(answer)
