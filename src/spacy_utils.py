''' 
LANGUAGE ANALYTICS @ AARHUS UNIVERSITY, ASSIGNMENT 1: Linguistic Analysis using NLP

AUTHOR: Louise Brix Pilegaard Hansen

DESCRIPTION:
This script contains util functions for extracting relevant linguistic information from a text corpus
'''
# import required modules
import os 
import spacy
import pandas as pd
import re

def read_and_preprocess(path_to_txt_file: str) -> str:
    ''' 
    Opens a txt file from given path and removes pointed brackets and line breaks.

    Arguments:
        - path_to_txt_file: path to txt file to open
    
    Returns:
        - preprocessed txt file as string
    ''' 

    # read txt file and set encoding
    with open(path_to_txt_file, "r", encoding="unicode_escape") as f:
        text = f.read()
    
    # preprocess (remove pointed brackets and everything between)
    cleaned_text = re.sub("<.*?>", '', text)

    # remove line breaks (looks like it is present in some of the files)
    preprocessed_text = cleaned_text.replace("\n", " ")

    return preprocessed_text

def count_relfreq_pos(doc: spacy.tokens.doc.Doc, tag: str) -> float:
    ''' 
    Counts the relative frequency (out of 10,000 words) of a given part-of-speech (POS) tag

    Arguments:
        - doc: spacy-tokenized text file/string
        - tag: POS-tag to count frequency of (e.g., 'NOUN')
    
    Returns:
        - relative frequency as float
    '''
    # extract POS tag for each token in doc
    pos_doc = [token.pos_ for token in doc]
    
    # count the absolute frequency of the desired POS tag
    count = pos_doc.count(tag)

    # calculate relative frequency by 10,000 words and round to two decimals
    rel_count = round((count/len(doc))*10000, 2) 

    return rel_count

def count_ner(doc: spacy.tokens.doc.Doc, entity_label: str) -> int:
    ''' 
    Counts the unique amount of a given entity returned by a Named Entity Recognition (NER) search.

    Arguments:
        - doc: spacy-tokenized text file/string
        - entity_label: entity label to count unique occurences of (e.g., "ORG")
    
    Returns:
        - number of unique entities of the given label
    '''
    # initialize empty list
    labels = []

    # loop over all entities in the doc and search for the desired entity label
    for ent in doc.ents:
        if ent.label_ == entity_label:
            labels.append(ent.text)
        else:
            continue
    
    # count number of unique labels
    unique_labels = len(set(labels))
    
    return unique_labels

def extract_ling_info(folder_path: str, filename: str) -> dict:
    ''' 
    Opens a txt file from path and extracts POS and NER linguistic information.

    Arguments:
        - folder_path: path to folder the given file is in
        - filename: name of txt file to extract information from
    
    Returns:
        - two dicts containing POS and NER linguistic information, respectively
    '''
    # define path to the txt file
    path_to_txt_file = os.path.join(folder_path, filename)

    # read and preprocess txt file
    cleaned_text = read_and_preprocess(path_to_txt_file)

    # load spacy model
    nlp = spacy.load("en_core_web_md")
    
    # tokenize
    doc = nlp(cleaned_text)
    
    # create list of desired POS-tags we want to count frequency of
    pos_name = ['NOUN', 'VERB', 'ADJ', 'ADV']

    # count the relative frequency of each of the tags and save as dict
    rel_freqs = [count_relfreq_pos(doc, tag) for tag in pos_name]
    rel_freqs_dict = dict(zip(pos_name, rel_freqs))

    # create list of NER-labels we want to count unique occurences of
    ner_labels = ['PERSON', 'LOC', 'ORG']

    # count unique occurences of each of the labels and save as dict
    ner = [count_ner(doc, label) for label in ner_labels]
    ner_dict = dict(zip(ner_labels, ner))

    return rel_freqs_dict, ner_dict