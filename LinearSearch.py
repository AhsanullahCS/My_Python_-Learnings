n = int(input("how many number you want to enter"))
arr = []
for i in range(n):
    num = int(input(f"enter the number {i+1} ->"))
    arr.append(num)
print(arr)

num = int(input("Give number to do Linear Search"))
found = False
location = -1

for i in range(0,n,1):
    if arr[i] == num:
        found = True
        location = i
        break

if found:
    print(f"THE NUMBER YOU ENTER IS AT THE LOCATION ->{location}")
else:
    print("THE NUMBER YOU ENTER IS NOT FOUND")
