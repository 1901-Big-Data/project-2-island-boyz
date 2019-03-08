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
            #print(num)
            out.write(line)
    out.close()

if __name__ == "__main__":
    main()