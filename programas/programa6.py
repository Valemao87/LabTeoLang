# -*- coding: utf-8 -*-
import re
import sys
import programa2
import programa4
import programa5
def programa6(RutaPdf,RutaXML):

#Lo que hay que hacer aca es aggarar el importe de el PDF (Monto y fecha) utilizando programa2
#Luego utilizando el programa4 chekeamos con el programa 5 si el monto y fecha estan o no en el XML
#Si FALSE no hacer nada
#Si TRUE entonces eliminar el moviemiento por completo preservando la estrucutura de el XML y ademas actualiznado la cantidade de importes totales



#1 monto y fecha
    pdf = programa2.programa2(RutaPdf)
    fecha = pdf[0]
    monto = pdf[1]

#2 XML en string y no como un objeto
    xml = programa4.programa4(RutaXML)

#3 Chekear si monto y fecha estan en el XML
    
    if programa5.programa5(RutaPdf,RutaXML): 
        #deletear la linea
        xml
        #Cambiar contador de importes
    else: return xml


 

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
