import csv
from prompts import*
from Eagle1.predictdemo_new import *
from loguru import logger

folder_path = "CelebA_dataset_remaining"  # Path to the folder containing images
output_csv = "new_features_CelebA_dataset_remaining.csv"
input_prompt=prompt6
facial_list= prompt6_feature_list

if __name__=="__main__":
    eagle_csv_generator(folder_path,output_csv,input_prompt,facial_list)