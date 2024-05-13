'''
Script to visualize the results from the Assignment 1 analysis.

'''
# import modules
import os 
import pandas as pd 
import matplotlib.pyplot as plt
import glob 

def collect_dfs(dir_path):
    '''
    Function to gather all csv files into one pandas dataframe
    '''

    # find all csv files in directory
    extension = 'csv'
    os.chdir(dir_path)
    result = glob.glob('*.{}'.format(extension))

    full_df = pd.DataFrame()

    # read csv files as dataframes and concatenate to one big
    for file in sorted(result):
        #folder_path = os.path.join(dir_path, file)
        df = pd.read_csv(file)
        df['essay'] = file[:2] # remove .csv 
        full_df = pd.concat([full_df, df])
    
    return full_df 

def calc_means(full_df, essays):

    '''
    Calculate the mean relative frequency of POS and NER tags for each essay
    '''

    noun_means = []
    verb_means = []
    adj_means = []
    adv_means = []
    PER_means = []
    LOC_means = []
    ORG_means = []

    # get mean frequencies for each essay
    for essay in essays:
        df_period = full_df.query(f"essay == '{essay}'")

        noun_mean = df_period['RelFreq_NOUN'].mean()
        noun_means.append(noun_mean)

        verb_mean = df_period['RelFreq_VERB'].mean()
        verb_means.append(verb_mean)

        adj_mean = df_period['RelFreq_ADJ'].mean()
        adj_means.append(adj_mean)

        adv_mean = df_period['RelFreq_ADV'].mean()
        adv_means.append(adv_mean)

        PER_mean = df_period['Unique_PER'].mean()
        PER_means.append(PER_mean)

        LOC_mean = df_period['Unique_LOC'].mean()
        LOC_means.append(LOC_mean)

        ORG_mean = df_period['Unique_ORG'].mean()
        ORG_means.append(ORG_mean)

    pos_means = [noun_means, verb_means, adj_means, adv_means]
    ner_means = [PER_means, LOC_means, ORG_means]

    return pos_means, ner_means 

def plot_pos(pos_means, essays):
    '''
    Plot mean relative frequency of pos tags
    '''

    labels = ['Nouns', 'Verbs', 'Adjectives', 'Adverbs']

    for i, v in enumerate(pos_means):
        plt.plot(essays, v, label=labels[i])

    plt.legend(fontsize=8)
    plt.tick_params(axis='x', labelrotation=80)
    plt.ylabel('Mean relative frequency (per 10,000 words)')
    plt.xlabel('Essay')
    plt.title('Average relative frequencies of POS tags across essays')

    #fig_path = os.path.join('pos_mean_freq.png')
    plt.savefig('pos_mean_freq.png')

def plot_ner(ner_means, essays):
    '''
    Plot mean unique NER tags per essay
    '''

    labels = ['Person', 'Location', 'Organizations']

    plt.figure()
    for i, v in enumerate(ner_means):
        plt.plot(essays, v, label=labels[i])
    
    plt.legend()
    plt.tick_params(axis='x', labelrotation=80)
    plt.ylabel('Mean amount of unique NER labels')
    plt.xlabel('Essay')
    plt.title('Average amount of unique NER labels across essays')

    #fig_path = os.path.join('out', 'ner_mean_freq.png')
    plt.savefig('ner_mean_freq.png')

def main():
    
    # path to csv files
    dir_path = os.path.join('out')

    # collect df of all csv files
    full_df = collect_dfs(dir_path)

    # get list of essays
    essays = list(pd.unique(full_df['essay']))

    # calculate mean relative frequencies of POS and mean unique NER tags for each essay
    pos_means, ner_means = calc_means(full_df, essays)

    # plot results
    plot_pos(pos_means, essays)
    plot_ner(ner_means, essays)

if __name__ == '__main__':
   main()
