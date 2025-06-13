import pandas as pd
from datetime import datetime
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
    # DF ensambler:
    df = pd.DataFrame(columns=['Nombre','Altura','Peso'])


    # Read CSV files:
    for csv_file in glob.glob("*.csv"):
        df = pd.concat([df, trans_csv(csv_file)], ignore_index=True)

    #Read JSON file:
    for json_file in glob.glob("*.json"):
        df = pd.concat([df, trans_json(json_file)], ignore_index=True)

    return df

## Transform phase:
def transform(data2transform):
    '''
    Transforma los valores en sistema imperial a sistema métrico 
    '''
    #Transfrom data of 'Altura' column:
    data2transform[['Altura']] = round(data2transform[['Altura']] * 2.54, 2)

    #Transform data of 'Peso' column:
    data2transform[['Peso']] = round(data2transform[['Peso']] * 0.453592, 2)

    data2transform = data2transform.rename(columns={'Altura':'Altura (cm)','Peso':'Peso(kg)'})

    return data2transform

## Load phase:
def load(data2load):
    '''
    Cargar datos en un documento csv de datos conjuntos
    '''

    #Load the DF data into a CSV file excluding the index column:
    data2load.to_csv('final_file.csv', index=False)
    print("Final file generated, check it!")


##Logging phase:
def logging(message):
    '''
    Función de logging para registrar la fases de la ejecución
    '''
    with open('logging_file.txt','a') as file:

        #Adding a newline tot the logging file with the message and date:
        file.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S " + message) + '\n' )


logging('Starting the ETL process')
logging('Extraction phase started')
dfs_extracted = extract()
logging('Extraction phase ended')
logging('Transform phase started')
dfs_transformed = transform(dfs_extracted)
logging('Transform phase ended')
logging('Load phase started')
load(dfs_transformed)
logging('Load phase ended')
logging('ETL process ended')