#!/usr/local/bin/python3
from matplotlib import pyplot as plt

def main():
    gold_gdp()
    gold_pop()
    medals_pop()
    medals_gdp()
    medals_lit()

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
    plt.show()

    plt.xcorr(g_m_list, gdp_list)
    plt.show()

def gold_pop():
    c_list = list()
    pop_list = list()
    g_m_list = list()
    with open("gold-pop.csv", "r") as file:
        for line in file:
            country, pop, gold = line.split(',')
            c_list.append(country)
            pop_list.append(float(pop))
            g_m_list.append(int(gold))
    plt.bar(range(len(c_list)), g_m_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Gold medals per country")
    plt.show()
    
    plt.bar(range(len(c_list)), pop_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Population")
    plt.xlabel("Countries")
    plt.title("Popluation by country")
    plt.show()

    plt.xcorr(g_m_list, pop_list)
    plt.show()

def medals_pop():
    c_list = list()
    pop_list = list()
    g_m_list = list()
    with open("medals-pop.csv", "r") as file:
        for line in file:
            country, pop, gold = line.split(',')
            c_list.append(country)
            pop_list.append(float(pop))
            g_m_list.append(int(gold))
    plt.bar(range(len(c_list)), g_m_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Total medals per country")
    plt.show()
    
    plt.bar(range(len(c_list)), pop_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Population")
    plt.xlabel("Countries")
    plt.title("Popluation by country")
    plt.show()

    plt.xcorr(g_m_list, pop_list)
    plt.show()

def medals_gdp():
    c_list = list()
    gdp_list = list()
    g_m_list = list()
    with open("medals-gdp.csv", "r") as file:
        for line in file:
            country, gdp, gold = line.split(',')
            c_list.append(country)
            gdp_list.append(float(gdp))
            g_m_list.append(int(gold))
    plt.bar(range(len(c_list)), g_m_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Total medals per country")
    plt.show()
    
    plt.bar(range(len(c_list)), gdp_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("GDP per capita")
    plt.xlabel("Countries")
    plt.title("GDP per capita by country")
    plt.show()

    plt.xcorr(g_m_list, gdp_list)
    plt.show()

def medals_lit():
    c_list = list()
    lit_list = list()
    g_m_list = list()
    with open("medals-lit.csv", "r") as file:
        for line in file:
            country, lit, medals = line.split(',')
            c_list.append(country)
            lit_list.append(float(lit))
            g_m_list.append(int(medals))
    plt.bar(range(len(c_list)), g_m_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("Medals")
    plt.xlabel("Countries")
    plt.title("Gold medals per country")
    plt.show()
    
    plt.bar(range(len(c_list)), lit_list, align='center')
    plt.xticks(range(len(c_list)), c_list, rotation='90')
    plt.ylabel("GDP per capita")
    plt.xlabel("Countries")
    plt.title("Literacy by country")
    plt.show()

    plt.xcorr(g_m_list, lit_list)
    plt.show()

if __name__ == "__main__":
    main()