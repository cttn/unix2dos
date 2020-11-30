# -*- coding: latin1 -*-
"""
Created on Wen Dec 4 11:40:28 2019

@author: Cttn
"""

import argparse

def cgw_parser():
    parser = argparse.ArgumentParser(description='Convierte formato unix a dos y viceversa',
                                     epilog="-- unix2dos (por CJC)--")
    parser = argparse.ArgumentParser(prog='unix2dos')
    parser.add_argument('-a', '--archivo', metavar="ARCHIVO", default='', help='Path del archivo de configuración deseado.')
    parser.add_argument('-e', '--ext', metavar="Extension", default='', help='No sobrescribir archivo: se genera uno nuevo con la extensión dada.')
    parser.add_argument('-i', action='store_true', help='Invertir conversion (dos2unix).')
    args = parser.parse_args()
    return args
    
    
if __name__ == "__main__":

    parsed = cgw_parser()
    arch = parsed.archivo
    extra = parsed.ext
    invertir = parsed.i
    
    print("\n ######### UNIX2DOS (por CJC) #########")
    
    if arch=='':
        raise SystemExit(" ERROR: No se seleccionó archivo a converitr")

    try:
        with open(arch, "r") as f:
            texto = f.read()

        if invertir:
            print(" Convirtiendo "+ str(arch)+ " a formato UNIX.")
            with open(arch+extra, "w",newline='\n') as f:
                texto = f.write(texto)    
        else:
            print(" Convirtiendo "+ str(arch)+ " a formato DOS.")
            with open(arch+extra, "w",newline='\r\n') as f:
                texto = f.write(texto)
    except UnicodeDecodeError:
        print("Error de decodificación UNICODE.")
    except:
    	  print("Error al procesar el archivo.")
