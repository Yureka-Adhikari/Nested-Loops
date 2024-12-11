def convertbinary(n):
    if n > 1:
        convertbinary(n//2)
    print (n%2 , end=" ")
    
dec= float(input("enter a number to find it's binary value: "))
    
convertbinary(dec)
    
print()