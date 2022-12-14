import json

run_name = 'gnina-exhaustive-100'

pdb_codes = ['1onq','1xz0','4x6c','4x6d_1','4x6d_2','4x6e','5j1a','6nux','7koz','7kp0','7kp1','7ryn','7ryo','7sh4']

filepath = f'experiments/{run_name}'

split_token = '$$$$'


def generate_statistics(frame):
  statistics = {}
  raw_statistics = frame.split('END')[1]
  for line in raw_statistics.splitlines():
    if '>' in line:
      key = line.replace('>','').replace('<','')
    elif len(line) > 0 and '$' not in line:
      value = line
      if key is not None:
        statistics[key] = value
      key = None

  return statistics


for pdb_code in pdb_codes:

    this_filepath = f'{filepath}/{pdb_code}'
    filename = f'{this_filepath}/{pdb_code}.sdf'

    with open(filename) as file:
        sdf_file = file.read()

    frames = sdf_file.split(f'{split_token}\n')
    
    frame_data = {}
    i = 1

    for frame in frames:
        if len(frame.strip()) > 0:
            this_frame = frame + split_token
            frame_data[str(i)] = {}
            frame_data[str(i)]['full'] = this_frame
            frame_data[str(i)]['info'] = generate_statistics(this_frame)
            i += 1

    json_output_filepath = f'{this_filepath}/{pdb_code}_scores.json'
    with open(json_output_filepath, 'w') as scores_json_file:
        json.dump(frame_data, scores_json_file)
    print (frame_data['1']['info'])