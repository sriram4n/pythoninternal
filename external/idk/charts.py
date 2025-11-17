import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
values = [30, 15, 45, 10]

# -------- BAR CHART --------
plt.figure(figsize=(5,4))
plt.bar(labels, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# -------- LINE CHART --------
plt.figure(figsize=(5,4))
plt.plot(labels, values, marker='o')
plt.title("Line Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# -------- PIE CHART --------
plt.figure(figsize=(5,4))
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
