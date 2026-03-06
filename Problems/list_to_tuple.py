n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)
result = [(i, lst[i]) for i in range(len(lst))]
print("List of tuples:")
print(result)