# Basic ETL project:
En este mini-proyecto, se pretende generar un sistema basico de ETL de Extracción de datos en sistema imperial, de diferentes fuentes, para su posterior transformación de datos a sistema metrico.

La organización del directorio es la siguiente:
    
* **`basic_ETL.py`**: Este documento contiene el sistema **ETL**. Solo hace falta ejecutarlo para poder recibir la recopilación de datos en el documento `final_file.csv`, también se genera el documento `logging_file.txt`, que contendría los logs de ejecución de todo el proceso.

* **`usuarios.csv`** y **`usuarios.json`**: Son los documentos que contienen los datos de 100 usuarios, cada uno, que recibirá el sistema **ETL** para su posterior transformación.
---

Ejemplo de ejecución:
```
tester@ETL-SYSTEM:~/Python_Project_4_DE/modulo-1$ python3 basic_ETL.py
```