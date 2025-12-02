def dial_unlock_1(instructions,start_point):
    times = 0
    for i in instructions:
        direction = i[0]
        amount = int(i[1:])
        if direction == "R":
            start_point = start_point + amount
        else:
            start_point = start_point - amount
        while start_point >= 100 or start_point < 0:
            if start_point < 0:
                start_point = start_point + 100
            if start_point >= 100:
                start_point = start_point - 100
        if start_point == 0:
            times = times + 1
    return times
def dial_unlock_2(instructions,start):
    current = start
    times = 0
    for i in instructions:
        direction = i[0]
        amount = int(i[1:])
        while amount > 0:
            if direction == "L":
                current = current - 1
            else:
                current = current + 1
            amount = amount - 1
            if current == 100:
                current = 0
                times = times + 1
            if current == -1:
                current = 99
                times = times + 1

    return times
with open('Day1_text', 'r') as file:
    content = file.read()
    list_rotations = content.split()
start_point = 50
print("Part 1 : ",dial_unlock_1(list_rotations,start_point))
print("Part 2 : ",dial_unlock_2(list_rotations,start_point))
