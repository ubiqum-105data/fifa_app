#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine
from config.db import get_db_string

# bidimensional array containing 2-sized arrays, where a[0][0] = the relative
# file path for the data to be imported and a[0][1] contains the name of the
# table
IMPORT_DATA = [
    ['../data/fifa2005.csv', 'fifa_2005'],
    ['../data/fifa2006.csv', 'fifa_2006'],
    ['../data/fifa2007.csv', 'fifa_2007'],
    ['../data/fifa2008.csv', 'fifa_2008'],
    ['../data/fifa2009.csv', 'fifa_2009'],
    ['../data/fifa2010.csv', 'fifa_2010'],
]

if __name__ == '__main__':
    for d in IMPORT_DATA:
        df = pd.read_csv(d[0], encoding = 'utf-8',
                         index_col = 'id')
        if 'edition' in df:
            df = df.drop(columns = ['edition'])
        overall = df[['overall']]
        potential = [int(str(p[0])[2:]) for p in overall.values]
        overall = [int(str(p[0])[:2]) for p in overall.values]
        df['overall'] = overall
        df['potential'] = potential
        engine = create_engine(get_db_string())
        df.to_sql(name = d[1], con = engine, index_label = 'id')

