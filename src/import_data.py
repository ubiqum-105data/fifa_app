#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine
from config.db import get_db_string

# bidimensional array containing 2-sized arrays, where a[0][0] = the relative
# file path for the data to be imported and a[0][1] contains the name of the
# table
IMPORT_DATA = [
    #['../data/fifa2005.csv', 'fifa_2005'],
    #['../data/fifa2006.csv', 'fifa_2006'],
    #['../data/fifa2007.csv', 'fifa_2007'],
    #['../data/fifa2008.csv', 'fifa_2008'],
    #['../data/fifa2009.csv', 'fifa_2009'],
    #['../data/fifa2010.csv', 'fifa_2010'],
    #['../data/fifa2011.csv', 'fifa_2011'],
    #['../data/fifa2012.csv', 'fifa_2012'],
    ['../data/fifa2013.csv', 'fifa_2013'],
    ['../data/fifa2014.csv', 'fifa_2014'],
    ['../data/fifa2015.csv', 'fifa_2015'],
    ['../data/fifa2016.csv', 'fifa_2016'],
    ['../data/fifa2017.csv', 'fifa_2017'],
    ['../data/fifa2018.csv', 'fifa_2018'],
    ['../data/fifa2018wc.csv', 'fifa_2018wc'],
    ['../data/fifa2019.csv', 'fifa_2019'],
]

if __name__ == '__main__':
    for d in IMPORT_DATA:
        try:
            df = pd.read_csv(d[0], encoding = 'utf-8',
                             index_col = 'id')
            if 'edition' in df:
                df = df.drop(columns = ['edition'])
            #overall = df[['overall']]
            #potential = [int(str(p[0])[2:]) for p in overall.values]
            #overall = [int(str(p[0])[:2]) for p in overall.values]
            #df['overall'] = overall
            #df['potential'] = potential
            engine = create_engine(get_db_string())
            df.to_sql(name = d[1], con = engine, index_label = 'id')
        except:
            continue

