x=1
n=int(input("Enter Any Number"))
for i in range(25):
    x=x-(x*x-n)/(2*x)
print(round(x,4))