list=[]
n=int(input("Enter the size of List: "))
print("Enter the elememts of List: ")

for i in range(0,n):
    list.append(int(input()))

x = int(input("Enter the element to be searched: "))
lower_bound = 0
upper_bound = len(list)-1
mid = (lower_bound + upper_bound)//2

while lower_bound <= upper_bound:
    if x == list[mid]:
        print("Element Found at index:\t",mid)
        break
    else:
        if x > list[mid]:
            lower_bound = mid+1 
            mid = (lower_bound+upper_bound)//2
        elif x < list[mid]: 
            upper_bound = mid-1 
            mid = (lower_bound+upper_bound)//2

if(lower_bound>upper_bound):
    print("Element Not Found")