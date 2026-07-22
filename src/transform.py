from datetime import datetime
import pandas as pds

from src.extract import get_data_from_URL


def transform_data():
    rawData = get_data_from_URL()
    #print(rawData['current'])

    current = rawData['current']
    current2 = rawData.get('current',{})
    # print(current)
    # print(current2)

    # clean up the column names.
    colMap = {
            'temperature_2m':'temperature',
            'relative_humidity_2m':'humidity',
            'wind_speed_10m':'wind_speed',
            }

    expectedCols = [
            'temperature',
            'humidity',
            'wind_speed'
            ]

    df = pds.DataFrame([current])
    df = df.rename(columns=colMap)
    df = df[expectedCols]

    df['timestamp'] = datetime.now()

    print(df)

    return df
