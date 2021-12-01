with open('./2020/data/data01') as data_file:
    data = sorted(map(int, data_file.read().split()))

while len(data) > 1:
    sum = data[0] + data[-1]
    if sum > 2020:
        del data[-1]
    elif sum < 2020:
        del data[0]
    else:
        print('The answer is: {0}+{1}={2}, {0}*{1}={3}'.format(data[0], data[-1], sum, data[0]*data[-1]))
        break