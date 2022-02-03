numbers = [2,5,8,0]
hand = "right"

position = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
}

answer = ''
l_key = '*'
r_key = '#'

l_dis = 0
r_dis = 0



for i in numbers:
    if i in [1, 4, 7]:
        answer += 'L'
        l_key = i
        # print(l_key)
    elif i in [3, 6, 9]:
        answer += 'R'
        r_key = i
        # print(r_key)
    else:
        l_dis = abs(position.get(l_key)[0] - position.get(i)[0]) + abs(position.get(l_key)[1] - position.get(i)[1])
        r_dis = abs(position.get(r_key)[0] - position.get(i)[0]) + abs(position.get(r_key)[1] - position.get(i)[1])

        if l_dis < r_dis:
            answer += 'L'
            l_key = i
        elif r_dis < l_dis:
            answer += 'R'
            r_key = i
        elif r_dis == l_dis:
            if hand == 'left':
                answer += 'L'
                l_key = i
            elif hand == 'right':
                answer += 'R'
                r_key = i

print(answer)