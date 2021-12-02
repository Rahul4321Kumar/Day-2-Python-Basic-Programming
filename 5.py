# Write a program to remove a given character from a string.
# solution 1
test_str = "Engineering"
  

print ("The original string is : " + test_str)
  

new_str = test_str[:2] +  test_str[3:]
  

print ("The string after removal character : " + new_str)

# solution 2
s = 'abc12321cba'

print(s.replace('a', ''))