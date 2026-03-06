class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    
n = int(input("Enter the list of numbers: "))
lst = []

for i in range(n):
    value = int(input("Enter the value: "))
    lst.append(value)
print("Reversed List:")
for item in ReverseIterator(lst):
    print(item, end=" ")