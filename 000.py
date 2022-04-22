
def nextNum(n):
    return n+sum([int(e) for e in str(n)])
def solve(n):
    river1 = set()
    river3 = set()
    river9 = set()
    cur = 1
    #暴力计算第1条数字河流
    for i in range(100000):
        river1.add(cur)
        cur = nextNum(cur)
    cur = 3
    #暴力计算第9条数字河流
    for i in range(100000):
        river3.add(cur)
        cur = nextNum(cur)
    cur = 9
    #暴力计算第9条数字河流
    for i in range(100000):
        river9.add(cur)
        cur = nextNum(cur)
    condition = [False,False,False]
    cur = n
    #暴力计算第n条数字河交汇于哪一条
    for i in range(10000):
        if cur in river1 and condition[0] == False:
            print('first meet river 1 at',cur)
            condition[0] = True
        if cur in river3 and condition[1] == False:
            print('first meet river 3 at',cur)
            condition[1] = True
        if cur in river9 and condition[2] == False:
            print('first meet river 9 at',cur)
            condition[2] = True
        if all(e == True for e in condition):
            print("与1、3、9都相交")
            break
        cur = nextNum(cur)

solve(1235)