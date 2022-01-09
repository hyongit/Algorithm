word = input().strip().upper()
li = []
cnt = 0
word_li = list(set(word))

for i in word_li:
    li.append(word.count(i))

if li.count(max(li)) > 1:
    print('?')
else:
    print(word_li[li.index(max(li))])

