import csv,re

with open ('Crimes.csv','r') as crime_file:
    crimes=csv.reader(crime_file)
    counter=0
    pattern=re.compile(r'[-/](20)*15 ')
    crime_dict={}
    for i in crimes:

        if re.search(pattern,i[2]):
            if i[5] not in crime_dict:
                crime_dict[i[5]] = 0
            else:
                crime_dict[i[5]] += 1

MOST_POPUALR_CRIME_EVER = max(crime_dict.values())
print(list(crime_dict.keys())[list(crime_dict.values()).index(MOST_POPUALR_CRIME_EVER)])