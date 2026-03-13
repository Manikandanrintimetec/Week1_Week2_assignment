import numpy as np
import matplotlib.pyplot as plt
random_numbers = np.random.randint(1, 101, size=1000)
print(random_numbers)
unique_numbers, counts = np.unique(random_numbers, return_counts=True)
frequency_table = dict(zip(unique_numbers, counts))
print(frequency_table)

# Extract x and y values from frequency table
numbers = list(frequency_table.keys())
counts = list(frequency_table.values())

# Plot histogram
plt.figure(figsize=(12, 5))
plt.bar(numbers, counts, color='lightblue')
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers")
plt.show()


# Step 4: Retain top 5 most frequent numbers and combine the rest as 'Other'
# Sort numbers by frequency descending
sorted_numbers = sorted(frequency_table, key=frequency_table.get, reverse=True)
top5_numbers = sorted_numbers[:5]

# Create new frequency table with Top 5 + Other
new_frequency = {}
other_count = 0
for num, count in frequency_table.items():
    if num in top5_numbers:
        new_frequency[num] = count
    else:
        other_count += count
new_frequency['Other'] = other_count

print("Top 5 + Other Frequency Table:")
print(new_frequency)

# Step 5: Plot histogram for Top 5 + Other
# Convert all x labels to strings (important for 'Other')
x_labels = [str(k) for k in new_frequency.keys()]
y_values = list(new_frequency.values())

plt.figure(figsize=(8, 5))
plt.bar(x_labels, y_values, color='skyblue')
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.title("Histogram: Top 5 Most Frequent Numbers + Other")
plt.show()