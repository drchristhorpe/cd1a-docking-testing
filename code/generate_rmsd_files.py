import os
import json
import numpy as np

run_name = 'smina-exhaustive-200'

pdb_codes = ['1onq','1xz0','4x6c','4x6d_1','4x6d_2','4x6e','5j1a','6nux','7koz','7kp0','7kp1','7ryn','7ryo','7sh4']

filepath = f'experiments/{run_name}'

append_string = ''

for pdb_code in pdb_codes:
    this_filepath = f'{filepath}/{pdb_code}'
    output_filepath = f'{this_filepath}/{pdb_code}_rmsds.txt'
    obrms_command = f'obrms --firstonly pdb_files/split/{pdb_code}_ligand.pdb {this_filepath}/{pdb_code}{append_string}.sdf > {output_filepath}'
    print (obrms_command)
    os.system(obrms_command)

    with open(output_filepath, 'r') as rmsds_txt_file:
        raw_rmsds = rmsds_txt_file.read()

    i = 1
    rmsds_dict = {'stats':{}, 'rmsds':{}}
    rmsds = []
    for line in raw_rmsds.splitlines():
        rmsd = float(line.split(': ')[1])
        rmsds_dict['rmsds'][str(i)] = rmsd
        rmsds.append(rmsd)
        i += 1
    print (rmsds)
    rmsds_dict['stats']['std_sample'] = np.std(rmsds, ddof=1)
    rmsds_dict['stats']['std_population'] = np.std(rmsds)
    rmsds_dict['stats']['mean'] = np.mean(rmsds)

    json_output_filepath = f'{this_filepath}/{pdb_code}_rmsds.json'
    with open(json_output_filepath, 'w') as rmsds_json_file:
        json.dump(rmsds_dict, rmsds_json_file)