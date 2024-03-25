n1 = int(input("Enter the number of key-value pairs in the dictionary D1: "))
D1 = {}
for i in range(n1):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    D1[keys] = values
n2 = int(input("Enter the number of key-value pairs in the dictionary D2: "))
D2 = {}
for i in range(n2):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    D2[keys] = values
common_keys = D1.keys() & D2.keys()
print("Common keys between D1 and D2 are:")
for key in common_keys:
    print(key)