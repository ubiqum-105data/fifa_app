import sqlalchemy
from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from config.db import get_db_string

some_engine = create_engine(get_db_string())
#Session = sessionmaker(bind=some_engine)
#session = Session()

sql = text('SELECT fifa_2005.name, fifa_2005.nation, fifa_2005.overall, fifa_2006.overall FROM fifa_2005, fifa_2006 WHERE fifa_2005.name = fifa_2006.name')
result = some_engine.execute(sql)

for i in result:
   print(i)

