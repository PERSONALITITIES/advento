def day_one():
    file = open("day_one.txt")
    line = file.readline()
    max_ = 0
    sum_ = 0
    while line:
        if line != "\n":
            sum_ += int(line)
        else:
            max_ = max(max_, sum_)
            sum_ = 0
        line = file.readline()
    
    return max_

def day_two():
    file = open("day_2.txt")
    line = file.readline()
    matchups = {"AX":3, "AY":6, "AZ":0, "BX":0, "BY":3, "BZ":6, "CX":6, "CY":0, "CZ":3}
    values = {"X":1, "Y":2, "Z":3}
    soma = 0
    while line:
        line = line.replace(" ", "").replace("\n", "")
        soma += matchups[line] + values[line[1]]
        line = file.readline()
    return soma

print(day_one())