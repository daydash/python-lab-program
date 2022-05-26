def fun_gcd(a,b):
    if(b==0):
        return a
    else:
        return fun_gcd(b,a%b)
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
print("The GCD of two numbers are:",fun_gcd(a,b))
