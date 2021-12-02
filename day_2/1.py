def read_file(file_name):
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]
        return list(line.split(' ') for line in lines)


data = read_file("./input_data.txt")

horizontal_position = sum((int)(i[1]) for i in data if i[0] == "forward")
depth = sum((int)(i[1]) for i in data if i[0] == "down") - \
    sum((int)(i[1]) for i in data if i[0] == "up")

print(horizontal_position * depth)
