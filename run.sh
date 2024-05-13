# activate virtual environment
source env/bin/activate

# unzip data file (create /in folder with data)
unzip data.zip

# run script
python3 src/extract_ling_info.py

# deactivate venv
deactivate