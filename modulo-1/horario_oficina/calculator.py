# Imports:
import pandas as pd
import os
import glob
from tabula import read_pdf

#ETL:

## Extract:
def extract_pdfdata():
    '''
    Genera un DF con datos de los PDF
    '''
    BASEDIR = os.path.dirname(__file__)

    DATADIR = os.path.join(BASEDIR, "data")

    all_df = []

    for pdffile_data in glob.glob(os.path.join(DATADIR, "*.pdf")):
        
        print(f'Extracting data from: {pdffile_data}')

        df_info = read_pdf(pdffile_data, pages='all', stream=True, multiple_tables=True)

        df_pdf = pd.concat(df_info, ignore_index=True)

        all_df.append(df_pdf)

    return all_df

## Transform:


## Load-Log:


# Calculate:
## Ruta a los datos:

extract_pdfdata()