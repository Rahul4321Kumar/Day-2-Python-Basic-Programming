# Write a program to remove duplicates from the list.
# solution 1
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))

# solution 2
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))