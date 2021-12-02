def read_file(file_name):
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]
        return list(line.split() for line in lines)


instructions = read_file("./input_data.txt")

aim = horizontal_position = depth = 0

for direction in instructions:
    direction_value = (int)(direction[1])
    match direction[0]:
        case "forward":
            horizontal_position += direction_value
            depth += aim * direction_value
        case "down":
            aim += direction_value
        case "up":
            aim -= direction_value


print(horizontal_position * depth)
