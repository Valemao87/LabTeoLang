# -*- coding: utf-8 -*-
import re
import sys
from pypdf import PdfReader

def programa1(RutaPdf): 

    #Sets pdf as the pdf content in RutaPdf using PdfReader fucntion thing
      
    pdf = PdfReader(RutaPdf)


    # inicializacion de la variable text como string 
    
    text = "" 

    #Iterate trough the pages in pdf and append (concatenacion) them in text variable
    # the function extract_text returns either text or "" if no text was found, thats why the "or" is needed 
    
    for page in pdf.pages: 
        text += page.extract_text(layout=True) or ""
    
    
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
