k = ")("

def partition(str):
    part1, part2 = "", ""

    for i in range(len(str)):
        part1 += str[i]
        if part1.count('(') == part1.count(')'):
            break

    part2 = str[len(part1):]
    print(part1, part2)

    return part1, part2

#올바
def isright(j):
    stack = []

    for i in j:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    if not stack:
        return True
    else:
        return False

def solution(p):
    answer = ''
    tmp = ''

    #1단계
    if not p:
        return p

    #2단계
    u, v = partition(p)

    #3단계
    if isright(u) == True:
        return u + solution(v)

    #4단계
    else:
        # 4-1
        answer += '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        u = u[1:-1]
        for i in u:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        # 4-5
        return answer + tmp

print(solution(k))