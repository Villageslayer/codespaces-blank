import glob
import json

json_files = glob.glob('Datasets/**/dataset-metadata.json', recursive=True)

for file in json_files:
    # Load the JSON file
    with open(file, 'r') as f:
        metadata = json.load(f)

    # Modify the keys
    metadata['title'] = 'WORRRRKYV3'
    metadata['id'] = "villageslayer/WORRRRKYV3"

    # Write the changes back to the file
    with open(file, 'w') as f:
        json.dump(metadata, f, indent=4)