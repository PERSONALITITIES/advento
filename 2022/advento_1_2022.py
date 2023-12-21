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

print(day_one())