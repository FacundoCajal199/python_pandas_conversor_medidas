import pandas as pd

data = {
    "piezas:": ["pata","tablero","puerta","estante","papel lateral"],
    "centimetros": [40,120,60,30,180]
}

df = pd.DataFrame(data)


#guardar el dataFrame en un archivo de exel

df.to_excel("muebles_medidas.xlsx", index= False)