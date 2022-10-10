# [프로그래머스] 카펫

brown, yellow = 10, 2
x, y = 0, 0
w, h = 0, 0

for i in range(1, yellow+1):
    if yellow % i == 0:
        x = int(yellow//i)
        y = i
        if (x*2)+(y*2)+4 == brown:
            w = x+2
            h = y+2
            print(w, h)
        