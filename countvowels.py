s = input("Enter a string: ")
count = 0

print("Vowels are:")

for ch in s:
    if ch in "aeiouAEIOU":
        print(ch, end=" ")
        count += 1

print()
print("Number of vowels:", count)