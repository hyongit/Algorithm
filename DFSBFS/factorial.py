# 재귀함수 이용하여 factorial 구현
# 재귀함수는 스택처럼 쌓임

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))