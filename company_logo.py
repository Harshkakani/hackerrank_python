a = input()

arr = []
for letter in a:
    count = 0
    for i in range(len(a)):
        if a[i] == letter:
            count += 1
    arr.append((letter, count))

arr = list(set(arr))
arr.sort(key=lambda x: x[1])
arr = arr[::-1]
for i in range(len(arr)-1):
    if arr[i][1] == arr[i+1][1]:
        if ord(arr[i][0]) > ord(arr[i+1][0]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            pass
    else:
        pass

for (a,b) in arr[0:3]:
    print(str(a)+' '+str(b))
