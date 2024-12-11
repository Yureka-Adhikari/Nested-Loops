string= input("Please enter a word: ")

char= input("Please enter the letter you'd like to check: ")

i=0
count=0

while(i < len(string)):
    if (string[i]== char):
        count = count+1
    i= i + 1
    
print(f"The total number of {char} in the given word is {count}")