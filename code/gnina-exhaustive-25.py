import os
from pathlib import Path

pdb_codes = ['1onq','1xz0','4x6c','4x6d_1','4x6d_2','4x6e','5j1a','6nux','7koz','7kp0','7kp1','7ryn','7ryo','7sh4']



for pdb_code in pdb_codes:
    folder_name = f'experiments/gnina-exhaustive-25/{pdb_code}'
    if os.path.exists(folder_name):
        print (f'{pdb_code} already docked')
    else:
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        cd1a_filename = f'pdb_files/split/{pdb_code}_cd1a.pdb'
        ligand_filename = f'pdb_files/split/{pdb_code}_ligand.pdb'
        docked_filename = f'{folder_name}/{pdb_code}.sdf'
        log_filename = f'{folder_name}/{pdb_code}.txt'
        

        gnina_command = f'tools/gnina -r {cd1a_filename} -l {ligand_filename} --autobox_ligand {ligand_filename} -o {docked_filename} --log {log_filename} --exhaustiveness 25 --seed 0'
        
        os.system(gnina_command)