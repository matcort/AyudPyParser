# -*- coding: utf-8 -*-
import sys
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
########################################################################################################################
#
#         _nnnn_                      	      Ayudantia Fundamentos de Programacion.
#        dGGGGMMb     ,"""""""""""""".		Matias Cortes G. 
#       @p~qp~~qMb    | Linux Rules! |		Año: 2016.
#       M|@||@) M|   _;	Abre tu mente|	
#       @,----.JM| -'  \____________/		Realizar: 	-Completar funcion Bisturi, saca tags html
#      JS^\__/  qKL						-Hacer estadistica por palabra, cuantas veces se repite 
#     dZP        qKRb			     				cada palabra.
#    dZP          qKKb						
#   fZP            SMMb						
#   HZM            MMMM		
#   FqM            MMMM
# __| ".        |\dS"qML			
# |    `.       | `' \Zq			
#_)      \.___.,|     .'			
#\____   )MMMMMM|   .'			
#     `-'       `--' hjm
########################################################################################################################


def get(url):
	req = requests.get(url)
	statusCode = req.status_code
	htmlText = req.text
	return htmlText#, statusCode

def archivo(htmlText, nomarchivo):
	archivo = open(nomarchivo, "w")
#	contenido = archivo.read()
#	final_de_archivo = archivo.tell()
	#lista = ['Linea 1\n', 'Linea 2']
	 
	archivo.write(htmlText)
	archivo.close
	return nomarchivo
	#archivo.seek(final_de_archivo)

	
def bisturi(archivo): #Funcion por completar



	
	
		
		
	



# print str(sys.argv) #imprime el arreglo entero que contiene las entradas al programa
# print sys.argv[0] #imprime el primer argumento
# print sys.argv[1] #imprime el segundo argumento
# print len(sys.argv) # imprime la cantidad de argumentos

url = str(sys.argv[1])

bisturi(archivo(get(url), "nomarchivo"))


