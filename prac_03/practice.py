with open("practicefilewk3.txt") as in_file:
    for line in in_file:
        part = line.strip().split(",")
        name = part[0]
        year = int(part[1])
        cost = part[2]
        print(f"{name}, {year}, ${cost[1:-2]}")
