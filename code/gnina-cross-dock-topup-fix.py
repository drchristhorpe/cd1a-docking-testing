import os
from pathlib import Path

pdb_codes = ['1onq']


cluster_pdbs = ['7ryn']


for pdb_code in pdb_codes:
    folder_name = f'experiments/gnina-crossdock/{pdb_code}'
    print (pdb_code)
    exhaustiveness = 100
    i = 0
    for cluster_pdb in cluster_pdbs:
        i += 1
        if cluster_pdb != pdb_code:
            cd1a_filename = f'pdb_files/split/{cluster_pdb}_cd1a.pdb'
            ligand_filename = f'pdb_files/split/{pdb_code}_ligand.pdb'
            docked_filename = f'{folder_name}/{pdb_code}_cluster{i}.sdf'
            log_filename = f'{folder_name}/{pdb_code}_cluster{i}.txt'
            gnina_command = f'tools/gnina -r {cd1a_filename} -l {ligand_filename} --autobox_ligand {ligand_filename} -o {docked_filename} --log {log_filename} --exhaustiveness {exhaustiveness} --seed 0'
            
            os.system(gnina_command)

                
        
        
        

