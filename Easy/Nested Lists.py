if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    sec = sorted(set([row[1] for row in records]))[1]
    name = [i[0] for i in records if i[1] == sec]
    print(*sorted(name), sep = '\n')
