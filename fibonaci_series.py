num = int(input("Enter Number: "))
n1 = 0
n2 = 1
print(n1,n2, end=" ")
for i in range(2, num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()