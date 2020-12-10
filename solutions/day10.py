import collections

data_file = open('./data/data10')
adapters = sorted(map(int, data_file.read().split('\n')))
data_file.close()

# Add the outlet and device
adapters.insert(0, 0)
adapters.append(adapters[-1]+3)

def get_links_out(adapters, step_range):
    links = {}
    for adapter in adapters:
        links[adapter] = list(filter(lambda a: a - adapter in step_range, adapters))
    return links

def get_links_in(links_out):
    links_in_cumulative = {0: 1}
    for adapter in links_out:
        for link in links_out[adapter]:
            if link not in links_in_cumulative:
                links_in_cumulative[link] = 0
            links_in_cumulative[link] += links_in_cumulative[adapter]
    return links_in_cumulative

steps = collections.Counter(list(map(lambda x: x[0]-x[1], zip(adapters[1:], adapters[:-1]))))
print(steps[1]*steps[3])

links_in = get_links_in(get_links_out(adapters, range(1,4)))
print(links_in.popitem()[1])
