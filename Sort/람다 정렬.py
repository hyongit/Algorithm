#정렬 라이브러리 key 매개변수로 람다 함수 사용

arr = [('사과',5), ('바나나',2), ('당근',3)]

# arr.sort(key = lambda x : x[1])
result = sorted(arr, key = lambda x : x[1])
print(result)