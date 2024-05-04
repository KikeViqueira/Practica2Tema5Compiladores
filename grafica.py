import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Ruta al archivo Excel
archivo_excel = 'medidasNoOpt500k.xlsx'

# Leer el archivo Excel
df = pd.read_excel(archivo_excel, index_col=0)

# Convertir columnas a numérico porque pandas a veces importa números como texto
df.columns = pd.to_numeric(df.columns, errors='coerce')

# Calcular promedios para cada valor de N
promedios = df.mean(axis=0)

# Crear la gráfica
plt.figure(figsize=(20, 10))  # Tamaño ampliado para una mejor visualización

# Línea de promedios con marcadores para cada punto de medición
plt.plot(promedios.index, promedios, marker='o', linestyle='-', color='b', markersize=4, label='Tiempo Promedio')

# Añadir título y etiquetas
plt.title('Rendimiento del Algoritmo por Tamaño de Problema N')
plt.xlabel('Valor de N')
plt.ylabel('Tiempo Promedio de Ejecución (s)')

# Configurar el eje Y para reflejar exactamente los valores mínimo y máximo observados
plt.ylim([promedios.min(), promedios.max()])

# Configurar el eje y para una mayor precisión
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))

# Configurar el eje X para mostrar sólo algunos valores de N pero considerar todos los puntos
xticks_values = list(promedios.index[::5]) + [500000]  # Asegurar que todos son enteros
xticks_labels = [str(x) for x in xticks_values]  # Etiquetas convertidas a string para visualización
plt.xticks(ticks=xticks_values, labels=xticks_labels, rotation=45)

plt.legend()

# Guardar la figura
plt.savefig('grafica_tiempos_precisos.png')

# Mostrar la gráfica
plt.show()
