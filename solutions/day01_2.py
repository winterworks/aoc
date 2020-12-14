with open('./data/data1') as data_file:
    data = sorted(map(int, data_file.read().split()))

i = 1
j = -1

while len(data) > 2:
    sum = data[0] + data[i] + data[j]
    if sum > 2020:
        if i == 1:
            del data[j]
            j = -1
        else:
            i = 1
            j -= 1
    elif sum < 2020:
        if i == len(data)-3:
            del data[0]
            j = -1
            i = 1
        else:
            i += 1
    else:
        print('The answer is: {0}+{1}+{2}={3}, {0}*{1}*{2}={4}'.format(data[0], data[i], data[j], sum, data[0]*data[i]*data[j]))
        break

