def solution(s):
    answer = []
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s)+i, i):
            if tmp == s[j:j+i]:
                cnt += 1
                
            else:
                if cnt > 1:
                    b = b + str(cnt) + tmp
                    
                else:
                    b += tmp
                    
                tmp = s[j:j+i]
                cnt = 1
    
        answer.append(len(b))
    return min(answer)

print(solution(input()))