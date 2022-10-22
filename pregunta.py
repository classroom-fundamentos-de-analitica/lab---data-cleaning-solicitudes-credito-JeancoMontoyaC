import re
import pandas as pd
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
 
    df.dropna(axis = 0, inplace = True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[columna] = df[columna].str.lower()
        df[columna] = df[columna].apply(lambda x: x.replace('_', ' '))
        df[columna] = df[columna].apply(lambda x: x.replace('-', ' '))
        df[columna]=df[columna].apply(lambda x: x.replace('.', ' '))
    
    df['monto_del_credito'] = df['monto_del_credito'].replace(regex="\$[\s*]", value="")
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace(",", ""))
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace(".00", ""))


    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.search("^\d+/", x).group())-1 == 4) else datetime.strptime(x, "%d/%m/%Y"))
    df.drop_duplicates(inplace = True)

    return df
