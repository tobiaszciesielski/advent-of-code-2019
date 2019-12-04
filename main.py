import re
import time


def day_3():
    def create_surface(moves_1, moves_2):
        current_horizontal = 0
        current_vertical = 0
        u_1, d_1, l_1, r_1 = 0, 0, 0, 0
        for m in moves_1:
            direction, steps = m

            if direction == 'U':
                current_horizontal += steps
                if current_horizontal > u_1:
                    u_1 = current_horizontal

            elif direction == 'D':
                current_horizontal -= steps
                if current_horizontal < d_1:
                    d_1 = current_horizontal

            elif direction == 'R':
                current_vertical += steps
                if current_vertical > r_1:
                    r_1 = current_vertical

            elif direction == 'L':
                current_vertical -= steps
                if current_vertical < l_1:
                    l_1 = current_vertical

        current_horizontal = 0
        current_vertical = 0
        u_2, d_2, l_2, r_2 = 0, 0, 0, 0
        for m in moves_2:
            direction, steps = m
            if direction == 'U':
                current_horizontal += steps
                if current_horizontal > u_1:
                    u_2 = current_horizontal

            elif direction == 'D':
                current_horizontal -= steps
                if current_horizontal < d_2:
                    d_2 = current_horizontal

            elif direction == 'R':
                current_vertical += steps
                if current_vertical > r_2:
                    r_2 = current_vertical

            elif direction == 'L':
                current_vertical -= steps
                if current_vertical < l_2:
                    l_2 = current_vertical

        u_max = max(abs(u_1), abs(u_2))
        d_max = max(abs(d_1), abs(d_2))
        r_max = max(abs(r_1), abs(r_2))
        l_max = max(abs(l_1), abs(l_2))
        matrix_size = (u_max+d_max + 1, r_max + l_max + 1)
        matrix = [['.' for _ in range(matrix_size[1])] for __ in range(matrix_size[0])]
        starting_point = (u_max, l_max)
        matrix[starting_point[0]][starting_point[1]] = 'o'

        return matrix, starting_point

    def allocate_wire(matrix, starting_point, moves, sign):
        crossing_points = []
        x, y = starting_point  # current position
        for move in moves:
            direction, steps = move
            if direction == 'U':
                for n in range(1, steps + 1):
                    val = matrix[x - n][y]
                    if val == '.':
                        matrix[x - n][y] = sign
                    elif val != sign:
                        matrix[x - n][y] = '+'
                        crossing_points.append((x - n, y))
                x, y = (x - steps, y)
            elif direction == 'D':
                for n in range(1, steps + 1):
                    val = matrix[x + n][y]
                    if val == '.':
                        matrix[x + n][y] = sign
                    elif val != sign:
                        matrix[x + n][y] = '+'
                        crossing_points.append((x + n, y))
                x, y = (x + steps, y)
            elif direction == 'L':
                for n in range(1, steps + 1):
                    val = matrix[x][y - n]
                    if val == '.':
                        matrix[x][y - n] = sign
                    elif val != sign:
                        matrix[x][y - n] = '+'
                        crossing_points.append((x, y - n))
                x, y = (x, y - steps)
            elif direction == 'R':
                for n in range(1, steps + 1):
                    val = matrix[x][y + n]
                    if val == '.':
                        matrix[x][y + n] = sign
                    elif val != sign:
                        matrix[x][y + n] = '+'
                        crossing_points.append((x, y + n))
                x, y = (x, y + steps)

        return crossing_points

    def compute_min_manhattan_distance(matrix, starting_point, crossing_points):
        central_x, central_y = starting_point
        return min([abs(central_x - x) + abs(central_y - y) for x, y in crossing_points])

    content = open('inputs/input_day3.txt', mode='r').readlines()
    wires = []
    for i in range(2):
        wires.append([(p[0], int(p[1])) for p in re.findall('([UDLR])(\d+)', content[i])])

    surface, central_port = create_surface(wires[0], wires[1])
    allocate_wire(surface, central_port, wires[0], sign='#')
    crossing_points = allocate_wire(surface, central_port, wires[1], sign='*')

    print(compute_min_manhattan_distance(map, central_port, crossing_points))



def day_2():
    def compute(index_1, index_2):
        content = open('inputs/input_day2.txt', mode='r').read()
        program = [int(x) for x in content.split(sep=',')]
        program[1] = index_1
        program[2] = index_2
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
        return program[0]

    for i in range(0, 100):
        for j in range(0, 100):
            res = compute(index_1=i, index_2=j)
            if res == 19690720:
                print(res, 'is created with', i, j, 'solution is', 100*i+j)
                break


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
    start = time.time()
    day_1()
    day_2()
    day_3()
    day_4()
    end = time.time()
    print(end - start)
