#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine
from config.db import get_db_string

if __name__ == '__main__':
    df = pd.read_csv('../data/fifa2005.csv', encoding = 'utf-8',
                     index_col = 'id')
    overall = df[['overall']]
    potential = [int(str(p[0])[2:]) for p in overall.values]
    overall = [int(str(p[0])[:2]) for p in overall.values]
    df['overall'] = overall
    df['potential'] = potential
    engine = create_engine(get_db_string())
    df.to_sql(name = 'player', con = engine, if_exists = 'append',
              index_label = 'id')

