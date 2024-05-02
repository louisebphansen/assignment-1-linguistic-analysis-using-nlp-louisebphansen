'''
This script loops over files in subfolders of a given directory and extracts linguistic information from them
'''
# import required modules
import os 
import spacy
import pandas as pd
import re
from tqdm import tqdm
import argparse
from codecarbon import EmissionsTracker
from codecarbon import track_emissions

# import function from utils script
from my_spacy_utils import extract_ling_info

# define emissionstracker to track CO2 emissions (for assignment 5)
tracker = EmissionsTracker(project_name="assignment1_subtasks",
                    experiment_id="linguistic_analysis",
                    output_dir='emissions',
                    output_file="assignment1_subtasks_emissions.csv")

# define argument parser
def argument_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, help= 'name of the linguistic dataset to use. must be a subfolder of /in', default='USEcorpus')

    args = vars(parser.parse_args())
    
    return args

def extract_from_folder(in_path: str, folder_name: str):
    ''' 
    Loops over files in folder, extracts linguistic information and saves these to a csv file in the 'out' folder.

    Arguments:
        - in_path: path to directory with folder to loop over
        - folder_name: name of folder to iterate over
    
    Returns:
        - None
    ''' 
    # create empty lists to append information to and create df from
    filenames = []

    RelFreq_NOUN = []
    RelFreq_VERB = []
    RelFreq_ADJ = []
    RelFreq_ADV = []

    Unique_PER = []
    Unique_LOC = []
    Unique_ORG = []

    # define path to folder to iterate over
    folder_path = os.path.join(in_path, folder_name)

    # get properly sorted files in that folder
    dirs = os.listdir(folder_path)
    sorted_dirs = sorted(dirs)

    # loop over each file in that folder
    for file in tqdm(sorted_dirs, desc='Extracting linguistic information'):
        try:
            # extract linguistic information from that file
            rel_freqs, ner = extract_ling_info(folder_path, file)

            # append information to lists
            filenames.append(file)
            RelFreq_NOUN.append(rel_freqs['NOUN'])
            RelFreq_VERB.append(rel_freqs['VERB'])
            RelFreq_ADJ.append(rel_freqs['ADJ'])
            RelFreq_ADV.append(rel_freqs['ADV'])
            Unique_PER.append(ner['PERSON'])
            Unique_LOC.append(ner['LOC'])
            Unique_ORG.append(ner['ORG'])
        
        except Exception as e:
            print(f'An error occured to file {file}:', e)

    # create dicts from lists
    data = {'Filename': filenames,
    'RelFreq_NOUN' : RelFreq_NOUN,
    'RelFreq_VERB': RelFreq_VERB,
    'RelFreq_ADJ': RelFreq_ADJ,
    'RelFreq_ADV': RelFreq_ADV,
    'Unique_PER': Unique_PER,
    'Unique_LOC': Unique_LOC, 
    'Unique_ORG': Unique_ORG}

    # convert dict to dataframe
    df = pd.DataFrame(data)

    # save df as a csv in 'out' folder
    df.to_csv(os.path.join('out', f'{folder_name}.csv'), index=False)

# create new tracker using a decorator to track emissions for running the entire script
@track_emissions(project_name="assignment1_FULL",
                experiment_id="assignment1_FULL",
                output_dir='emissions',
                output_file="assignment1_FULL_emissions.csv")
def main():
    
    # parse arguments
    args = argument_parser()

    # define path to folder with subdirectories
    data_path = os.path.join('in', args['dataset'])

    # track downloading of spacy model
    tracker.start_task('Download spacy model')

    # download spacy model
    spacy.cli.download('en_core_web_md')

    # stop tracking
    downloading_emissions = tracker.stop_task()

    # track linguistic analysis task
    tracker.start_task('Extract linguistic information')

    # loop over each directory in the folder and save csv file with linguistic information
    for dir in sorted(os.listdir(data_path)):
        extract_from_folder(data_path, dir)
    
    # stop tracking of analysis
    analysis_emissions = tracker.stop_task()

    # stop overall tracking 
    tracker.stop()

if __name__ == '__main__':
   main()