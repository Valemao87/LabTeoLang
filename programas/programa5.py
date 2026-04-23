# -*- coding: utf-8 -*-
import re
import sys
import programa2
import programa4
def programa5(RutaPdf,RutaXML):
    #aca sacamos los dos tipos de archivos que tenemos para analizar en particular
    #programa2 lo devuelve como tupla la infromacion fecha y monto
    #programa4 devuelve un texto pleno para analizar
    resultado = False
    facturapdf=programa2.programa2(RutaPdf)
    bancariaxml=programa4.programa4(RutaXML)
    #target lo usamos para generar la expresion regular que buscamos con f
    #notar que usamos """ """ que es para decir la expresion contine "" y es para diferenciar
    target = f""" Importe="{facturapdf[1]}" Fecha="{facturapdf[0]}" """
    #guardamos en rexml todas las veces que aparece el target en bancariasxml
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
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
