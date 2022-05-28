# 백준 [ 괄호의 값 ]

arr = input()
str = []
stack = []
rst = 0

for i in arr:
    str.append(i)

for s in str:

    if s == ')':
        tmp = 0
        while len(stack) > 0:
            top = stack.pop()
            if top == '(':
                if tmp == 0:
                    stack.append(tmp + 2)
                    break
                else:
                    stack.append(tmp * 2)
                    break
            elif top == '[':
                print(0)
                exit(0)
            else:
                tmp += int(top)

    elif s == ']':
        tmp = 0
        while len(stack) > 0:
            top = stack.pop()
            if top == '[':
                if tmp == 0:
                    stack.append(tmp + 3)
                    break
                else:
                    stack.append(tmp * 3)
                    break
            elif top == '(':
                print(0)
                exit(0)
            else:
                tmp += int(top)

    else:
        stack.append(s)

    #print(stack)

    if not stack and s in [')', ']']:
        print(0)
        exit(0)

#print(stack)

for i in stack:
    if i == '[' or i == '(':
        print(0)
        exit(0)
    else:
        rst += i

print(rst)