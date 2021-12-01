data_file = open('./2020/data/data09')
data = list(map(lambda r: int(r), data_file.read().split('\n')))
data_file.close()

def is_sum_of_two(value_sum, value_list):
    for value in value_list:
        if value_sum - value in value_list:
            return True

def find_invalid(rows, preamble):
    invalid = []
    for i in range(preamble, len(rows)):
        if not is_sum_of_two(rows[i], rows[i-preamble:i]):
            invalid.append(i)
    return invalid

def find_range_with_sum(rows, value):
    for i, start_row in enumerate(rows):
        range_sum = 0
        end_row = i
        while end_row < len(rows) and range_sum < value:
            range_sum += rows[end_row]
            end_row += 1
            if range_sum == value:
                return rows[i:end_row]

invalid_value = data[find_invalid(data, 25)[0]]
print(invalid_value)
range_for_sum = find_range_with_sum(data, invalid_value)
print(min(range_for_sum) + max(range_for_sum))