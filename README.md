# Assignment 1: Linguistic Analysis using NLP

This assignment is the first assignment for the portfolio exam in the Language Analytics course at Aarhus University, spring 2024.

### Contributions
All code was created by me, but code provided in the notebooks used for teaching the course has been reused. 

### Assignment description

- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the information

### Contents of the repository


| <div style="width:120px"></div>| Description |
|---------|:-----------|
|```in```| Contains the *USEcorpus* dataset used for the assignment |
| ```out``` | Contains csv files produced by running the code in ```src``` |
| ```src```  | Contains the python scripts for extracting linguistic information from the dataset     |
| ```run.sh```    | Bash script for running the code |
| ```setup.sh```  | Bash script for setting up virtual environment and downloading spaCy model |
| ```requirements.txt```  | Packages required to run the code|


### Methods

This project contains the code to extract relevant linguistic information from a corpus of text. More specifically, ```src/my_spacy_utils.py``` contains the code to extract the relative frequencies of several parts-of-speech (POS) tags, namely nouns, verbs, adjectives and adverbs as well as unique occurences of entities of persons, organizations and locations found by named entity recognition (NER). ```src/extract_ling_information.py``` uses this code to loop over an input folder with subdirectories containing the input text files. 

The code mainly uses functions from ```spaCy``` to tokenize, find POS-tags and named entities. I am  using the *'en_core_web_md'* model.


### Usage

All code for this assignment was designed to run on an Ubuntu 22.04 operating system using Python version 3.10.12. It is therefore not guaranteed that it will work on other operating systems.

#### DATA ?? 

#### Set up virtual environment
It is important that you run the code from the main folder, i.e., *assignment-1-linguistic-analysis-using-nlp-louisebphansen*. Your terminal should look like this:

```
--your_path-- % assignment-1-linguistic-analysis-using-nlp-louisebphansen %
```


To run the code in this repo, clone it using ```git clone```.

In order to set up the virtual environment, the *venv* package for Python needs to be installed first:

```
sudo apt-get update

sudo apt-get install python3-venv
```

Next, run:

```
bash setup.sh
```

This will create a virtual environment in the directory (```env```), install the required packages to run the code and download the *'en_core_web_md'* from **spaCy**.


#### Run code

To run the code, you can do the following:

##### Run script(s) with predefined arguments

From the terminal, type 
```
bash run.sh
```

This will activate the virual environment and run the ```src/extract_ling_information.py```script with default arguments to extract linguistic information about POS-tags and NER-labels from each subfolder in the USEcorpus dataset. The output from this is saved in the ```out```folder.
 

##### Define arguments yourself
Alternatively, the script can be run with different arguments:

```
# activate the virtual environment
source env/bin/activate

python3 src/extract_ling_info.py --dataset <dataset> 
```
**Arguments:**

- **Dataset:** Name of dataset placed in the ```in``` folder with subdirectories to iterate over.


### Results








