num= int(input("Enter a number you would like to check: "))

if num== 0 or num == 1:
    print(num,"is not a prime number")
    
elif num>1:
    for i in range(2,num):
        
        if num % i == 0:
            print(num, "is not a prime number")
            print(i,"times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")
    
else:
    print(num, "is a negative number and thus NOT a prime number")