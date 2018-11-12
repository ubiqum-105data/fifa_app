#!/usr/bin/python3
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('data/fifa2005.csv')
    overall = df[['overall']]
    potential = [int(str(p[0])[2:]) for p in overall.values]
    overall = [int(str(p[0])[:2]) for p in overall.values]
    df['overall'] = overall
    df['potential'] = potential
