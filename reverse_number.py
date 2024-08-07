num = int(input("Enter number to reverse: "))
digits=0
reverse=0
for i in range(1,len(str(num))+1):
    digit= num%10
    reverse= reverse*10+digit
    num=num//10
print("Reverse of number is: ", reverse)