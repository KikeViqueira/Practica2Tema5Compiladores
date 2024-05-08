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

# Crear la gráfica, ajustando las dimensiones para una mejor visualización
plt.figure(figsize=(20, 10))  # Tamaño aún más ampliado

# Línea de promedios con marcadores para cada punto de medición
plt.plot(promedios.index, promedios, marker='o', linestyle='-', color='b', markersize=5, label='Tiempo Promedio')

# Añadir título y etiquetas
plt.title('Rendimiento del Algoritmo no Optimizado')
plt.xlabel('Valor de N')
plt.ylabel('Tiempo Promedio de Ejecución (s)')

# Configurar el eje Y para empezar en cero y acabar ligeramente por encima del máximo observado
plt.ylim([0, max(promedios) * 1.05])  # Un margen del 5% por encima del máximo para visibilidad

# Configurar el eje y para una mayor precisión
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))

# Configurar el eje X para mostrar sólo algunos valores de N
xticks_values = list(promedios.index[::5]) + [promedios.index[-1]]
xticks_labels = [str(x) for x in xticks_values]  # Etiquetas convertidas a string para visualización
plt.xticks(ticks=xticks_values, labels=xticks_labels, rotation=45)

plt.legend()

# Guardar la figura en un tamaño más grande con menos espacio en blanco
plt.savefig('medidasNoOpt500k.png', dpi=500, bbox_inches='tight')  # Aumentar la resolución para impresión

# Mostrar la gráfica
plt.show()
