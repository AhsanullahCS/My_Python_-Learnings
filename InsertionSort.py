# j K
# 6 4 2 1 
# 4 6 2 1 
# 4 4 6 1
# 1 2 4 6
n = int(input("How many numbers do you want to enter? "))
arr = []

for i in range(n):
    num = int(input(f"Enter number {i+1} -> "))
    arr.append(num)

print(f"Unsorted Array: {arr}")

for i in range(1,len(arr)):
    key = arr[i]
    j = i-1

    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j = j - 1

        arr[j + 1] = key

print(arr)                                         