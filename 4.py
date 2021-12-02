# Write a program to count the number of vowels in a String.
# solution 1
def vowel_count(str):
      
    
    count = 0
      
    
    vowel = set("aeiouAEIOU")
      
    
    for alphabet in str:
      
       
        if alphabet in vowel:
            count = count + 1
      
    print("No. of vowels :", count)
 
str = "Engineering"
  

vowel_count(str)

# solution 2
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)