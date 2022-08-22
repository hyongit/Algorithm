n = int(input())
length = len(str(n))
total = 0

for i in range(length-1):
    total += 9 * 10**i * (i+1) # 0 * 10의 제곱수 * 자리수

# (n에서 10의 제곱수 빼고 + 1) * 자리 수
total = total + (((n-10**(length-1))+1) * length)

print(total)