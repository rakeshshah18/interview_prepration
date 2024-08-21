number = 1234
remainder = 0
reverse1 = 0
for i in range(1, len(str(number))+1):
    remainder = number % 10
    reverse1 = reverse1 * 10 +remainder
    number = number // 10
print(reverse1)