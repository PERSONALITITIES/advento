def set_up(dia):
    file = open("day_" + str(dia) + ".txt")
    line = file.readline()
    return (file, line)

def day_one():
    file, line = set_up(1)
    max_ = [0, 0, 0]
    sum_ = 0
    while line:
        if line != "\n":
            sum_ += int(line)
        else:
            max_ = sorted(max_)
            if max_[0] < sum_:
                max_[0] = sum_
            sum_ = 0
        line = file.readline()
    max_ = sorted(max_)
    if max_[0] < sum_:
        max_[0] = sum_
    return sum(max_)

def day_two():
    file, line = set_up(2)
    matchups = {"AX":"C", "AY":"A", "AZ":"B", "BX":"A", "BY":"B", "BZ":"C", "CX":"B", "CY":"C", "CZ":"A"}
    game_values = {"X":0, "Y":3, "Z":6}
    hand_values = {"A":1, "B":2, "C":3}
    soma = 0
    while line:
        line = line.replace(" ", "").replace("\n", "")
        soma += game_values[line[1]] + hand_values[matchups[line]]
        line = file.readline()
    return soma

def day_four():
    file, line = set_up(4)
    sum = 0
    while line:
        limites = line.replace("\n", "").split(",")
        limite1 = limites[0].split("-")
        limite2 = limites[1].split("-")
        lista1 = []
        lista2 = []
        inicio1 = int(limite1[0])
        inicio2 = int(limite2[0])
        fim1 = int(limite1[1])
        fim2 = int(limite2[1])
        while inicio1 <= fim1:
            lista1.append(str(inicio1))
            inicio1 += 1
        while inicio2 <= fim2:
            lista2.append(str(inicio2))
            inicio2 += 1
        check = any(num in lista1 for num in lista2)
        if check:
            sum += 1
        line = file.readline()
    return sum

print(day_four())