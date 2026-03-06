def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

num = int(input("Enter the number: "))

print("fibonacci series: ")
for i in fibonacci(num):
    print(i, end=" ")