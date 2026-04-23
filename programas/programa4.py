# -*- coding: utf-8 -*-
import re
import sys
def programa4(RutaXML):
    #Aca usamos with que abre y cierra el archivo una vez salido del bloque, open que lo abre
    #el archivo que habre RutaXML y la operacion "r" de read y
    #el encoding que refiere a que acepta todos los digitos de 8 bits representados
    #as f es para indicar a donde va lo leido
    with open(RutaXML, "r", encoding="utf-8") as f:
        text =" " 
        text=f.read()
     #read se usa para leer como string lo que se encuentra en f y luego pasarlo a text
    return text
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa4(entrada)      # ejecutar 
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
