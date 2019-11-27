def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found: #if found search operations are terminated
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
            print(pos)
    return found

testlist = [1, 2, 32, 8, 17]
print(sequentialSearch(testlist, 32))

#print(sequentialSearch(testlist, 13))
