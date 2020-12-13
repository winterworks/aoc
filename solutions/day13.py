import math

data_file = open('./data/data13')
data = data_file.read().split('\n')
data_file.close()

busses = list(map(lambda bus: int(bus), map(lambda bus: bus if bus != 'x' else 0, data[1].split(','))))
busses_active = list(map(lambda bus: int(bus), filter(lambda bus: bus != 'x', data[1].split(','))))

bus_mod = list(map(lambda bus: bus - int(data[0]) % bus, busses_active))
next_bus_index = bus_mod.index(min(bus_mod))
next_bus = busses_active[next_bus_index]

print(next_bus*min(bus_mod))

def get_lcm(list):
    lcm = list[0]
    for i in list[1:]:
        lcm = int(lcm*i/math.gcd(lcm, i))
    return lcm

def get_bus_leave_pattern_time(busses, cap, busses_found = []):
    time = busses[0]
    while len(busses_found) < cap:
        for bus_index, bus in enumerate(busses):
            if bus == 0:
                continue
            if (time + bus_index) % bus == 0:
                if bus not in busses_found:
                    busses_found.append(bus)
            else:
                time += get_lcm(busses_found)
    return time

print(get_bus_leave_pattern_time(busses, len(busses_active)))