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

        target = f""" Importe="{monto}" Fecha="{fecha}" """
        
        target_text = xml

        xml = re.sub(target, "", target_text)




        #Cambiar contador de importes
        #First find the number, then minus one it

        
        num_text = xml
        num = re.search(r"<BanTeng:TotalMovimientos>(\d+)", num_text)
        if num:
            num = int(num.group(1)) -1 

        #Now sub

        result = re.sub(r"(<BanTeng:TotalMovimientos>)(\d+)", r"\1" + str(num), xml)

        return result


        
    else: return xml


 

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
