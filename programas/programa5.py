# -*- coding: utf-8 -*-
import re
import sys
import programa2
import programa4
def programa5(RutaPdf,RutaXML):
    resultado = False
    facturapdf=programa2.programa2(RutaPdf)
    bancariaxml=programa4.programa4(RutaXML)

    target = f""" Importe="{facturapdf[1]}" Fecha="{facturapdf[0]}" """

    rexml=re.findall( target ,bancariaxml)

    if rexml:     
        resultado = True 


    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
