number=int(input("Enter number : "))
print("-----------------------------------------------")
sum1=0
for i in range (number+1):
    sum1+= i
print("Sum of",number,"is : ",sum1)


fact=1
for i in range (1, number+1):
    fact=fact*i
    
print("Factorial of",number,"is : ",fact)