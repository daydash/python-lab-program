n=int(input("Enter Any Number: "))
p=int(input("Enter Exponent: "))
pow=1
for i in range(1,p+1):
    pow=pow*n
print("The power of given number is: ",pow)