# 2
def partition(k):
    tmp_u = ''
    total = ''
    str = '('
    tmp_u += k[0]

    for i in range(1, len(k)):
        tmp_u += k[i]

        if tmp_u.count('(') == tmp_u.count(')'):
            break

    a = len(tmp_u)
    tmp_v = k[a:]

    return tmp_u, tmp_v


# 3
def isright(k):
    stack = []

    for i in k:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''
    # 1
    if not p:
        return p

    # 2
    u, v = partition(p)

    # 3
    if isright(u) == True:
        answer += u
        return answer + solution(v)

    # 4
    else:
        # 4-1
        answer += '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution(')('))