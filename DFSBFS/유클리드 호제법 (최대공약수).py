# 유클리드 호제법으로 최대공약수 구하기
# 자연수 A, B (A>B)에 대하여 A를 B로 나눈 값 R
# 이 때 A와 B의 최대공약수는 B와 R의 최대공약수와 같음

# A    B
# 192  162
# 162  30
# 30   12
# 12   6

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192, 162))