n = int(input("how many number you want to enter"))
arr = []
for i in range(0,n,1):
    num = int(input(f"enter the number {i+1} ->"))
    arr.append(num)
print(f"THE UNSORTED ARRAY IS {arr}")
#5 8 4 7 2 

for i in range(0,n,1):
    min = i
    for j in range(i+1,n,1):
        if(arr[min] > arr[j]):
            min = j
    if min!=i:
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp



print(f"THE FINAL SELECTION SORTED ARRAY IS {arr}")