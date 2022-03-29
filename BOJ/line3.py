num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]	
employees = ["1 development hometask",
"1 recruitment marketing",
"2 hometask",
"2 development marketing hometask",
"3 marketing",
"3 officetask",
"3 development"]

# result = [1,4,5,7]

result = []
emp_num = [0 for _ in range(num_teams)]
emp_arr = []

for i in range(len(employees)):
    emp = employees[i].split(' ')
    emp_num[int(emp[0])-1] += 1

print(emp_num)

for i in range(len(employees)):
    emp = employees[i].split(' ')
    print(emp)

    rem = 0
    office = 0


    for j in range(1, len(emp)):
        #print(emp[j])
        if emp[j] in remote_tasks:
            rem += 1
        elif emp[j] in office_tasks:
            office += 1
    
    print(rem, office)
    if rem == len(emp)-1:
        emp_arr.append([emp[0], i+1])

print(emp_arr)
tmp_num = [0 for _ in range(num_teams)]

for i in range(len(emp_arr)):
    tmp_num[int(emp_arr[i][0])-1] += 1

print(tmp_num)