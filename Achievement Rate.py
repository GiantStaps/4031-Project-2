def data_parser():
    import csv
    import numpy as np 
    import pandas as pd

    '''
    2019 Data
    '''
    
    with open("2019 Content Mastery.csv") as fin:
        reader = csv.reader(fin)
        data_list = list(reader)
        print(data_list)
    
    def checkFloat(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    dict_certificate = {}
    for school in data_list[1:]:
        if school[4] in dict_certificate:
            if "all students" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["All Students English Achievement"] = float(school[10])
            if "all students" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["All Students Math Achievement"] = float(school[10])
            if "american indian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["American Indian/Alaskan English Achievement"] = float(school[10])
            if "american indian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["American Indian/Alaskan Math Achievement"] = float(school[10])
            if "asian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Asian/Pacific Islander English Achievement"] = float(school[10])
            if "asian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Asian/Pacific Islander Math Achievement"] = float(school[10])
            if "black" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Black English Achievement"] = float(school[10])
            if "black" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Black Math Achievement"] = float(school[10])
            if "economically" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Economically Disadvantaged English Achievement"] = float(school[10])
            if "economically" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Economically Disadvantaged Math Achievement"] = float(school[10])
            if "hispanic" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Hispanic English Achievement"] = float(school[10])
            if "hispanic" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Hispanic Math Achievement"] = float(school[10])
            if "white" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["White English Achievement"] = float(school[10])
            if "white" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["White Math Achievement"] = float(school[10])
            if "disability" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Students With Disability English Achievement"] = float(school[10])
            if "disability" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Students With Disability Math Achievement"] = float(school[10])
            pass
        else:
            dict_certificate[school[4]] = {}
            dict_certificate[school[4]]["School Name"] = school[4]
            dict_certificate[school[4]]["County"] = school[2]
            dict_certificate[school[4]]["Classification"] = school[6]
            dict_certificate[school[4]]["All Students English Achievement"] = 0.0
            dict_certificate[school[4]]["All Students Math Achievement"] = 0.0
            dict_certificate[school[4]]["American Indian/Alaskan English Achievement"] = 0.0
            dict_certificate[school[4]]["American Indian/Alaskan Math Achievement"] = 0.0
            dict_certificate[school[4]]["Asian/Pacific Islander English Achievement"] = 0.0
            dict_certificate[school[4]]["Asian/Pacific Islander Math Achievement"] = 0.0
            dict_certificate[school[4]]["Black English Achievement"] = 0.0
            dict_certificate[school[4]]["Black Math Achievement"] = 0.0
            dict_certificate[school[4]]["Economically Disadvantaged English Achievement"] = 0.0
            dict_certificate[school[4]]["Economically Disadvantaged Math Achievement"] = 0.0
            dict_certificate[school[4]]["Hispanic English Achievement"] = 0.0
            dict_certificate[school[4]]["Hispanic Math Achievement"] = 0.0
            dict_certificate[school[4]]["White English Achievement"] = 0.0
            dict_certificate[school[4]]["White Math Achievement"] = 0.0
            dict_certificate[school[4]]["Students With Disability English Achievement"] = 0.0
            dict_certificate[school[4]]["Students With Disability Math Achievement"] = 0.0
            if "all students" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["All Students English Achievement"] = float(school[10])
            if "all students" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["All Students Math Achievement"] = float(school[10])
            if "american indian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["American Indian/Alaskan English Achievement"] = float(school[10])
            if "american indian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["American Indian/Alaskan Math Achievement"] = float(school[10])
            if "asian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Asian/Pacific Islander English Achievement"] = float(school[10])
            if "asian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Asian/Pacific Islander Math Achievement"] = float(school[10])
            if "black" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Black English Achievement"] = float(school[10])
            if "black" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Black Math Achievement"] = float(school[10])
            if "economically" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Economically Disadvantaged English Achievement"] = float(school[10])
            if "economically" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Economically Disadvantaged Math Achievement"] = float(school[10])
            if "hispanic" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Hispanic English Achievement"] = float(school[10])
            if "hispanic" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Hispanic Math Achievement"] = float(school[10])
            if "white" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["White English Achievement"] = float(school[10])
            if "white" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["White Math Achievement"] = float(school[10])
            if "disability" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Students With Disability English Achievement"] = float(school[10])
            if "disability" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[10]):
                dict_certificate[school[4]]["Students With Disability Math Achievement"] = float(school[10])
            pass
    
    '''
    2021 Data
    '''
    
    with open("2021 Content Mastery.csv") as fin1:
        reader = csv.reader(fin1)
        data_list1 = list(reader)

    dict_certificate1 = {}
    for school in data_list1[1:]:
        if school[4] in dict_certificate1:
            if "all students" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["All Students English Achievement"] = float(school[14])
            if "all students" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["All Students Math Achievement"] = float(school[14])
            if "american indian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["American Indian/Alaskan English Achievement"] = float(school[14])
            if "american indian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["American Indian/Alaskan Math Achievement"] = float(school[14])
            if "asian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Asian/Pacific Islander English Achievement"] = float(school[14])
            if "asian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Asian/Pacific Islander Math Achievement"] = float(school[14])
            if "black" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Black English Achievement"] = float(school[14])
            if "black" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Black Math Achievement"] = float(school[14])
            if "economically" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Economically Disadvantaged English Achievement"] = float(school[14])
            if "economically" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Economically Disadvantaged Math Achievement"] = float(school[14])
            if "hispanic" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Hispanic English Achievement"] = float(school[14])
            if "hispanic" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Hispanic Math Achievement"] = float(school[14])
            if "white" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["White English Achievement"] = float(school[14])
            if "white" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["White Math Achievement"] = float(school[14])
            if "disability" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Students With Disability English Achievement"] = float(school[14])
            if "disability" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Students With Disability Math Achievement"] = float(school[14])
            pass
        else:
            dict_certificate1[school[4]] = {}
            dict_certificate1[school[4]]["School Name"] = school[4]
            dict_certificate1[school[4]]["County"] = school[2]
            dict_certificate1[school[4]]["Classification"] = school[6]
            dict_certificate1[school[4]]["All Students English Achievement"] = 0.0
            dict_certificate1[school[4]]["All Students Math Achievement"] = 0.0
            dict_certificate1[school[4]]["American Indian/Alaskan English Achievement"] = 0.0
            dict_certificate1[school[4]]["American Indian/Alaskan Math Achievement"] = 0.0
            dict_certificate1[school[4]]["Asian/Pacific Islander English Achievement"] = 0.0
            dict_certificate1[school[4]]["Asian/Pacific Islander Math Achievement"] = 0.0
            dict_certificate1[school[4]]["Black English Achievement"] = 0.0
            dict_certificate1[school[4]]["Black Math Achievement"] = 0.0
            dict_certificate1[school[4]]["Economically Disadvantaged English Achievement"] = 0.0
            dict_certificate1[school[4]]["Economically Disadvantaged Math Achievement"] = 0.0
            dict_certificate1[school[4]]["Hispanic English Achievement"] = 0.0
            dict_certificate1[school[4]]["Hispanic Math Achievement"] = 0.0
            dict_certificate1[school[4]]["White English Achievement"] = 0.0
            dict_certificate1[school[4]]["White Math Achievement"] = 0.0
            dict_certificate1[school[4]]["Students With Disability English Achievement"] = 0.0
            dict_certificate1[school[4]]["Students With Disability Math Achievement"] = 0.0
            if "all students" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["All Students English Achievement"] = float(school[14])
            if "all students" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["All Students Math Achievement"] = float(school[14])
            if "american indian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["American Indian/Alaskan English Achievement"] = float(school[14])
            if "american indian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["American Indian/Alaskan Math Achievement"] = float(school[14])
            if "asian" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Asian/Pacific Islander English Achievement"] = float(school[14])
            if "asian" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Asian/Pacific Islander Math Achievement"] = float(school[14])
            if "black" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Black English Achievement"] = float(school[14])
            if "black" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Black Math Achievement"] = float(school[14])
            if "economically" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Economically Disadvantaged English Achievement"] = float(school[14])
            if "economically" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Economically Disadvantaged Math Achievement"] = float(school[14])
            if "hispanic" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Hispanic English Achievement"] = float(school[14])
            if "hispanic" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Hispanic Math Achievement"] = float(school[14])
            if "white" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["White English Achievement"] = float(school[14])
            if "white" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["White Math Achievement"] = float(school[14])
            if "disability" in school[7].lower() and "english" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Students With Disability English Achievement"] = float(school[14])
            if "disability" in school[7].lower() and "math" in school[8].lower() and checkFloat(school[14]):
                dict_certificate1[school[4]]["Students With Disability Math Achievement"] = float(school[14])
            pass
    for i in dict_certificate:
        if i in dict_certificate1:
            dict_certificate[i]["2021 All Students English Achievement"] = dict_certificate1[i]["All Students English Achievement"]
            dict_certificate[i]["2021 All Students Math Achievement"] = dict_certificate1[i]["All Students Math Achievement"]
            dict_certificate[i]["2021 American Indian/Alaskan English Achievement"] = dict_certificate1[i]["American Indian/Alaskan English Achievement"]
            dict_certificate[i]["2021 American Indian/Alaskan Math Achievement"] = dict_certificate1[i]["American Indian/Alaskan Math Achievement"]
            dict_certificate[i]["2021 Asian/Pacific Islander English Achievement"] = dict_certificate1[i]["Asian/Pacific Islander English Achievement"]
            dict_certificate[i]["2021 Asian/Pacific Islander Math Achievement"] = dict_certificate1[i]["Asian/Pacific Islander Math Achievement"]
            dict_certificate[i]["2021 Black English Achievement"] = dict_certificate1[i]["Black English Achievement"]
            dict_certificate[i]["2021 Black Math Achievement"] = dict_certificate1[i]["Black Math Achievement"]
            dict_certificate[i]["2021 Economically Disadvantaged English Achievement"] = dict_certificate1[i]["Economically Disadvantaged English Achievement"]
            dict_certificate[i]["2021 Economically Disadvantaged Math Achievement"] = dict_certificate1[i]["Economically Disadvantaged Math Achievement"]
            dict_certificate[i]["2021 Hispanic English Achievement"] = dict_certificate1[i]["Hispanic English Achievement"]
            dict_certificate[i]["2021 Hispanic Math Achievement"] = dict_certificate1[i]["Hispanic Math Achievement"]
            dict_certificate[i]["2021 White English Achievement"] = dict_certificate1[i]["White English Achievement"]
            dict_certificate[i]["2021 White Math Achievement"] = dict_certificate1[i]["White Math Achievement"]
            dict_certificate[i]["2021 Students With Disability English Achievement"] = dict_certificate1[i]["Students With Disability English Achievement"]
            dict_certificate[i]["2021 Students With Disability Math Achievement"] = dict_certificate1[i]["Students With Disability Math Achievement"]
            dict_certificate[i]["19-21 Difference in Math"] = dict_certificate[i]["2021 All Students Math Achievement"] - dict_certificate[i]["All Students Math Achievement"]
            dict_certificate[i]["19-21 Difference in English"] = dict_certificate[i]["2021 All Students English Achievement"] - dict_certificate[i]["All Students English Achievement"]


    # Urban / Rural
    with open("urban_rural.csv") as fin2:
        reader = csv.reader(fin2)
        data_list2 = list(reader)

    for i in dict_certificate:
        dict_certificate[i]["Urban/Rural"] = ""
        for county in data_list2[1:]:
            if county[1].lower() in dict_certificate[i]["County"].lower():
                dict_certificate[i]["Urban/Rural"] = county[5]


    # Deep Data Cleaning
    df = pd.DataFrame.from_dict(dict_certificate).T
    df = df.dropna()
    df = df[(df["All Students English Achievement"] != 0.0) & (df["All Students Math Achievement"] != 0.0) & 
           (df["2021 All Students English Achievement"] != "0.0") & (df["2021 All Students Math Achievement"] != "0.0")]
    
    dict_certificate = df.T.to_dict()
    # To Reorganize the columns
    # Write to a New CSV File      
    csv_columns = ["School Name", "County", "Urban/Rural", "Classification", "19-21 Difference in Math", "19-21 Difference in English",
                "All Students English Achievement", "All Students Math Achievement", 
                "2021 All Students English Achievement", "2021 All Students Math Achievement", 
                "American Indian/Alaskan English Achievement", "American Indian/Alaskan Math Achievement", 
                "Asian/Pacific Islander English Achievement", "Asian/Pacific Islander Math Achievement", 
                "Black English Achievement", "Black Math Achievement", 
                "Economically Disadvantaged English Achievement", "Economically Disadvantaged Math Achievement",
                "Hispanic English Achievement", "Hispanic Math Achievement", "White English Achievement",
                "White Math Achievement", "Students With Disability English Achievement",
                "Students With Disability Math Achievement", 
                "2021 American Indian/Alaskan English Achievement", "2021 American Indian/Alaskan Math Achievement", 
                "2021 Asian/Pacific Islander English Achievement", "2021 Asian/Pacific Islander Math Achievement", 
                "2021 Black English Achievement", "2021 Black Math Achievement", 
                "2021 Economically Disadvantaged English Achievement", "2021 Economically Disadvantaged Math Achievement",
                "2021 Hispanic English Achievement", "2021 Hispanic Math Achievement", "2021 White English Achievement",
                "2021 White Math Achievement", "2021 Students With Disability English Achievement",
                "2021 Students With Disability Math Achievement"]
    with open("CS2316 - 2019 & 2021 Content Mastery Data.csv", "w") as f:
        w = csv.DictWriter(f, csv_columns)
        w.writeheader()
        for k in dict_certificate:
            w.writerow({column: dict_certificate[k].get(column) for column in csv_columns})
    
    return df


############ Function Call ############
data_parser()