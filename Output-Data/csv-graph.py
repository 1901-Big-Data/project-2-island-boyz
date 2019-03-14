#!/usr/local/bin/python3
from matplotlib import pyplot as plt

def main():
    gold_gdp()

def gold_gdp():
    c_list = list()
    gdp_list = list()
    g_m_list = list()
    with open("gold-gdp.csv", "r") as file:
        for line in file:
            country, gdp, gold = line.split(',')
            c_list.append(country)
            gdp_list.append(gdp)
            g_m_list.append(gold)
    
    plt.bar(c_list, g_m_list)
    plt.xticks(c_list, rotation='65')
    plt.yticks(g_m_list)
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Countries GDP per capita\nand Gold medals")
    plt.show()

if __name__ == "__main__":
    main()