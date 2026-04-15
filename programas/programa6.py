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
    xml = programa4.programa4(RutaXML)

    if programa5.programa5(RutaPdf,RutaXML): 
        
        #1 Construir target
        pdf = programa2.programa2(RutaPdf)
        fecha = pdf[0]
        monto = pdf[1]
        target = f""" Importe="{monto}" Fecha="{fecha}" """

        target_text = xml

        #La syntax de este sub es: rf significa una regular experission que tabien es una "F-string" (Formated String) lo que permite concatenar variables
        # Adentro de los "" de rf"" el ^ significa que va a buscar al inicio de cada linea, .* siginica: 
        # [ . ] = cualquier caracter menos un newline (\n)
        # [ .* ] = cantidad no especificada de cualquier caracter 
        # [\n?] = Puede, puede no, haber un new line al final de la linea 
        #El target esta adentro de re.escape() para que python lo interprete como la variable tipo string que es y no como la strig = "target"

        #Efectivamente rf"^.*{re.escape(target)}.*\n?" signifca:
            #Busco el patro desde el inicio de cada linea (^) donde desde elinicio puede haber una cantidad no especificada de caracteres (.*) donde el target va estar, y despues de el target puede haber una cantidad no especidicada de caracteres (.*) y puede haber un brakline al final
        #la flag multine signifca que va ejecutar el search paa toda linea, efectivamente cambia el comportamiento de (^) para que resete la busqueda a cada linea
        xml = re.sub(rf"^.*{re.escape(target)}.*\n?", "", target_text, flags=re.MULTILINE)
        
        #Cambiar contador de importes
        
        num_text = xml
        num = re.search(r"<BanTeng:TotalMovimientos>(\d+)", num_text)
        if num:
            target = str(num.group(1))
            num = str(int(num.group(1)) -1) 

        #Now sub

        result = re.sub(rf"(?<=<BanTeng:TotalMovimientos>){re.escape(target)}", str(num), xml)

        with open("debug.txt", "a") as debug:
            debug.write("Target: " + target + "\n" + "Num: " + num + "\n")

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
