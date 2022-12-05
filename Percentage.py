def extra_source2():
    import csv
    import re
    import pandas as pd

    with open("2021 Demographics Overview.csv") as fin:
        reader = csv.reader(fin)
        data_list = list(reader)

    with open("Certified_Personnel 2021.csv") as fin1:
        reader = csv.reader(fin1)
        data_list1 = list(reader)

    base_dict = {}
    for school in data_list1[1:]:
        if school[4] in base_dict:
            if "bachelor" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["BS"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "master" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["MS"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "specialist" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["S"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "doctor" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["phd"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
        else:
            base_dict[school[4]] = {}
            base_dict[school[4]]["School Name"] = school[4]
            base_dict[school[4]]["County"] = school[2]
            base_dict[school[4]]["BS"] = 0
            base_dict[school[4]]["MS"] = 0
            base_dict[school[4]]["S"] = 0
            base_dict[school[4]]["phd"] = 0
            base_dict[school[4]]["Total"] = 0
            if "bachelor" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["BS"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "master" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["MS"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "specialist" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["S"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])
            if "doctor" in school[6].lower() and "teachers" in school[7].lower():
                base_dict[school[4]]["phd"] += int(school[8])
                base_dict[school[4]]["Total"] += int(school[8])

    for i in base_dict:
        if base_dict[i]["Total"] != 0:
            base_dict[i]["Post Grad Percentage"] = float(base_dict[i]["MS"]
                                                     + base_dict[i]["S"]
                                                     + base_dict[i]["phd"]) / float(base_dict[i]["Total"])


    for school in data_list:
        if school[4] in base_dict:
            base_dict[school[4]]["Total Students Enrolled"] = int(float(school[7]))
            base_dict[school[4]]["Teacher-Student Ratio"] = float(base_dict[school[4]]["Total Students Enrolled"] / base_dict[school[4]]["Total"])
            base_dict[school[4]]["White Percentage"] = float(re.findall("(.*)%", school[16])[0])
            base_dict[school[4]]["Black Percentage"] = float(re.findall("(.*)%", school[13])[0])
            base_dict[school[4]]["Econ Disadvantaged Percentage"] = float(re.findall("(.*)%", school[17])[0])

    df_percentages = pd.DataFrame.from_dict(base_dict).T
    df_percentages = df_percentages.dropna()
    percent_dict = df_percentages.T.to_dict()
    
    # Write to a New CSV File      
    csv_columns = ["School Name", "County", "BS", "MS", "S", "phd", "Total", "Post Grad Percentage", "Total Students Enrolled", 
                  "Teacher-Student Ratio", "White Percentage", "Black Percentage", "Econ Disadvantaged Percentage"]
    with open("2316 - Percentages & Certificates.csv", "w") as f:
        w = csv.DictWriter(f, csv_columns)
        w.writeheader()
        for k in percent_dict:
            w.writerow({column: percent_dict[k].get(column) for column in csv_columns})
    return df_percentages

############ Function Call ############
extra_source2()