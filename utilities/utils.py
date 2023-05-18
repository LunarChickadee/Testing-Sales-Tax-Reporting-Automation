
import csv
#these are the utilities to make selenium able to use our data


# pull from csv
def read_data_from_csv(filename):
    #create an empty list
    datalist = []

    #open CSV in "read" mode
    csvdata = open(filename, "r")

    #create a CSV reader for our new file
    reader = csv.reader(csvdata)

    #skips header
    next(reader)

    #append CSV rows to list
    for rows in reader:
        datalist.append(rows)
    return datalist