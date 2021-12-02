# Write a program to reverse a number.
# solution 1
num = 123456
print(str(num)[::-1])

# solution 2
n = 4562
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)