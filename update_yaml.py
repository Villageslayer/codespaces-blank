import glob
import yaml

# Get a list of all data.yaml files in all subdirectories of dataset
yaml_files = glob.glob('Datasets/**/data.yaml', recursive=True)

for file in yaml_files:
    # Load the YAML file
    with open(file, 'r') as f:
        data = yaml.safe_load(f)

    # Modify the values
    data['train'] = f"../train/images"
    data['val'] = f"../valid/images"

    # Write the changes back to the file
    with open(file, 'w') as f:
        yaml.safe_dump(data, f)