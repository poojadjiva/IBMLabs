num=int(input("Enter a number"))
fact=1
if(num<0):
    print("Enter a positive number")
elif(num==0):
    print("factorial=1")
else:
    for i in range(1, num+1):
        fact*=i
    print("the factorial of", num, "is", fact)