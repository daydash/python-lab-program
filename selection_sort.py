List = []
n = int(input("Enter Size Of List: "))
print("Enter the elements of the list")
for i in range(0,n):
    List.append(int(input()))
for i in range(0,n):
    pos = i
    min = List[i]
    for j in range(i,n):
        if List[j] < min:
            min = List[j]
            pos = j
    temp = List[i]
    List[i] = List[pos]
    List[pos] = temp
print("List after sorting:", List)