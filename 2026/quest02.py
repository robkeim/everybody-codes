# Not efficient, but it works 😅

from itertools import permutations


def part1():
    lines = [line.strip() for line in open("quest02_p1.txt").readlines()]

    result = 0

    for line in lines:
        for permutation in permutations(["1", "2", "3", "4", "5"]):
            match = True

            for comparison in line.split():
                left = comparison[0]
                op = comparison[1]
                right = comparison[2]

                if (op == "<" and permutation.index(left) < permutation.index(right)) or (op == ">" and permutation.index(left) > permutation.index(right)):
                    match = False
                    break

            if match:
                result += int("".join(permutation))

    print(result)


def part2():
    lines = [line.strip() for line in open("quest02_p2.txt").readlines()]

    result = 0

    for line in lines:
        for permutation in permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            match = True

            for comparison in line.split():
                left = comparison[0]
                op = comparison[1]
                right = comparison[2]

                if (op == "<" and permutation.index(left) < permutation.index(right)) or (
                        op == ">" and permutation.index(left) > permutation.index(right)):
                    match = False
                    break

            if match:
                result += int("".join(permutation))

    print(result)


def part3():
    lines = [line.strip() for line in open("quest02_p3.txt").readlines()]

    result = 0

    for line in lines:
        for permutation in permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            match = True

            for comparison in line.split():
                left = comparison[0]
                op = comparison[1]
                right = comparison[2]

                if (op == "<" and permutation.index(left) < permutation.index(right)) or (
                        op == ">" and permutation.index(left) > permutation.index(right)):
                    match = False
                    break

            if match:
                result += int("".join(permutation))

    print(result)


def main():
    part1()
    part2()
    part3()


if __name__ == "__main__":
    main()
