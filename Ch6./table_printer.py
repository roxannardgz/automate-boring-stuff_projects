## table printer

def printTable(theTable):
    
    #loop through all items and get max len
    max_len = []
    for lists in theTable:
        max_list = 0
        for item in lists:
            if len(item) > max_list:
                max_list = len(item)
        max_len.append(max_list)


    #right justify itmes based of max_len
    for i in range(len(theTable)):
        for j in range(len(theTable[0])):
            theTable[i][j] = theTable[i][j].rjust(max_len[i])
        
    #prints transposed table
    for i in range(len(theTable[0])):
        print(' '.join(row[i] for row in theTable))

    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)
