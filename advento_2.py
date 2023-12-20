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
        sum += int(first + last)
        first = ""
        last = ""
        line = file.readline()
    
    return sum

def day_two():
    file = open("day_2.txt")
    line = file.readline()
    sum = 0
    ZERO = 0
    dicionario = {"red" : ZERO, "green" : ZERO, "blue" : ZERO}
    while line:
        list_game_games = line.split(":")
        list_game_games[0] = list_game_games[0].replace("Game ", "")
        list_games = list_game_games[1].split(";")
        for game in list_games:
            list_tudo_separadinho = game.replace(",", "").replace("\n", "").split(" ")[1:]
            for i in range(len(list_tudo_separadinho) - 1):
                if (list_tudo_separadinho[i + 1] in dicionario.keys()) and (int(dicionario[list_tudo_separadinho[i + 1]]) < int(list_tudo_separadinho[i])):
                    dicionario[list_tudo_separadinho[i + 1]] = int(list_tudo_separadinho[i])
        sum += (int(dicionario["red"]) * int(dicionario["blue"]) * int(dicionario["green"]))
        line = file.readline()
        for key in dicionario.keys():
            dicionario[key] = ZERO
    return sum

print(day_two())