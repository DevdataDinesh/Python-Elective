n = int(input("Enter the number of key-value pairs in the dictionary: "))
d = {}
for i in range(n):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    d[keys] = values
print("Original dictionary : ",d)
new_d = {}
for key, value in d.items():
    new_d[value] = key
print("New dictionary after interchanging key and value: ",new_d)