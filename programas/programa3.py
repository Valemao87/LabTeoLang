# -*- coding: utf-8 -*-
import re
import sys
import programa1

def programa3(RutaFactura):
    
    texto = programa1.programa1(RutaFactura)
    
    res = ""
    lineas = texto.split("\n")

    
    patron = r"^\s*(\d+)\s+(.+?)\s+(\d+\s*,\s*\d{2})\s+(\d+\s*,\s*\d{2})\s*$"
    
    for linea in lineas:
        m = re.match(patron, linea)
        if m:
            cant = m.group(1)
            desc = m.group(2)
            precio = m.group(3)
            total = m.group(4)
            
            res += f"Cant: {cant} |Desc: {desc} | {precio} c/u |Total:  {total}\n"
    
    return res
    
if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
