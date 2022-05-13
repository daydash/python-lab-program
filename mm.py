R1 = int(input("Enter the number of rows in 1st matrix: "))
C1 = int(input("Enter the number of columns in 1st matrix: "))

A = []
print("Enter the values in 1st matrix:")

for i in range(R1):
    a = []
    for j in range(C1):
         a.append(int(input()))
    A.append(a)
 
R2 = int(input("Enter the number of rows in 2nd matrix: "))
C2 = int(input("Enter the number of columns in 2nd matrix: "))

B = []
print("Enter the values in 2nd matrix:")

for i in range(R2):
    b = []
    for j in range(C2):
         b.append(int(input()))
    B.append(b)
     
result = []

for i in range(R1):
    res = []
    for j in range(C2):
         res.append(0)
    result.append(res)

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("\nFinal Matrix is:\n")
for r in result:
    print(r)