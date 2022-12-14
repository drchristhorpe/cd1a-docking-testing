import os
from pathlib import Path

ligand_pdb_codes = ['3xu','6fb','42h','cis','fo4','fof','jho','mw9','ola','pam','slf','wgr','wu7','wua']


cluster_pdbs = ['7ryn', '7koz','4x6c','7ryo','5j1a']


for pdb_code in ligand_pdb_codes:
    print (pdb_code)
    folder_name = f'experiments/snina-crossdock-16/{pdb_code}'
    if os.path.exists(folder_name):
        print (f'{pdb_code} already docked')
    else:  
        print (folder_name)
        Path(folder_name).mkdir(parents=True, exist_ok=True)

        exhaustiveness = 16
        i = 0
        for cluster_pdb in cluster_pdbs:
            i += 1
            if cluster_pdb != pdb_code:
                cd1a_filename = f'pdb_files/split/{cluster_pdb}_cd1a.pdb'
                ligand_filename = f'pdb_files/ligands/pdb/{pdb_code}.pdb'
                autobox_filename = f'pdb_files/split/{cluster_pdb}_ligand.pdb'
                docked_filename = f'{folder_name}/{pdb_code}_cluster{i}.sdf'
                log_filename = f'{folder_name}/{pdb_code}_cluster{i}.txt'
                gnina_command = f'tools/smina.osx.12 -r {cd1a_filename} -l {ligand_filename} --autobox_ligand {autobox_filename} -o {docked_filename} --log {log_filename} --exhaustiveness {exhaustiveness} --seed 0'
                
                os.system(gnina_command)

                
        
        
        

