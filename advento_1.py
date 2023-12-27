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

def day_two():
    RED = 12
    BLUE = 14
    GREEN = 13
    file = open("day_2.txt")
    line = file.readline()
    dicionario = {"red" : RED, "green" : GREEN, "blue" : BLUE}
    sum = 0
    while line:
        game_ = True
        list_game_games = line.split(":")
        list_game_games[0] = list_game_games[0].replace("Game ", "")
        list_games = list_game_games[1].split(";")
        for game in list_games:
            list_tudo_separadinho = game.replace(",", "").replace("\n", "").split(" ")
            for i in range(len(list_tudo_separadinho) - 1):
                if (list_tudo_separadinho[i + 1] in dicionario.keys()) and (dicionario[list_tudo_separadinho[i + 1]] < int(list_tudo_separadinho[i])):
                    game_ = False
        if game_:
            sum += int(list_game_games[0])
        line = file.readline()
    return sum

def day_three():
    vetor = [-1, 0, 1]
    file = open("day_3.txt")
    previous_line = file.readline()
    line = file.readline()
    next_line = file.readline()
    soma = []
    soma_mesmo = 0
    while line:
        previous_line = previous_line.replace("\n", "")
        line = line.replace("\n", "")
        next_line = next_line.replace("\n", "")
        for i, char in enumerate(line):
            if char in "*":
                for v in vetor:
                    if i + v >= 0 and i + v < len(previous_line):
                        if previous_line[i + v] in "1234567890":
                            num = int(day_three_aux(previous_line, i+v))
                            soma.append(num)
                            if previous_line[i] != ".":
                                break
                for v in vetor:
                    if i + v >= 0 and i + v < len(line):
                        if line[i + v] in "1234567890":
                            num = int(day_three_aux(line, i+v))
                            soma.append(num)  
                for v in vetor:
                    if i + v >= 0 and i + v < len(next_line):
                        if next_line[i + v] in "1234567890":
                            num = int(day_three_aux(next_line, i+v))
                            soma.append(num)
                            if next_line[i] != ".":
                                break
            if len(soma) == 2:
                soma_mesmo += soma[0] * soma[1]
            soma = []
        previous_line = line
        line = next_line
        next_line = file.readline()
    return soma_mesmo

def day_three_aux(line, i):
    num = line[i]
    if line[i-1] in "1234567890":
        num = line[i-1] + num
        if line[i-2] in "1234567890":
            num = line[i-2] + num
            return num
        if line[i+1] in "1234567890":
            num = num + line[i+1]
            return num
    if line[i+1] in "1234567890":
        num = num + line[i+1]
        if line[i+2] in "1234567890":
            num = num + line[i+2]
            return num
    return num

print(day_three())