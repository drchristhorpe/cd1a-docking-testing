import os
from pathlib import Path

pdb_codes = ['1onq','1xz0','4x6c','4x6d_1','4x6d_2','4x6e','5j1a','6nux','7koz','7kp0','7kp1','7ryn','7ryo','7sh4']


cluster_pdbs = ['7ryn', '7koz','4x6c','7ryo','5j1a']

exhaustiveness = 25

for pdb_code in pdb_codes:
    print (pdb_code)
    folder_name = f'experiments/gnina-crossdock-{exhaustiveness}/{pdb_code}'
    if os.path.exists(folder_name):
        print (f'{pdb_code} already docked')
    else:  
        print (folder_name)
        Path(folder_name).mkdir(parents=True, exist_ok=True)

        
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

                
        
        
        

