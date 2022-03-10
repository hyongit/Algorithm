size = [[60, 50], [30, 70], [60, 30], [80, 40]]

a, b = 0, 0

for i in range(len(size)):
    if size[i][0] < size[i][1]:
        size[i][0], size[i][1] = size[i][1], size[i][0]

size.sort(key = lambda x : (-x[0]))
a = size[0][0]

size.sort(key = lambda x : (-x[1]))
b = size[0][1]

print(a*b)