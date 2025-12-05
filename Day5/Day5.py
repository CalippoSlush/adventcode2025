test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
with open('Day5_text', 'r') as file:
    content = file.read()
    text = content

def remove_dups(list):
    start = [list[0]]
    n = len(list)
    if n <= 1:
        return list
    for i in range(1,n):
        if list[i] != list[i-1]:
            start.append(list[i])
    return start
def get_numbers(list):
    i = 0
    ID = []
    last_index = 0
    while list[i] != '' and i < len(list) - 1:
        ID_range = list[i].split("-")
        for j in ID_range:
            ID.append(int(j))
        last_index = i
        i += 1
    return ID , last_index
def part1(input):
    input_split = input.split("\n")
    num,start = get_numbers(input_split)
    total = 0
    for i in range(start+2, len(input_split)):
        for j in range(0,len(num),2):
            n = input_split[i]
            if not n: continue
            if num[j] <= int(n) <= num[j + 1]:
                total += 1
                break
    return total
def part2(input):
    input_split = input.split("\n")
    num, _ = get_numbers(input_split)
    all_pair = []
    total = 0
    for i in range(0, len(num), 2):
        x = num[i]
        y = num[i+1]
        j=0
        while j < len(all_pair):
            if x>all_pair[j+1] or y<all_pair[j]:
                j+=2
            else:
                x = min(x,all_pair[j])
                y = max(y,all_pair[j+1])
                all_pair.pop(j)
                all_pair.pop(j)
        all_pair.append(x)
        all_pair.append(y)
    for i in range(0,len(all_pair),2):
        total += all_pair[i+1]-all_pair[i]+1
    return total

print("Part 1 Test : ",part1(test))
print("Part 1      : ",part1(text))
print("Part 2 Test : ",part2(test))
print("Part 2      : ",part2(text))
