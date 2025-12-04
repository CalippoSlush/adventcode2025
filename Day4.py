with open('Day4_text_test', 'r') as file:
    content = file.read()
    test = content.replace("\n", "")
with open('Day4_text', 'r') as file:
    content = file.read()
    input = content.replace("\n", "")
test = list(test)
input = list(input)
def part1(test,size):
    check = 0
    for i in range(len(test)):
        total = 0
        if test[i]=="@":
            if i % size == 0:
                index_check = [-size, -size + 1, 1, size, size + 1]
            elif i % size == size - 1:
                index_check = [-size - 1, -size, -1, size - 1, size]
            else:
                index_check = [-size - 1, -size, -size + 1, -1, 1, size - 1, size, size + 1]
            for j in index_check:
                ID = i + j
                if ID < 0 or ID >= len(test):
                    continue
                if test[ID] == "@":
                    total += 1
            if total < 4:
                check += 1
    return check

def find_removes(test,size):
    remove =[]
    for i in range(len(test)):
        total = 0
        if test[i] == "@":
            if i % size == 0:
                index_check = [-size, -size + 1, 1, size, size + 1]
            elif i % size == size - 1:
                index_check = [-size - 1, -size, -1, size - 1, size]
            else:
                index_check = [-size - 1, -size, -size + 1, -1, 1, size - 1, size, size + 1]
            for j in index_check:
                ID = i + j
                if ID < 0 or ID >= len(test):
                    continue
                if test[ID] == "@":
                    total += 1
            if total < 4:

                remove.append(i)
    return remove
def removed(test,index):
    for i in index:
        test[i]= "."
    return test
def part2(test,size):
    can_rem = find_removes(test, size)
    total = 0
    while len(can_rem)>0:
        can_rem = find_removes(test,size)
        total+= len(can_rem)
        test = removed(test,can_rem)
    return total
print("Part 1 Test : ",part1(test,10))
print("Part 1      : ",part1(input,135))
print("Part 2 Test : ",part2(test,10))
print("Part 2      : ",part2(input,135))


