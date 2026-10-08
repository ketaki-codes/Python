s = input("Enter a string: ") # enter the string
count = 0

print("Vowels are:") 

for ch in s:                  # put ch in s
    if ch in "aeiouAEIOU":    #ch as aeiou
        print(ch, end=" ")    #print which voewls is
        count += 1          # counting of vowels

print()
print("Number of vowels:", count) #num of vowels