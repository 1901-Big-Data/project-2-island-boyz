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
            gdp_list.append(float(gdp))
            g_m_list.append(int(gold))
    '''
    plt.bar(range(len(c_list)), g_m_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Gold medals per country")
    plt.show()
    
    plt.bar(range(len(c_list)), gdp_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("GDP per capita")
    plt.xlabel("Countries")
    plt.title("GDP per capita by country")
    '''

    plt.xcorr(g_m_list, gdp_list)


    plt.show()

if __name__ == "__main__":
    main()