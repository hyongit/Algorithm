number = 1924
k = 2

answer = []

for num in str(number):
    while k > 0 and answer and answer[-1] < num :
        answer.pop()
        k -= 1
    answer.append(num)

print(''.join(answer[:len(answer)-k]))