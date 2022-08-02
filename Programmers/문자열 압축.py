s = 'abcabcdede'

for i in range(1, len(s)+1): # i자씩 끊기!
        b = ''
        cnt = 1 
        tmp=s[:i] 
        # [a]
        # [ab]
        # [abc]
        # ...

        for j in range(i, len(s)+i, i): # i부터 끝까지 i단위로 나누어 탐색
            print(j, s[j:i+j])
            if tmp==s[j:i+j]:# i 단위로 자른 것이 앞과 같으면

                # i = 1, [b, c, a, b, c, ...]
                # i = 2, [ca, bc, de, de]
                # i = 3, [abc, ded, e]

                cnt+=1 # 카운트
            else: # 아니면
                if cnt!=1: # 앞에서 중복이 있었다!
                    b = b + str(cnt)+tmp # 글자 만들기
                    #print(j, b)
                else:
                    b = b + tmp # 아니면 그냥 문자 붙임
        
                tmp=s[j:j+i]
                cnt = 1
            #print(b)
