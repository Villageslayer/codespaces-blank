#!/bin/bash
export KAGGLE_USERNAME=villageslayer
export KAGGLE_KEY=6df063fec518248205dc372585e12fc8 
# Change to the dataset directory
python update_json.py
python update_yaml.py
cd Datasets

# For each subdirectory
for d in */ ; do
    # Change to the subdirectory
    cd "$d"

    # Run different command for the first folder
    if [ "$d" == "rrrr-1/" ]; then
        echo "Running different command in $d"
        kaggle datasets create -p ./ -r zip
        # Add your different command here for the first folder
    else
        # Run the same command for other folders
        echo "Running command in $d"
        kaggle datasets version -p ./ -m $d -r zip
        # Add your command here for other folders
    fi

    # Change back to the parent directory
    cd ..
done