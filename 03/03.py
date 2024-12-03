"""day 3 - part 2 """
import re

file = open(r"\AoC\03\input.txt", 'r')
content = file.read()


# regex to find all occurances of do() OR don't() OR mul(d,d)
pattern = r"do\(\)|don\'t\(\)|mul\(\d+\,\d+\)"
matches = re.findall(pattern, content)

sum = 0
flag = True
i = 0

while i < len(matches):
    tmp1 = matches[i]
    # if do() is encountered, skip it to the immediate next mul() operation
    if matches[i] == "do()":
        i += 1
        tmp1 = matches[i]
    # if don't() is encountered, skip till do() is encountered
    # again skip by one to process immediate next mul()
    elif matches[i] == "don't()":
        while i<len(matches) and matches[i] != "do()":
            i+=1
        i += 1
        tmp1 = matches[i]

    item = (tmp1[4:-1]).split(',')
    pdt = int(item[0]) * int(item[1])
    sum += pdt
    i+=1

print(sum)