def day_one():
    dicionario = {"twone" : "21", "threeigth" : "38",  "nineight" : "98", "sevenine" : "79", "oneight" : "18",
                   "fiveight" : "58", "eighthree" : "83", "eightwo" : "82",   "one" : "1", "two" : "2",
                    "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    file = open("day_1.txt")
    line = file.readline()
    sum = 0
    first = ""
    last = ""
    while line:
        for key in dicionario.keys():
            line = line.replace(key, dicionario[key])
        for i in line:
            if i.isdigit() and first == "":
                first = i
            elif i.isdigit():
                last = i
        if last == "":
            last = first
        print(first + last)
        sum += int(first + last)
        first = ""
        last = ""
        line = file.readline()
    
    return sum

print(day_one())