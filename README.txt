Descripción General
El conjunto de scripts que se encuentra dentro de la carpeta archivos, se utiliza para medir, registrar y visualizar el rendimiento de ejecutables específicos bajo diferentes condiciones de carga de trabajo. El proceso se divide en tres partes principales: generación de datos, visualización individual y comparación de rendimientos.



programa.py
Este script automatiza la ejecución de un programa ejecutable múltiples veces con diferentes tamaños de entrada N y registra los tiempos de ejecución en un archivo Excel. Es esencial que el ejecutable haya sido compilado con la opción -O0 para garantizar que no se apliquen optimizaciones adicionales que podrían afectar los resultados de la medición.

Funcionalidades:
Ejecución Automatizada: Ejecuta el script objetivo ./ejecutable con valores incrementales de N y captura el tiempo de ejecución.
Registro de Datos: Los resultados se almacenan en un archivo Excel, medidasOpt1M.xlsx, con una fila para cada ejecución y una columna para cada tamaño de problema N.

Configuración:
Cambiar el nombre del ejecutable en la función ejecutar_script si se desea medir otro programa.
Modificar el rango de N para los distintos casos de prueba que se quieran probar.
Modificar el valor de i para indicar cuantas veces se tiene que repetir el caso de prueba y este tener múltiples medidas y más fiables.

Nota: En el caso de mis pruebas:
	-> Con N de 10000 a 500000 la i fue range(1,11) por lo que la función ejecutar_script se ejecutó 10 veces.
	-> Con N de 1000000 a 5000000 la i fue range(1,6) por lo que la función ejecutar_script se ejecutó 6 veces.





GraficaIndividual.py
Este script lee los datos de tiempo de ejecución de un archivo Excel creado con el anterior programa y genera un gráfico que muestra el rendimiento del algoritmo.

Funcionalidades:
Lectura de Datos: Carga los tiempos de ejecución desde un archivo Excel especificado.
Visualización de Datos: Genera una gráfica de los tiempos promedio de ejecución contra los tamaños de entrada.

Configuración:
Asegurarse de que el archivo Excel exista en la directorio de trabajo y contenga los datos adecuados.
Modificar el título y etiquetas del gráfico según corresponda al contenido del archivo Excel (Según queramos la gráfica del optimizado o del no Optimizado).





ConjuntoGraficas.py
Este script compara visualmente el rendimiento de dos versiones de un algoritmo (optimizado y no optimizado) utilizando datos de dos archivos Excel diferentes.

Funcionalidades:
Comparación Visual: Carga los datos de dos archivos Excel y los grafica en la misma visualización para comparar directamente el rendimiento.

Configuración:
Asegurarse de que los nombres de los archivos Excel sean correctos y estén presentes en el directorio del script.
El archivo excel1 siempre debe contener los datos del algoritmo no optimizado, y excel2 los del optimizado.





Uso General:
Para ejecutar estos scripts, necesitarás un entorno de Python con las bibliotecas pandas, matplotlib y openpyxl instaladas. Los scripts se pueden ejecutar directamente desde la línea de comandos, con el siguiente comando: python3 nombreScript.py
