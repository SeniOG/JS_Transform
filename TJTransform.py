# read csv file
# clean the data:
    # salary, empty space
# transform the data
# save to json/csv
import os
from TJClean import parse_csv
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# from pyspark.sql import Row


# Create a SparkSession
# spark = SparkSession.builder \
#     .appName("Import Data from Multiple CSVs") \
#     .getOrCreate()

# Path to the directory containing CSV files
directory_path = "/Users/senio/Documents/Code_Projects/jobsearch/data" #<< update for cloud computing



# Iterate through CSV files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        
        parsed_data = parse_csv(file_path)
        for entry in parsed_data:
            for key, value in entry.items():
                print(f"{key}: {value}")
            print() 


        
        



# Stop the SparkSession
# spark.stop()

### Bugs: 1. Blank CSVs cause script to crash
