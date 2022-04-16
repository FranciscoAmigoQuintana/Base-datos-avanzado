
from cProfile import run
import collections
from pickle import FALSE, TRUE
import subprocess
from time import sleep
from unittest import result

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

## Variable que hace alucion a la base de datos y el cliente de localhost
db = client.db_lab1

## Variable que guarda el nombre de la collecion
cliente = db.cliente

vida=TRUE

while vida==TRUE:

    print ("Bienvenido al menu de clientes")
    print ("  ")
    print ("Ingrese el 1 para insertar un cliente")
    print ("Ingrese el 2 para buscar un cliente")
    print ("Ingrese el 3 para eliminar un cliente")
    print ("Ingrese el 4 para editar un cliente")
    print ("Ingrese el 5 para salir de la aplicacion")
    print (" ")
    selector = input()

    ## Ingresa clientes
    if selector=="1":
        nombre = input("Ingrese el nombre del cliente\n")
        contenido = input("Ingrese el contenido\n")
        
        post_data = {
            'nombre': nombre,
            'contenido': contenido
        }
        result = cliente.insert_one(post_data)

    ## Muestra los clientes de la base de datos
    elif selector=="2":
        nombrebuscar = input("Ingrese el nombre del cliente\n")
        buscar_cliente = cliente.find({'nombre': nombrebuscar})
        print (" ")

        for x in buscar_cliente:
            print (x)

        print (" ")
        pasar = input("Aprete intro para continuar")
    
    ## Elimina clientes
    elif selector=="3":
        print (" ")
        cebador3=input("Ingrese 1 para eliminar un registro o Ingrese 2 para eliminar todos los registros\n")
        print (" ")

        if cebador3=="1":
            nombreeliminar = input("Ingrese el nombre del cliente a eliminar (eliminara la primera entrada de informacion)\n")

            ## Elimina solo un cliente
            eliminar_cliente = cliente.delete_one({'nombre': nombreeliminar})
            print (" ")
            print ("se realizo la accion")
            print (" ")
        
        elif cebador3=="2":
            nombreeliminar = input("Ingrese el nombre del cliente a eliminar (eliminara la informacion del todos los cliente ingresada)\n")

            ## Elimina solo un cliente
            eliminar_cliente = cliente.delete_many({'nombre': nombreeliminar})
            print (" ")
            print ("se realizo la accion")
            print (" ")
        
    ## Actualizar un cliente o todos los clientes
    elif selector=="4":
        print (" ")
        cebador2=input("Ingrese 1 para actualizar un registro o Ingrese 2 para actualizar todos los registros\n")
        print ("")

        if cebador2=="1":    
            nombreactualizar = input("Ingrese el nombre del cliente a actualizar su informacion\n")
            print (" ")
            contenidonuevo = input("Ingrese el nuevo contenido\n")
            print (" ")

            actualizar_cliente = cliente.update_one({'nombre': nombreactualizar},{"$set": {"contenido":contenidonuevo}})
            print (" ")
            print ("actualizacion realizada")
            print (" ")

        elif cebador2=="2":
            nombreactualizar = input("Ingrese el nombre del cliente a actualizar su informacion\n")
            print (" ")
            contenidonuevo = input("Ingrese el nuevo contenido\n")
            print (" ")

            actualizar_cliente = cliente.update_many({'nombre': nombreactualizar},{"$set": {"contenido":contenidonuevo}})
            print (" ")
            print ("actualizacion realizada")
            print (" ")

        else:
            print (" ")
            print ("Ingrese un valor valido")
            print (" ")

    ## Salir del programa
    elif selector=="5":
        quit()
    else:
        print ("Numero incorrecto")

    sleep(2)
    subprocess.run(["clear"])



