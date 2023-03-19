import math
def f(x_start, x_finish):
    y = 0
    variables = []
    while x_start < x_finish: 
        if x_start > 2.5:
            y += math.sin(2.3 * x_start - 1)
        if 0 <= x_start and x_start <= 2.5:
            y += 1 - 3 * math.log10(math.fabs(1 - x_start))
        if 0 > x_start:
            y += 2 - x_start
        variables.append(round(y, 3))
        x_start += 0.2
    return variables

x_start = -math.pi/5
x_finish = 9 * math.pi/5
print(f(x_start, x_finish))
