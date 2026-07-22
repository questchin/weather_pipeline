import sqlite3 as sql

from src.transform import transform_data

def load_data():
    connection = sql.connect('data/local_weather.db')
    
    df = transform_data()

    df.to_sql(name = 'local_weather', con = connection, if_exists='append')

    return None
