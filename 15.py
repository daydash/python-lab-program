n=int(input("Enter Any Number: "))
rev=n
palindrome=0
while rev>0:
    a=rev%10
    # print("a=",a)
    palindrome=palindrome*10+a
    # print("palindrome=",palindrome) 
    rev=rev//10
    # print("reverse=",rev)
if n==palindrome:
    print(n, " is palindrome")
else:
    print(n, " is not palindrome")