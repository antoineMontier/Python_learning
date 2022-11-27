

def printDoubleTable(list):
    #assert isinstance(list, int[][])
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end="|")
        print("")

def createPascalArray(n):
    assert n > 0 and isinstance(n, int)
    if(n == 1):
        return [[1]]
    elif(n==2):
        return [[1], [1, 1]]

    res = [[1], [1, 1], [1, 2, 1]]
    for i in range(3, n-1):
        res.append([1])
        #start of each line is 1
        for j in range(1, i):
            res[i].append(res[i-1][j-1] + res[i-1][j])
        res[i].append(1)
    return res

def fibo(n):
    assert n >= 0 and isinstance(n, int)
    if(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return fibo(n-1)+fibo(n-2)

def facto(n):
    assert n >= 0 and isinstance(n, int)
    if(n <= 1):
        return 1
    else:
        return n * facto(n-1)

def pow(x, n):
    assert isinstance(n, int) and not(x == 0 and n == 0)
    if(n == 0):
        return 1
    elif(n > 0):
        res = x
        while(n>1):
            res *= x
            n -= 1
        return res
    else:#n < 0
        res = 1/x
        while(n < -1):
            res /= x
            n += 1
        return res

def swap(a, b):#useless cause the variables are transmitted by copy
    c = a
    a = b
    b = c

def scalarproduct(l1, l2):
    assert len(l1) == len(l2)
    if len(l1) == 1:
        return l1[0]*l2[0]
    else:
        #create new array without first element :
        l1_bis = []
        l2_bis = []
        for i in range(1, len(l1)):
            l1_bis.append(l1[i])
            l2_bis.append(l2[i])
        return l1[0]*l2[0] + scalarproduct(l1_bis, l2_bis)









print("\n\n")

print(scalarproduct([1, 2, 4], [-1, 8, 3]))

print("\n\n")






