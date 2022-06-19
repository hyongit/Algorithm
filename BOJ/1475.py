# 백준 [방 번호]

s = input()
nums = [0] * 10

for i in s:
    if i == '6' or i == '9':
        nums[6] += 1
    else:
        nums[int(i)] += 1

nums[6] = (nums[6]+1)//2
print(max(nums))

