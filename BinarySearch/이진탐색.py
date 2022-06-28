# 이진탐색

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]

m_list.sort()
start = 0
end = len(m_list)-1

print(start, end)

while start<=end:
    mid = (start+end)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid] > target:
        end = mid-1
    else:
        start = mid-1