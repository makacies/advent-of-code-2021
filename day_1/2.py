with open("./input_data.txt") as file:
    window_size = 3
    current_window_sum = 0
    current_window_start_index = 0
    increase_counter = 0
    depths = []

    for line in file:
        depths.append(int(line))

    for depth in depths:
        if len(depths) - window_size < current_window_start_index:
            break

        next_window_sum = depths[current_window_start_index] + \
            depths[current_window_start_index + 1] + \
            depths[current_window_start_index + 2]

        if next_window_sum > current_window_sum:
            increase_counter += 1

        current_window_sum = next_window_sum
        current_window_start_index += 1

print(increase_counter - 1)
