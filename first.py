

def printDoubleTable(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end="|")
        print("")

def createPascalArray(n):
    assert n > 0 and isinstance(n, int)
    res = [[]]
    for i in range(n):
        res.append([])
        for j in range(n):
            res[i].append(j+i)
    return res



#pascal = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]

print("\n\n")

pascal = createPascalArray(1)



printDoubleTable(pascal)
    

print("\n\n")






