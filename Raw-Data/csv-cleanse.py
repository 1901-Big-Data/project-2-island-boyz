#!/usr/local/bin/python3
import re

def main():
    cleanse()

def cleanse():
    out = open("athletes.csv", "w")
    with open("athlete_events.csv", "r") as file:
        for line in file:
            line = line.replace(', ', ' ')
            num = re.findall('\s\d+,\d+\s', line)
            num = str(num).replace(',', '')
            num = str(num).replace('[\'', '')
            num = str(num).replace('\']', '')
            line = re.sub('\s\d+,\d+\s', str(num), line)
            line = line.replace('\"', '')
            out.write(line)
    out.close()

def clean_world():
    out = open("countries.csv", "w")
    with open("countries_data.csv", "r") as file:
        for line in file:
            line = line.split(',')
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            myList = ','.join(map(str, line)) 
            out.write(myList)
    out.close()

if __name__ == "__main__":
    main()