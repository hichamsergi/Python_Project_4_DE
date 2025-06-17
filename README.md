# Python Project for Data Engineering

Este repositorio se utilizará para llevar a cabo un proyecto de Python para la Ingeniería de Datos, como parte del certificado de IBM de *Python Project for Data Engineering*.

Para poder llevar a cabo el proyecto, se tomará el rol de un ingerniero de datos y se utilizarán técnicas de *web scraping* y transformación de datos, para poder almacenarlos en bases de datos a las que poder hacer *queries* mediante Python.

**ÍNDICE:**
1. [Módulo 1](#módulo-1)
2. [Módulo 2](#módulo-2)

## MÓDULO 1:

* Básicos del ETL (Extract Transform and Load).
* Extraccion de datos utilizando *web scraping*.
* Query a bases de datos mediante Python.

### 1. Extract, Transform and Load (ETL):
El concepto de ETL simplemente describe el flujo de trabajo que consiste en la **extracción** de datos, como podria ser la recopilación de datos desde diferentes fuentes y formatos. Posteriormente, la **transformación** de dichos datos, como podría ser la transformación de datos del sistema imperial al sistema métrico. Y finalmente, la **carga** de los datos transformados en un documento recopilatorio y transformado.

#### 1.1. *Extract*:
Ejemplo:

(*suponemos que en le directorio activo existen un conjunto de documentos .csv y .json*)
```python

import pandas as pd
from datetime import datetime
import glob

def extract_csvdata(file_in_csv):
    '''
    Function 2 generate a DF from csv file
    '''
    dataframe = pd.read_csv(file_in_csv)
    return dataframe

def extract_jsondata(file_in_json):
    '''
    Function 2 generate a DF from json file
    '''
    dataframe = pd.read_json(file_in_json)
    return dataframe

def extract():

    # Generamos un DF con las columnas de 'nombre', 'altura' y 'peso':
    extracted_data = pd.DataFrame(columns=['name','height','weight'])

    for csv_file in glob.glob('*csv'):
        extracted_data = extracted_data.append(extract_csvdata(csv_file), ignore_index=True)

    
    for json_file in glob.glob('*.json'):
        extracted_data = extracted_data.append(extract_jsondata(json_file), ignore_index=True)


    return  extracted_data
```

(*Breve explicación del funcionamiento de la función glob.glob()* ):
```python
list_csv = glob.glob('*.csv')
    #list_csv:['file1.csv','file2.csv','file3.csv']

list_json = glob.glob('*.json')
    #list_json:['file1.json','file2.json','file3.json']
```


#### 1.2. *Transform*:
Ejemplo:

```python

def transform(data):

    #Transformamos los datos de sistema imperial a sistema metrico:    
    data['height'] = round(data.height * 0.0254,2)

    data['weight'] = round(data.weight * 0.45359237,2)

    return data
```

#### 1.3. *Load* and logging:
Ejemplo:

```python
def load(targetfile,data_2_load):
    data_2_load.to_csv(targetfile,index=False) # Convertimos el DF en un csv file de nombre targetfile
```

Para poder cargar los datos necesitamos generar una entrada de registro:

```python

def log(message):

    timestamp_format = '%Y-%h-%d-%H:%M:%S'

    now = datetime.now()

    timestamp = now.strftime(timestamp_format)

    with open('logfile.txt','a') as f:
        f.write (timestamp + ',' + message + '\n')
```

Una vez definidas todas las funciones del proceso *ETL* lo que nos queda es llamar a las funciones para poder utilizarlas:

```python
log('ETL job started')


log('Extract phase started')
extracted_data = extract()
log('Extract phase ended')

log('Transform phase started')
transformed_data = transform(extracted_data)
log('Transform phase ended')

log('Load phase started')

targetfile = 'transformed_data.csv'

load(targetfile, transformed_data) # Atribuimos a targetfile, un documento vacio, 
                                   # el contenido del documento lo rellenamos con 
                                   # los valores del DF,transformed_data,
                                   # generado en las fases anteriores.
log('Load phase ended')
log('ETL job ended')
```

### 2. WEB SCRAPING:
De la descripción literal del inglés, *web scraping* define el hecho de "rascar la web", o extraer datos de la web. Consiste en analizar los datos y la informacion contenida en una web mediante *metodos HTTP* y la normalización de la información extraida. Podemos hacerlo de la siguiente forma:

```python
from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head>..." # Simulamos que hemos recogido información de una web

soup = BeautifulSoup(html, 'html5lib')
```

**Beautiful Soup** nos permite organizar el HTML de una web como si fuera una estructura de datos anidados. De esta forma convertimos dicho HTML en un conjunto de objetos en forma de arbol, con metodos que nos permiten analizar el HTML.

Como utilizar **Beautiful Soup**:

```python

title_object = soup.title
#
# title_object:
#       <title>Page Title</title>
#

head_object = soup.h3
#
# head_object:
#       <h3>
#           <b id='boldest'>Lebron James</b>
#       </h3>
#
# En el caso de haber mas de 1 objeto con el mismo "tag", solo recoge el primer "tag"

tag_hijo = head_object.b
tag_parent = tag_hijo.parent
#
# tag_hijo:
#       <b id='boldest'>Lebron James</b>
#
# tag_parent tiene el mismo contenido que head_object

tag_hermano = head_object.next_sibling
#
# tag_hermano:
#       <p> Salary: $ 92,000,000</p>

tag_hijo.attrs
tag_hijo.string
#
# tag_hijo.attrs:
#       {'id':'boldest'}
#
# tag_hijo.string:
#       'Lebron James'

players_name = soup.find_all(name='h3')
#
# players_name:
#       <h3><b id='boldest'>Lebron James</b></h3>
#       <h3><b id='mr3'>Stephen Curry</b></h3>
#       <h3><b id='goat'>Michael Jordan</b></h3>
#
# El método find_all nos permite almacenar los descencientes de todas las etiquetas que 
#  coincidan con la busqueda, en este caso todas las etiquetas 'h3'

players_name[1]

sec_name = players_name[1]
sec_name.b
#
# players_name[1]:
#       <h3><b id='mr3'>Stephen Curry</b></h3>
#
# sec_name.b:
#       <b id='mr3'>Stephen Curry</b>
```

## MÓDULO 2:
* Flujo de trabajo ETL.
* Proyecto práctico.