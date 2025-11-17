num = 123
sum = 0

while(num > 0):
    sum += int(num % 10)
    num /= 10

print(sum)