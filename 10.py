def bubbleSort(List):
    n= len(List)
    for i in range(n):
        for j in range(0, n-i-1):
            if List[j]>List[j+1]:
                List[j], List[j+1] = List[j+1],List[j]


#Initialization with an empty list.
List = []
n=int(input("Enter the Number or elements of the list: "))
print("Enter the elements of the list:")
for i in range(0,n):
    List.append(int(input()))
bubbleSort(List)
print("Sorted List is:")
for i in range(len(List)):
    print(List[i])