# Write a program to reverse a string.
# solution 1
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Apple"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))

# solution 2
def reverse(string):
    string = string[::-1]
    return string
  
s = "Apple"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))
