# Write a program to reverse a list.
# solution 1
def Reverse(lst):
    lst.reverse()
    return lst
      
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

# solution 2
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
      
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))