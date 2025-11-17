d = {}
n = int(input("Enter no. of students: "))
for i in range(n):
    key = input("Enter roll (key): ")
    value = input("Enter name (value): ")
    d[key] = value

for key, value in d.items():
    print(f"Roll. {key} Name: {value}")
