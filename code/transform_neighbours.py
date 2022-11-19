import json

filepath = '../outputs/neighbours.json'

with open(filepath, 'r') as neighbour_file:
    neighbours = json.load(neighbour_file)


positions = {}

for pdb_code in neighbours['raw']:
    ligand_neighbours = neighbours['raw'][pdb_code]
    for neighbour in ligand_neighbours:
        if neighbour not in positions:
            positions[neighbour] = {'structures':[],'frequency':0}
        positions[neighbour]['structures'].append(pdb_code)
        positions[neighbour]['frequency'] += 1

neighbours['positions'] = positions

with open(filepath, 'w') as neighbour_file:
    json.dump(neighbours, neighbour_file, indent=4)
