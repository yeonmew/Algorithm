for _ in range(int(input())): #T개의 테스트 데이터
    data = input()
    res = 'YES'
    stk = []
    for i in data:
        if i == '(':
            stk.append(i)
        else:
            if len(stk) == 0:
                res = 'NO'
            else:
                stk.pop()

    if len(stk) != 0:
        res = 'NO'

    print(res)

