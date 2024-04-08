import os, csv, re
from skills_list import skills_list

# open CSV file
# iterate through lines and parse through through text
# correctly enter cleaned up text into dictionary
# append dictionary to list
# use job desc to create skills list for job
# add skills list to dictionary
# save dictionary to csv

directory = directory_path = "/Users/senio/Documents/Code_Projects/jobsearch/testdata" #<< update for cloud computing


job_list2 = []

output_file = "output.csv"

def extract_figures(text):
    #check for 'per day' text
    # check for 'hour'
    # else:
        # return int or ints 
    if 'per day' in text or 'daily' in text:
        return 'daily rate'
    elif 'hour' in text or 'hourly' in text:
        return 'hourly rate'
    else:
        try:
            # Regular expression pattern to match figures
            pattern = r'£\d+(?:,\d+)?(?:\.\d+)?'
            figures = re.findall(pattern, text)
            return [float(figure.replace('£', '').replace(',', '')) for figure in figures]
        except:
            return [None]

    

def contains_per_day(text):
    return 'per day' in text.lower()

def clean_text(text):
    cleaned_text = text.strip('"').replace('\n', ' ')
    cleaned_text = cleaned_text.replace('TITLE:', '')
    cleaned_text = cleaned_text.replace('SALARY:', '')
    cleaned_text = cleaned_text.replace('RECRUITER:', '')
    cleaned_text = cleaned_text.replace('DATE:', '')
    cleaned_text = cleaned_text.replace('LINK:', '')
    cleaned_text = cleaned_text.replace('JOB DESC:', '')
    cleaned_text = cleaned_text.replace('sSCRAPE', '')
    cleaned_text = cleaned_text.strip()

    return cleaned_text


def parse_csv(file_path):
   job_list = []
   
   with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        next(csvreader)  # Skip the header row

        for row_number, row in enumerate(csvreader, start=1):
            if len(row) < 7:
                print(f"Warning: Row {row_number} has fewer columns than expected.")
                continue

        # for row in csvreader:
            cleaned_row = [clean_text(item) for item in row]
            data_dict = {
                'TITLE': cleaned_row[0],
                'SALARY': extract_figures(cleaned_row[1]),
                'RECRUITER': cleaned_row[2],
                'POSTDATE': cleaned_row[3],
                'HREF': cleaned_row[4],
                'JOB_DESC': cleaned_row[5],
                'SCRAPE_DATE': cleaned_row[6],
                'SKILLS': skill_search(cleaned_row[5])
            }
            job_list.append(data_dict)
            
        return job_list
   
def skill_search(large_string):

       words = large_string.split()
       words = re.findall(r'\b\w+\b', large_string.lower())

    
       matching_words = set()

       for word in words:
           if word in skills_list:
               matching_words.add(word)
        
       return(matching_words)

# Print result to terminal
# parsed_data = parse_csv(file)
# for entry in parsed_data:
#     for key, value in entry.items():
#         print(f"{key}: {value}")
#     print() 

def save_to_csv(parsed_data):
    file_exists = os.path.exists(output_file) # checking for the file

    # Open the CSV file in append mode if it exists, otherwise open in write mode
    with open(output_file, 'a' if file_exists else 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)
        # write header row only if the file is new
        if not file_exists:
            header = parsed_data[0].keys()
            csv_writer.writerow(header)
        
        for entry in parsed_data:
            csv_writer.writerow(entry.values())

    print("Data has been saved to", output_file)

def process_files_in_directory(directory):
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            file_path = os.path.join(directory, file)
            parsed_data = parse_csv(file_path)
            save_to_csv(parsed_data)

process_files_in_directory(directory)





# bugs: 1. unable to search for 'C#' or 'C++'; currently only able to find 'C'
