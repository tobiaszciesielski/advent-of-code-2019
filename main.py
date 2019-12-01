def fuel(n):
    n = int(n / 3) - 2
    if n > 0:
        return n + (fuel(n))
    else:
        return 0


def day_1():
    content = open('inputs/input_day1.txt', mode='r').readlines()
    print('part 1:', sum([int(float(n) / 3) - 2 for n in content]))
    print('part 2:', sum([fuel(int(n)) for n in content]))


if __name__ == '__main__':
    day_1()
