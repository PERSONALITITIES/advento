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

print(day_two())