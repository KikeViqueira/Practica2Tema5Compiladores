import os
import sys
import subprocess
from openpyxl import Workbook

#Nombre del archivo excel donde se guardaran los datos
archivo = 'medidasOpt1M.xlsx'

#Función para ejecutar el script ./nopt y capturar sus resultadps
def ejecutar_script(i):
  resultados = []
  for N in range(1000000, 5000001, 100000):
    #Ejecutamos el script ./nopt con el valor de N actual y capturamos su salida
    salida = subprocess.run(['./nopt', str(N)] ,capture_output=True, text=True)
    tiempo= salida.stdout.strip() #extraemos el tiempo de ejecucuión limpiando los espacios en blanco
    resultados.append(tiempo)
  return resultados

#Función principal del programa
def main():
    try:
        wb = Workbook() #Creamos un nuevo libro de trabajo
        ws = wb.active #Obtenemos la hoja activa
        #Escribimos los encabezados
        ws.append(['i'] + [str(N) for N in range(1000000, 5000001, 100000)])
        for i in range(1, 6):
          resultados = ejecutar_script(i) #Ejecutamos el script ./nopt y capturamos sus resultados
          ws.append([i]+resultados) #Escribimos los resultados en el archivo excel
        wb.save(archivo) #Guardamos el archivo excel
        print(f'Archivo {archivo} se ha actualizado con éxito')

    except Exception as e:
       print(f'Error: {e}')
       sys.exit(1)

if __name__ == '__main__':
    main()   

       



  