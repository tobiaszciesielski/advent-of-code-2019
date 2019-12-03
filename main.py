
def day_2():
    content = open('inputs/input_day2.txt', mode='r').read()
    program = [int(x) for x in content.split(sep=',')]
    program[1] = 12
    program[2] = 2
    i = 0
    while program[i] != 99:
        a = program[i + 1]
        b = program[i + 2]
        c = program[i + 3]
        if program[i] == 1:
            program[c] = program[a] + program[b]
        elif program[i] == 2:
            program[c] = program[a] * program[b]
        i += 4
    print(program[0])


def day_1():
    def fuel(n):
        n = int(n / 3) - 2
        if n > 0:
            return n + (fuel(n))
        else:
            return 0

    content = open('inputs/input_day1.txt', mode='r').readlines()
    print('part 1:', sum([int(float(n) / 3) - 2 for n in content]))
    print('part 2:', sum([fuel(int(n)) for n in content]))


if __name__ == '__main__':
    day_2()
