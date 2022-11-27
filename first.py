

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

def colinear(l1, l2):
    assert len(l1) == len(l2)
    all_zero = True
    for i in range(len(l1)):
        all_zero = all_zero and l1[i] == 0

    if(all_zero):
        return True

    for i in range(len(l1) - 1):
        if(l1[i] != 0 and l1[i+1] != 0):
            if(l2[i] / l1[i] != l2[i+1]/l1[i+1]):
                return False
        elif(l1[i] != 0 and l1[i+1] == 0 and l2[i] == 0):
            return False
        elif(l1[i] == 0 and l1[i+1] != 0 and l2[i+1] == 0):
            return False
        elif(l1[i] == 0 and l1[i+1] == 0 and (l2[i+1] != 0 or l2[i] != 0)):
            return False

    return True#every test are sucessful

def max_index(list, size):
    assert len(list) >= size
    if(size == 1):
        return list[0]
    else:
        max_index = 0
        for i in range(1, size):
            if(list[max_index] < list[i]):
                max_index = i
        return max_index

def sort_max(list):
    virtual_size = len(list)
    while(virtual_size > 1):
        ind = max_index(list, virtual_size)
        maximum = list[ind]
        temp = list[virtual_size - 1]
        list[virtual_size-1] = maximum
        list[ind] = temp
        virtual_size -= 1
    return list

def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list)-1 - i):
            if(list[j]>list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list
            

        

    


        



print("\n\n")

print(  bubble_sort([7, 9, 2, 6, 7, 11, -1])  )

print("\n\n")






