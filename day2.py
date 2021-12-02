def day2a(input):
    depth = 0
    pos = 0

    lines = input.split("\n")
    for line in lines:
        if "forward" in line:
            pos = pos + int(line.split(" ")[1])
        if "down" in line:
            depth = depth + int(line.split(" ")[1])
        if "up" in line:
            depth = depth - int(line.split(" ")[1])

    print(depth * pos)


sample = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def day2b(input):
    aim = 0
    depth = 0
    pos = 0

    lines = input.split("\n")
    for line in lines:
        if "forward" in line:
            dx = int(line.split(" ")[1])
            pos = pos + dx
            depth = depth + dx*aim
        if "down" in line:
            aim = aim + int(line.split(" ")[1])
        if "up" in line:
            aim = aim - int(line.split(" ")[1])

    print(depth * pos)


day2b(sample)
with open('day2.txt', 'r') as f:
    contents = f.read()
    day2b(contents)
