def set_up(dia):
    file = open("day_" + str(dia) + ".txt")
    line = file.readline()
    return (file, line)

def day_one():
    file, line = set_up(1)
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
    file, line = set_up(2)
    matchups = {"AX":3, "AY":6, "AZ":0, "BX":0, "BY":3, "BZ":6, "CX":6, "CY":0, "CZ":3}
    values = {"X":1, "Y":2, "Z":3}
    soma = 0
    while line:
        line = line.replace(" ", "").replace("\n", "")
        soma += matchups[line] + values[line[1]]
        line = file.readline()
    return soma

def day_four():
    file, line = set_up(4)
    sum = 0
    while line:
        limites = line.split(",")
        limite1 = limites[0].split("-")
        limite2 = limites[1].split("-")
        if (limite1[0] <= limite2[0] and limite1[1] >= limite2[1]) or (limite1[0] >= limite2[0] and limite1[1] <= limite2[1]):
            sum += 1
        line = file.readline()
    return sum

print(day_four())