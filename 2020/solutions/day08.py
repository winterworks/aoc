import copy

data_file = open('./2020/data/data08')
data = data_file.read().split('\n')
data_file.close()

data = list(map(lambda row: row.split(' '), data))
data = list(map(lambda row: [row[0], int(row[1])], data))

def boot(rows, return_exec_rows = False):
    accumulator = 0
    executed_rows = []
    active_row = 0
    while active_row not in executed_rows:
        executed_rows.append(active_row)
        if active_row < 0 or active_row >= len(rows):
            break
        elif rows[active_row][0] == 'acc':
            accumulator += rows[active_row][1]
            active_row += 1
        elif rows[active_row][0] == 'jmp':
            active_row += rows[active_row][1]
        else:
            active_row += 1
    return executed_rows if return_exec_rows else accumulator

def boot_fix(rows):
    for i,row in enumerate(rows):
        modified_rows = copy.deepcopy(rows)
        if modified_rows[i][0] == 'jmp':
            modified_rows[i][0] = 'nop'
        elif modified_rows[i][0] == 'nop':
            modified_rows[i][0] = 'jmp'
        if len(rows) in boot(modified_rows, True):
            return boot(modified_rows)

print(boot(data))
print(boot_fix(data))
