tmp = []
answer = []

for string in strings:
    tmp.append(string[n] + string)

tmp.sort()

for i in tmp:
    answer.append(i[1:])

return answer