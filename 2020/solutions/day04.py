import re

with open('./2020/data/data04') as data_file:
    data = list(data_file.read().split('\n\n'))

required = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
validation = [
    'byr:(19[2-9][0-9]|200[0-2])(\n| )',
    'iyr:(201[0-9]|2020)(\n| )',
    'eyr:(202[0-9]|2030)(\n| )',
    'hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))(\n| )',
    'hcl:#[a-fA-F0-9]{6}(\n| )',
    'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\n| )',
    'pid:[0-9]{9}(\n| )'
]
r_pattern = re.compile('|'.join(required))
v_pattern = re.compile('|'.join(validation))

def check_required(passport):
    return len(r_pattern.findall(passport)) == len(required)

def validate(passport):
    return len(v_pattern.findall(passport+' ')) == len(validation)

print(sum(map(check_required, data)))
print(sum(map(validate, data)))
