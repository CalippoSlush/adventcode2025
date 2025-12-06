with open('Day6_text', 'r') as file:
    text = file.read()
test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

def split(input):
    lines = input.split("\n")
    l = []
    for i in lines:
        i = i.split()
        l.append(i)
    return l
def part1(input):
    l = split(input)
    total = 0
    for i in range(len(l[0])):
        sum = 0
        multi = 1
        operator = l[-1][i]
        if  operator == '+':
            for j in range(len(l)-1):
                sum+=int(l[j][i])
            total += sum
        else:
            for j in range(len(l)-1):
                multi*=int(l[j][i])
            total += multi
    return total
def part2(input):
    lines = input.split("\n")
    max_len = max(len(line) for line in lines)
    l = [line.ljust(max_len, '0') for line in lines]
    start_index = 0
    line_operator = l[-1]
    total = 0
    line = ""
    for j in range(1,len(line_operator)):
        operator = line_operator[start_index]
        next_operator = line_operator[j]
        int_sum = 0
        int_multi = 1

        if next_operator == '+' or next_operator == '*':
            end_index = j
            current_range = range(start_index, end_index-1)

        elif j==len(line_operator)-1:
            end_index = j
            current_range = range(start_index, end_index+1)

        else:
            continue

        for index in current_range:
            for k in range(len(l) - 1):
                t = l[k][index]
                line += t
            if operator == '+':
                int_sum += int(line)
            else:
                int_multi *= int(line)
            line = ""
        start_index = end_index

        if operator == '+'and next_operator != ' ':
            total+=int_sum
        elif operator == '*'and next_operator != ' ':
            total+=int_multi
    return total
print("Part 1 Test : ",part1(test))
print("Part 1      : ",part1(text))
print("Part 2 Test : ",part2(test))
print("Part 2      : ",part2(text))



