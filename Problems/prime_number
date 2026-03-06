start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
primes = [num for num in range(start, end + 1)
          if num > 1 and all(num % i != 0 for i in range(2, num))]
print("Prime Numbers:", primes)