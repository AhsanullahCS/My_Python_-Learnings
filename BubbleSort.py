n = int(input("ENTER THE NUMBER YOU WANT TO ENTER"))
arr = []

for i in range(0,n,1):
    num = int(input(f"Enter the number {i+1} "))
    arr.append(num)

print("THE UN_SORTED ARRAY -->> ",arr)

for i in range(0,n,1):
    for j in range(0,n-i-1):
        if arr[j]  > arr[j+1]:
            temp   = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("THE SORTED ARRAY -->> ",arr)