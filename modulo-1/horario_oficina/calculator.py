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

    df_alldata = pd.DataFrame()

    for pdffile_data in glob.glob(os.path.join(DATADIR, "*.pdf")):

        
        df_pdf = read_pdf(pdffile_data, pages='all', stream=True)
      
        df_alldata = pd.concat(df_alldata, df_pdf, ignore_index=True)

    return df_alldata

## Transform:


## Load-Log:


# Calculate:
## Ruta a los datos:

print(extract_pdfdata())