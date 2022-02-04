s = "one4seveneight"

word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

tmp = ""
answer = ""

for i in s:
    tmp += i

    if tmp in word:
        answer += str(word.index(tmp))
        tmp = ""

    elif tmp in nums:
        answer += i
        tmp = ""

    else:
        pass

print(int(answer))