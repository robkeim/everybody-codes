def part1():
    values = [int(line.strip()) for line in open("quest01_p1.txt").read().split(",")]

    result = 0

    for value in values:
        size = 1

        while size * size < value:
            size += 1

        result += (size * size) - value

    print(result)


def part2():
    values = [int(line.strip()) for line in open("quest01_p2.txt").read().split(",")]

    result = 0

    for value in values:
        size = 3

        while count_border(size) < value:
            size += 1

        result += count_border(size) - value

    print(result)

def count_border(size):
    return 4 * size - 4


def part3():
    values = [int(line.strip()) for line in open("quest01_p3.txt").read().split(",")]

    result = 0

    for value in values:
        size = 3

        while count_full_with_hole(size) < value:
            size += 2

        result += count_full_with_hole(size) - value

    print(result)

def count_full_with_hole(size):
    return size * size - 1


def main():
    part1()
    part2()
    part3()


if __name__ == "__main__":
    main()
