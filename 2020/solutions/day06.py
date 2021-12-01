import re
import numpy as np
from itertools import groupby

data_file = open('./2020/data/data06')
data = list(map(lambda group: group.split('\n'), data_file.read().split('\n\n')))
data_file.close()

def group_yes_count(answers_rows):
    all_yes = list("".join(answers_rows))
    count = len(set(all_yes))
    return count

def group_all_yes_count(answers_rows):
    all_yes = list("".join(answers_rows))
    count = sum(map(lambda answer: all_yes.count(answer) == len(answers_rows),  set(all_yes)))
    return count

# 1
group_yes_counts = list(map(group_yes_count, data))
print(sum(group_yes_counts))

# 2
group_all_yes_counts = list(map(group_all_yes_count, data))
print(sum(group_all_yes_counts))