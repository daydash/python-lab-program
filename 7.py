list=[]
n=int(input("Enter the size of List: "))
print("Enter the elememts of List: ")

for i in range(0,n):
    list.append(int(input()))
max=list[0]
print(f"initial_max={max}")
for i in range(1,n):
    if list[i]>max:
        max=list[i]
        print(f"max={max}")
        print(list[i])
print(f"Maximum element of the list is {max}")