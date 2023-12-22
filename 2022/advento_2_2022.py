def day_one():
    file = open("day_one.txt")
    line = file.readline()
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
    file = open("day_2.txt")
    line = file.readline()
    matchups = {"AX":"C", "AY":"A", "AZ":"B", "BX":"A", "BY":"B", "BZ":"C", "CX":"B", "CY":"C", "CZ":"A"}
    game_values = {"X":0, "Y":3, "Z":6}
    hand_values = {"A":1, "B":2, "C":3}
    soma = 0
    while line:
        line = line.replace(" ", "").replace("\n", "")
        soma += game_values[line[1]] + hand_values[matchups[line]]
        line = file.readline()
    return soma

print(day_one())