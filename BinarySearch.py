n = int(input("ENTER THE NUMBER YOU WANT TO ENTER"))
arr = []

for i in range(0,n,1):
    num = int(input(f"Enter the number {i+1} "))
    arr.append(num)
arr.sort()     
print(arr)

num = int(input("NOW ENTER THE NUMBER TO DO BINARY SEARCH -> "))
found = False
left = 0
right = len(arr)-1

while left<=right:
    mid = (left + right) // 2
    if arr[mid] == num:
        found = True
        print(F"THE NUMBER YOU ENTER {num} IS FOUND AT LOCATION {mid}")
        break
    elif num > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1    
if not found:
      print(F"THE NUMBER YOU ENTER {num} IS NOT MATCH")
