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

print(day_one())