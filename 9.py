# Write a program to swap the first and last item of a list.
# solution 1
def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     

newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# solution 2
def swapList(list):
     
    first = list.pop(0)  
    last = list.pop(-1)
     
    list.insert(0, last) 
    list.append(first)  
     
    return list
     

newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))