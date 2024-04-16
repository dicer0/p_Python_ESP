import pandas as pd

# Supongamos que df es tu DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Nueva fila que quieres añadir
nueva_fila = pd.DataFrame({'A': ['nuevo_valor_A'], 'B': ['nuevo_valor_B']})

# Concatenar la nueva fila con el DataFrame original
df = pd.concat([nueva_fila, df], ignore_index=True)

print(df)