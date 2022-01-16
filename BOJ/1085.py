x, y, w, h = map(int, input().split())
n = min(x, y)
m = w - x
k = h - y

a = n - 0
b = min(m, k)

print(min(a, b))


########################################

x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y))
