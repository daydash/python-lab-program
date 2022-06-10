def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j=i-1
        while j >=0 and key < lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key

#list assignment    
lst=[]
n=int(input("Enter the Number of elements of the list: "))
print("Enter the elements of the list:")
for i in range(0,n):
    lst.append(int(input()))
insertionSort(lst)
print("The sorted array is:")
for i in range(len(lst)):
    print(lst[i])