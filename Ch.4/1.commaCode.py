# Comma Code

#create a string with the values of the list, separated by comma and 'and'
def commaCode (theList):
    newList = ''
    long = len(theList)
    
    #check the length of the list
    if long == 1:
        print(theList[0])
    elif long == 0:
        print('Your list is empty.')
    else:
        for i in range(len(theList) - 2):
            newList += theList[i] + ', '
        
        newList = newList + theList[long-2] + ' and ' + theList[long-1]
            
        print(newList)


#create the list
print('Intorduce the values for your list. Press enter (empty string) to finish the list.')

listValue = 1
counter = 1
theList = []

#add input value to the list
while listValue:
    listValue = input('Value # ' + str(counter) + ': ')
    if listValue != '':
        theList.append(listValue)
        counter += 1
    

commaCode(theList)
