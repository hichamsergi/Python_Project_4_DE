import pandas as pd
from datetime import datetime as dt
import glob


# ETL (Extract Transform Load):

## Extract phase:

def trans_csv(csvdata):
    '''
    Generar un DF con datos CSV
    '''
    df_csv = pd.read_csv(csvdata)

    return df_csv

def trans_json(jsondata):
    '''
    Generar un DF con datos JSON
    '''
    df_json = pd.read_json(jsondata)

    return df_json

def extract():
    '''
    Extaer todos los datos CSV y JSON
    '''
    # DT ensambler:
    df = pd.DataFrame(columns=['Nombre','Altura','Peso'])


    # Read CSV files:
    for csv_file in glob.glob("*.csv"):
        df = pd.concat([df,trans_csv(csv_file)], ignore_index=True)

    #Read JSON file:
    for json_file in glob.glob("*.json"):
        df = pd.concat([df,trans_json(json_file)], ignore_index=True)

    return df

print(extract())

## Transform phase:
## Load phase:

##Logging phase:
