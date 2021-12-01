import re
import numpy as np

data_file = open('./2020/data/data16')
data = data_file.read().split('\n\n')
data_file.close()

# Parse all the data
rules = list(map(lambda row: re.split(': | or |-', row)[1:], data[0].split('\n')))
rule_labels = list(map(lambda row: row.split(': ')[0], data[0].split('\n')))
my_ticket = data[1].split('\n')[1].split(',')
tickets = list(map(lambda row: row.split(','), data[2].split('\n')[1:]))

# Convert rules and tickets to ints
rules = [list(map(int,r)) for r in rules]
my_ticket = [int(t) for t in my_ticket]
tickets = [list(map(int,t)) for t in tickets]

def validate_value(rules, value):
    valid_for_rules = []
    for i, rule in enumerate(rules):
        if rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]:
            valid_for_rules.append(i)
    return valid_for_rules

def tickets_errors(rules, tickets):
    invalid_values = []
    for ticket in tickets:
        for value in ticket:
            if len(validate_value(rules,value)) == 0:
                invalid_values.append(value)
    return invalid_values

def delete_invalid_tickets(rules, tickets):
    filtered_tickets = []
    for index, ticket in enumerate(tickets):
        valid = True
        for value in ticket:
            if len(validate_value(rules,value)) == 0:
                valid = False
        if valid:
            filtered_tickets.append(ticket)
    return filtered_tickets

def get_ticket_value_options(rules, tickets):
    fit = [[0 for i in range(len(tickets))] for i in range(len(rules))]
    for column in range(0,len(tickets[0])):
        for row, field in enumerate(np.array(tickets)[:,column]):
            fit[column][row] = validate_value(rules,field)
    return fit

def get_colum_options(column_fit):
    columns_options = []
    for index, column in enumerate(column_fit):
        options = list(set.intersection(*(list(map(lambda c: set(c), column)))))
        columns_options.append([index, options])
    return columns_options

def get_colum_rule_mapping(columns_options):
    column_rule_mapping = []
    for index, column_rule in enumerate(columns_options):
        if index < len(columns_options)-1:
            col = list(filter(lambda x : x not in columns_options[index+1][1], column_rule[1]))
            column_rule_mapping.append([column_rule[0], col])
        else:
            column_rule_mapping.append(column_rule)
    return column_rule_mapping

def get_rules_indexes(start_with):
    found_rules = list(filter(lambda r: r.startswith(start_with), rule_labels))
    return list(map(lambda r: rule_labels.index(r), found_rules))

def get_my_ticket_values(column_rule_mapping, rule_indexes):
    columns = []
    for rule_index in rule_indexes:
        for column_rule_map in column_rule_mapping:
            if rule_index in column_rule_map[1]:
                columns.append(my_ticket[column_rule_map[0]])
    return columns

# 1
print(sum(tickets_errors(rules, tickets)))

# 2
# Delete the invalid tickets and get the rule options for each value on each ticket
tickets = delete_invalid_tickets(rules, tickets)
ticket_value_options = get_ticket_value_options(rules, tickets)

# Check which column option is the only possibility for each column
columns_options = get_colum_options(ticket_value_options)
columns_options.sort(key=lambda r: len(r[1]), reverse=True)
column_rule_mapping = get_colum_rule_mapping(columns_options)

# Get the reqruired rules and use the mapping the get them from my ticket
rule_indexes = get_rules_indexes('departure')
required_columns = get_my_ticket_values(column_rule_mapping, rule_indexes)

print(np.prod(required_columns, dtype='i8'))