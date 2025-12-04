with open('Day3_text', 'r') as file:
    content = file.read()
    list_batteries = content.split()
print(list_batteries)
test = """987654321111111,811111111111119,234234234234278,818181911112111"""
test = test.split(",")
def find_max_1(batterie):
    maximum = 0
    max_index = 0
    for i in range(len(batterie)-1):
        num = int(batterie[i])
        if num > maximum:
            maximum = num
            max_index = i
    second = 0
    for i in range(max_index+1, len(batterie)):
        num = int(batterie[i])
        if num > second:
            second = num
    return maximum*10 + second
def sumJoltage1(l):
    total = 0
    for i in l:
        total += find_max_1(i)
    return total


def find_max_2(batterie):
    maximum = 0
    max_index = 0
    output = ""
    last_index = 0
    for i in range(0,len(batterie)-11):
        num = int(batterie[i])
        if num > maximum:
            maximum = num
            max_index = i
    output += str(maximum)
    #How many can I drop?
    drop = len(batterie)-12-max_index
    while drop != 0 and len(output)!=12:
        maximum = 0
        last = max_index+1+drop+1#last index to check according to maximum we can drop
        if last > len(batterie):
            last = len(batterie)
        for j in range(max_index+1,last):
            num = int(batterie[j])
            if num > maximum:
                maximum = num
                last_index = j
        drop -= (last_index - (max_index + 1)) #Rest amount of drops
        max_index = last_index
        output += str(maximum)
    if drop == 0:
        output += batterie[max_index+1:]
    return int(output)
def sumJoltage2(l):
    total = 0
    for i in l:
        total += find_max_2(i)
    return total

print("Part 1 Test : ",sumJoltage1(test))
print("Part 1      : ",sumJoltage1(list_batteries))
print("Part 2 Test : ",sumJoltage2(test))
print("Part 2      : ",sumJoltage2(list_batteries))