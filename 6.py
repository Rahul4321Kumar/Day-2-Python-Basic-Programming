# Write a program to count occurrences of a given character in a string.
# solution 1
def count(s, c) :
     
   
    res = 0
     
    for i in range(len(s)) :
         
        
        if (s[i] == c):
            res = res + 1
    return res
     
     

str= "Engineering"
c = 'e'
print(count(str, c))

# solution 2
my_string = "engineering"
my_char = "r"

print(my_string.count(my_char))