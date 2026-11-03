def part1():
    lines = [line.strip() for line in open("quest03_p1.txt").readlines()]
    result = 0

    for line in lines:
        line = line[::-1] # Ugly parsing, but it works :)

        for i in range(4):
            tmp = int(line[i]) * int(line[i + 5]) ** i
            result += tmp

    print(result)


def part2():
    lines = [line.strip("ISO-") for line in open("quest03_p2.txt").readlines()]
    result = 0

    for line in lines:
        value, iso = line.strip()[::-1].split()

        for index, value in enumerate(value):
            result += int(value) * int(iso[index % len(iso)]) ** index

    print(result)


def part3():
    pass


def main():
    part1()
    part2()
    part3()


if __name__ == "__main__":
    main()
