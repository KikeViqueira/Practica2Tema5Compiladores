import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Rutas a los archivos Excel
archivo_excel1 = 'medidasNoOpt500k.xlsx'
archivo_excel2 = 'otroArchivo.xlsx'

# Leer los archivos Excel
df1 = pd.read_excel(archivo_excel1, index_col=0)
df2 = pd.read_excel(archivo_excel2, index_col=0)

# Convertir columnas a numérico
df1.columns = pd.to_numeric(df1.columns, errors='coerce')
df2.columns = pd.to_numeric(df2.columns, errors='coerce')

# Calcular promedios para cada valor de N en ambos DataFrames
promedios1 = df1.mean(axis=0)
promedios2 = df2.mean(axis=0)

# Crear la gráfica
plt.figure(figsize=(20, 10))  # Tamaño ampliado para mejor visualización

# Línea de promedios para el primer archivo
plt.plot(promedios1.index, promedios1, marker='o', linestyle='-', color='b', markersize=4, label='Tiempo Promedio Archivo 1')

# Línea de promedios para el segundo archivo
plt.plot(promedios2.index, promedios2, marker='o', linestyle='-', color='r', markersize=4, label='Tiempo Promedio Archivo 2')

# Añadir título y etiquetas
plt.title('Comparación de Rendimiento por Tamaño de Problema N')
plt.xlabel('Valor de N')
plt.ylabel('Tiempo Promedio de Ejecución (s)')

# Configurar el eje y para una mayor precisión
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))

# Configurar los ticks del eje X
xticks_values = list(set(promedios1.index).union(set(promedios2.index)))
xticks_labels = [str(x) for x in xticks_values]
plt.xticks(ticks=xticks_values, labels=xticks_labels, rotation=45)

plt.legend()

# Guardar la figura
plt.savefig('comparativa_tiempos.png')

# Mostrar la gráfica
plt.show()
