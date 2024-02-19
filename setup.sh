# create virtual environment
python3 -m venv env

source env/bin/activate

# install packages from requirements file
pip install -r requirements.txt

# download spacy model
python3 -m spacy download en_core_web_md

deactivate 