input = """16100064-16192119,2117697596-2117933551,1-21,9999936269-10000072423,1770-2452,389429-427594,46633-66991,877764826-877930156,880869-991984,18943-26512,7216-9427,825-1162,581490-647864,2736-3909,39327886-39455605,430759-454012,1178-1741,219779-244138,77641-97923,1975994465-1976192503,3486612-3602532,277-378,418-690,74704280-74781349,3915-5717,665312-740273,69386294-69487574,2176846-2268755,26-45,372340114-372408052,7996502103-7996658803,7762107-7787125,48-64,4432420-4462711,130854-178173,87-115,244511-360206,69-86"""
test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
def list(input):
    last = 0
    range = ""
    output = []
    for i in input:
        if i != ",":
            range +=i
        else:
            output.append(range)
            range = ""
    output.append(range)
    return output

print("List : ",list(input))
def numbers(range):
    num1 = ""
    num2 = ""
    flag = False
    for i in range:
        if i != "-" and not flag:
            num1 += i
        elif flag:
            num2 += i
        else:
            flag = True
            continue
    num1 = int(num1)
    num2 = int(num2)
    return num1,num2

def check_invalid_1(number):
    number = str(number)
    half = int(len(number)/2)
    return number[:half] == number[half:]
def sum_invalid_1(input):
    num = list(input)
    sum = 0
    for i in num:
        (x , y) = numbers(i)
        for j in range(x,y+1):
            if check_invalid_1(j):
                sum += j
    return sum
print("Part 1 Test : " , sum_invalid_1(test))
print("Part 1 :      " ,sum_invalid_1(input))
def split_in(input,leng):
    output = []
    n = ""
    for i in input:
        n += i
        if len(n) == leng:
            output.append(n)
            n = ""
    return output
def check_invalid_2(number):
    number = str(number)
    max_length = int(len(number) / 2)
    flag = False
    for i in range(1,max_length+1):
        if len(number)%i != 0:
            continue
        if flag:
            return flag
        current = number[:i]
        check = split_in(number,len(current))
        for i in check:
            if i != current:
                flag = False
                break
            else:
                flag = True

    return flag

def sum_invalid_2(input):
    num = list(input)
    sum = 0
    for i in num:
        (x, y) = numbers(i)
        for j in range(x, y + 1):
            if check_invalid_2(j):
                sum += j
    return sum
print("Part 2 Test : ",sum_invalid_2(test))
print("Part 2 :      ",sum_invalid_2(input))


