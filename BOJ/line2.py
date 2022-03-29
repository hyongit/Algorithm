from itertools import combinations

sentences = ["line in line", "LINE", "in lion"]	
n = 5
arr = []
result_tmp = []

for i in sentences:
    tmp = list(set(i))
    
    if ' ' in tmp:
        tmp.remove(' ')

    for j in tmp:
        #print(j)
        if j.isupper() == True:
            arr.append('shift')
        arr.append(j.lower())

arr = list(set(arr))

# 조합 후 점수 계산
for i in combinations(arr, n):
    i_tmp = list(i)
    #print(i_tmp)

    if 'shift' in i:
        for l in i:
            if l == 'shift':
                continue
            i_tmp.append(l.upper())
    print(i_tmp)
    result = 0

    for j in sentences:
        print(j)
        len_words = 0
        len_upper = 0
        len_lower = 0
        len_space = 0
        for k in j:
            if k in i_tmp and k.islower() == True:
                len_lower += 1
                len_words += 1
                
            elif k in i_tmp and k.isupper() == True:
                len_upper += 1
                len_words += 2

            elif k == ' ':
                len_words += 1
                len_space += 1
        
        print(len_words, len_lower, len_upper)

        if len(j) == len_lower+len_upper+len_space:
            result += len_words

        print(result)
    result_tmp.append(result)
print(max(result_tmp))