def day_one():
    file = open("day_1.txt")
    line = file.readline()
    sum = 0
    first = ""
    last = ""
    while line:
        for i in line:
            if i.isdigit() and first == "":    # O PILO É MEIO GAY
                first = i
            elif i.isdigit():
                last = i
        if last == "":
            last = first
        sum += int(first + last)
        first = ""
        last = ""
        line = file.readline()
    
    return sum

print(day_one())