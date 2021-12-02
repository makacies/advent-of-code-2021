with open("./input_data.txt") as file:
    increase_counter = 0
    current_depth = 0
    for line in file:
        coming_depth = int(line)
        if coming_depth > current_depth:
            increase_counter += 1
        current_depth = coming_depth

print(increase_counter - 1)
