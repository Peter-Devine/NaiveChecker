import argparse
import os
import pandas as pd

# Takes input directory as argument
parser=argparse.ArgumentParser()
parser.add_argument('--input', default=".", help='The file path of the train.tsv, dev.tsv and test.tsv')
parser.add_argument('--columns', default="emotion", help='The file path of the train.tsv, dev.tsv and test.tsv')
parser.add_argument('--raw_freq', default="False", help='The file path of the train.tsv, dev.tsv and test.tsv')

args = parser.parse_args()
INPUT_PATH = args.input
SELECTED_COLUMNS_STRING = args.columns
SHOW_RAW_FREQUENCY = args.raw_freq.upper() == "TRUE"

selected_column_list = SELECTED_COLUMNS_STRING.split(",")

def whitespace_stripper(string):
    return(string.strip())

selected_column_list = list(map(whitespace_stripper, selected_column_list))

train = pd.read_csv(INPUT_PATH + "/train.tsv", sep="\t")
dev = pd.read_csv(INPUT_PATH + "/dev.tsv", sep="\t")
test = pd.read_csv(INPUT_PATH + "/test.tsv", sep="\t")

for selected_column in selected_column_list:
    if SHOW_RAW_FREQUENCY:
        denominator_train = [1]*len(train[selected_column].value_counts())
        denominator_dev = [1]*len(dev[selected_column].value_counts())
        denominator_test = [1]*len(test[selected_column].value_counts())
    else:
        denominator_train = train.shape[0]
        denominator_dev = dev.shape[0]
        denominator_test = test.shape[0]
    
    print("\n Train")
    print(train[selected_column].value_counts() / denominator_train)
    print("\n Dev")
    print(dev[selected_column].value_counts() / denominator_dev)
    print("\n Test")
    print(test[selected_column].value_counts() / denominator_test)

