list=[]
n=int(input("Enter the size of List: "))
print("Enter the elememts of List: ")

for i in range(0,n):
    list.append(int(input()))

key=int(input("Enter the number that to be searched: "))

for i in range(0,n):
    if list[i]==key:
        print(f"The element found at index: {i}")
        break
else:
    print("Element does not exist")