def solution(new_id):
    tmp = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if i.islower() or i.isdigit() or i in ['-', '_', '.']:
            tmp += i
    new_id = tmp

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]

    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id = new_id.replace('', 'a')

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

print(solution('...!@BaT#*..y.abcdefghijklm'))