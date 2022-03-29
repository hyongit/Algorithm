logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]

result = 0

for i in logs:

    if len(i) > 100:
        continue

    else:
        arr = i.split(" ")
        tmp = []

        if '' in arr:
            #print(arr)
            continue
        else:
            #print(arr)
            if 'team_name' and 'application_name' and 'error_level' and 'message' in arr:
                for j in arr:
                    if j == 'team_name' or j == 'application_name' or j == 'error_level' or j == 'message' or j == ':':
                        tmp.append(j)
                    else:
                        if j.isalpha() == False or len(j) > 100:
                            continue
                        else:
                            tmp.append(j)
        if len(tmp) == 12:
            #print(tmp)
            result += 1
        

print(len(logs) - result)