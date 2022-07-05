# [백준] 균형잡힌 세상
# 문자열

def right(msg):
    stack = []

    for i in msg:
        # (, [ 일 때는 스택에 삽입
        if i in ['(', '[']:
            stack.append(i)

        # ), ] 일 때
        elif i in [')', ']']:
            # ) 이고 stack에 괄호가 있을 경우
            if i == ')' and len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
            
            # ] 이고 stack에 괄호가 있을 경우
            elif i == ']' and len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'

            # stack에 여는 괄호가 없는 채로 닫는 괄호 들어 왔을 경우
            else:
                return 'no'

        # 괄호 외의 문자가 들어왔을 때
        else:
            continue

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

while True:
    str = input()
    
    if str == '.':
        break

    print(right(str))