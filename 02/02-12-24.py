a = []
b = []
file = open(r"Aoc\02\input.txt", "r")
try:
    while True:
        content=file.readline()
        tmp = content.split()
        a.append(tmp)
        if not content:
            break
except ValueError as e:
    print(tmp)
	
file.close()

def safe_inc(arr):
    if int(arr[0])>int(arr[1]):
        return False
    for i in range(1,len(arr)):
        if 3 >= int(arr[i]) - int(arr[i-1]) >= 1 :
            continue
        else:
            return False
    return True

def safe_dec(arr):
    if int(arr[0]) == int(arr[1]):
        return False
    for i in range(len(arr)-1):
        if 3 >= int(arr[i]) - int(arr[i+1]) >= 1:
            continue
        else:
            return False
    return True


# ma = [[7, 6, 4, 2, 1],[1, 2, 7, 8, 9],[9, 7, 6, 2, 1],[1, 3, 2, 4, 5],[8, 6, 4, 4, 1],[1, 3, 6, 7, 9]]


safe = 0
for arr in a[:1000]:
    removed = False
    for i in range(len(arr)):
        if removed:break
        tmp = arr[:i]+arr[i+1:]
        if safe_inc(tmp) or safe_dec(tmp) :
            safe += 1
            removed = True
    

print(safe)
   
