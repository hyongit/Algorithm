n = input()
length = int(len(n))
total = 0

for i in range(length-1):
    print(i)
    total += 9 * 10**i * (i+1) # 0 * 10의 제곱수 * 자리수

print(total)

# (n에서 10의 제곱수 빼고 + 1) * 자리 수
total = total + (((int(n)-10**(length-1))+1) * length)

print(total)