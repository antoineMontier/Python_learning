

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



#pascal = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]

print("\n\n")

pascal = createPascalArray(15)



printDoubleTable(pascal)
    

print("\n\n")






