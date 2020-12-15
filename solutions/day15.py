data_file = open('./data/data15')
numbers = list(map(lambda x: int(x), data_file.read().split(',')))
data_file.close()

def say_next(ages, last_number, i):
    new_number = 0
    ages_last = ages[last_number]
    if ages_last['occ'] > 1:
        new_number = i - ages_last['index']
        ages_last['index'] = i
    if new_number in ages:
        ages[new_number]['occ'] += 1
    else:
        ages[new_number] = {'index': i+1, 'occ': 1}
    return new_number

def get_nth_number(numbers, n):
    ages = {}
    for i, number in enumerate(numbers):
        ages[number] = {'index': i+1, 'occ': 1}
    last_number = numbers[-1]
    for i in range(len(numbers), n):
        last_number = say_next(ages, last_number, i)
    return last_number

print(get_nth_number(numbers, 2020))
print(get_nth_number(numbers, 30000000))