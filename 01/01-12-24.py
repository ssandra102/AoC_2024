
a = []
b = []
file = open(r"Aoc\01\input.txt", "r")
try:
    while True:
        content=file.readline()
        tmp = content.split("   ")
        a.append(int(tmp[0]))
        b.append(int(tmp[-1].replace('\n','')))
        if not content:
            break
except ValueError as e:
    print(tmp)
	
file.close()

print(len(a))
print(len(a))

a.sort()
b.sort()

total = 0
for i in zip(a,b):
    diff = abs(i[0]-i[1])
    total += diff

print(total)
similarity = 0

for i in a:
    appears = 0
    for j in b:
        if i == j:
            appears += 1
    score = i*appears
    similarity += score

print(similarity)