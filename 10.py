# Write a program to check common characters in two given strings.
# solution 1
s1 = "engineering"
s2 = "Apple"

a = list(set(s1) & set(s2))
print(a)
print("The common letters are:")
for i in a:
   print(i)