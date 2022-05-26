# Program to multiply two matrices
A=[]
n=int(input("Enter N for N x N matrix: "))
print("Enter the element:")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)
print(A)

# Display the 2D array
print("Display Array In Matrix Form")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

B=[]
n=int(input("Enter N for N x N matrix: "))
print("Enter the element:")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print(B)

# Display the 2D array
print("Display Array In Matrix Form")
for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()


result = []
for i in range (len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] +=A[i][k] * B[k][j]

print("The Result Matrix is:")
for r in result:
    print(r)