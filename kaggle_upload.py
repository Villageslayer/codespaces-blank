import os
import json

def load_kaggle_credentials():
    # Set the path to the kaggle.json file
    kaggle_json_path = '.kaggle/kaggle.json'

    # Check if the file exists
    if os.path.exists(kaggle_json_path):
        # Load the contents of the kaggle.json file
        with open(kaggle_json_path) as f:
            kaggle_json_data = json.load(f)

        # Set the KAGGLE_USERNAME and KAGGLE_KEY environment variables if they're not already set
        kaggle_username = kaggle_json_data.get('username', '')
        kaggle_key = kaggle_json_data.get('key', '')
        
        if 'KAGGLE_USERNAME' in os.environ and 'KAGGLE_KEY' in os.environ:
            print('Environment variables already set.')
        else:
            os.environ['KAGGLE_USERNAME'] = kaggle_username
            os.environ['KAGGLE_KEY'] = kaggle_key
            print('Environment variables set.')

        # Set the KAGGLE_CONFIG_DIR environment variable to the directory containing the kaggle.json file if it's not already set
        os.environ.setdefault('KAGGLE_CONFIG_DIR', os.path.dirname(kaggle_json_path))
        
        # Store the variables in a JSON file
        credentials = {
            'KAGGLE_USERNAME': kaggle_username,
            'KAGGLE_KEY': kaggle_key
        }
        with open('credentials.json', 'w') as f:
            json.dump(credentials, f)
            print('Credentials stored in credentials.json.')
    else:
        print('kaggle.json file not found.')

# Call the function to load the Kaggle credentials
load_kaggle_credentials()
