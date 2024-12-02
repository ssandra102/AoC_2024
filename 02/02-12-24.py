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
   
