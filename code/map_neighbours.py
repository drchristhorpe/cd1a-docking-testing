import json

with open('outputs/neighbours.json') as neighbour_file:
    neighbours = json.load(neighbour_file)

mapped_neighbours = {}

positions = []

for position in neighbours['positions']:
    positions.append(int(position))

positions = [str(position) for position in sorted(positions)]



header = ['structure']
for position in positions:
    header.append(position)

print (header)

mapped_neighbours['header'] = header

data = []

for structure in neighbours['raw']:
    row = []
    row.append(structure)
    for position in positions:
        if position in neighbours['raw'][structure]:
            row.append(1)
        else:
            row.append(0)
    data.append(row)

mapped_neighbours['data'] = data
print (data)

with open('outputs/mapped_neighbours.json', 'w') as mapped_file:
    json.dump(mapped_neighbours, mapped_file)

