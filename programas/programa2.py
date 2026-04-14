# -*- coding: utf-8 -*-
import re
import sys
import programa1
import datetime
def programa2(RutaFactura):
    
    #Aca queremos encontrar las TARGETWORDS que vienen despues de ciertas KEYWORDS.
    #En nuestro caso queremos la fecha que viene despues "FECHA:" y el monto que viene despues de "BANCARIO"
    
    fecha = ""
    monto = ""
    #Primero seteamos el texto que vamos a buscar nuestras TARGETWORD como el texto devuelto por el programa1 utilizando la RutaFactura

    texto = programa1.programa1(RutaFactura)


    #Segundo hacemos la busqueda de nuesstra TARGETWORD en el texto 
    #m_fecha y m_monto simboliza el MATCH de fecha y monto 

    #SYNTAX: r"" signifca la expression regular que estamos buscando
    #"FECHA:" y "BANCARIO" son las KEYWORD que sabemos que nuestra TARGETWORD viene despues
    # \s significa que despues de nuestra KEYWORKD habra un espacio y el "+" signifca que puede haber mas de un espacio
    #(\w) indica que va a guardar el CARACTER despues de la keyword, el "+" indica que va a guardar toda la string y va a parar la busqueda quando encuentre un blankspace


    m_fecha = re.search(r"FECHA:\s+([^\s]+)", texto)
    if m_fecha: #este if chekea que m_fecha no es NULL 
        fecha = m_fecha.group(1)
    
    #aca el syntax significa que despues de la palabra BANCARIO hay una cantidad mayor que 1 de espacios (\s signifca espacio) (\s+ significa 1 o mas espacios)
    #despues de eso el primer agrupamiento (\d+) significa que hay 1 o mas digitos que perteneceran al grupo, luego una cantidad de 0 o mas espacios (\s*) una coma (,) mas espacios y finalmente el grupo final (\d+)

    m_monto = re.search(r"BANCARIO\s+(\d+)\s*,\s*(\d+)", texto)
    if m_monto:
        monto_mil = m_monto.group(1)
        monto_cent = m_monto.group(2)

    monto = f"{monto_mil},{monto_cent}"

    #Arreglar fomato de fecha

    #la syntax aca es que \d{x} asigna x digitos al agrupamiento, osea:
    #(\d{2}) los parentesis significan 1 agrupamiento, el \d significa digitos y el {2} siginifica que la cantidad de digitos en el agrupamiento es 2
    # el [-/] es un OR, signifca que entre los agrupamientos estan - o /

    m_fecha = re.search(r"(\d{2})[-/](\d{2})[-/](\d{4})", fecha)

    if m_fecha:
        dia = m_fecha.group(1)
        mes = m_fecha.group(2)
        anio = m_fecha.group(3)
    
    fecha = ""
    fecha = f"{anio}-{mes}-{dia}"

 


    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
