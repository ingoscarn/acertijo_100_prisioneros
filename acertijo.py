import random
import time
#Creamos los papelitos con los numeros
lista_papeles = list(range(1,101))

#Los ordenamos de forma aleatoria
random.shuffle(lista_papeles)

#Metemos los papelitos en las cajas
cajas = {}
for caja in range(0,100):
   cajas[caja+1]=lista_papeles[caja]


#Creamos a los prisioneros
lista_prisioneros = list(range(1,101))

#Ordenamos a los prisioneros de forma aleatoria
random.shuffle(lista_prisioneros)

#contamos los intentos
contador_intentos = 1
#contamos los prisioneros inicia de 0 para ser un arreglo
contador_prisioneros = 0
#una lista para guardar a los que se salvan
prisioneros_salvados = []

#Que numero tiene el primer pisionero en entar
print("El primer prisionero tiene el numero: {}".format(lista_prisioneros[contador_prisioneros]))
#Obtenemos el valor de la caja que tenga el numero de prisionero:
print("Entonces abrimos la caja con el numero: {}".format(lista_prisioneros[contador_prisioneros]))
valor_papel_caja = cajas[lista_prisioneros[contador_prisioneros]]

#Obtenemos el valor del papelito
print("La caja numero: {} contiene el papel con numero: {} ".format(lista_prisioneros[contador_prisioneros],valor_papel_caja))

while True:
    if contador_intentos <= 50:
        numero_prisionero = lista_prisioneros[contador_prisioneros]
        print("==| Prisionero numero: {} Intento: {}  |==".format(numero_prisionero,contador_intentos))
        print("El prisionero tiene el numero: {} y el papel tiene impreso el numero: {}".format(numero_prisionero,valor_papel_caja))
        #Si mi papel y mi numero son iguales pum!! me salvo
        if numero_prisionero == valor_papel_caja:
            print("Los numeros coinciden, siguiente prisionero!")
            contador_prisioneros += 1
            contador_intentos = 0
            valor_papel_caja = cajas[lista_prisioneros[contador_prisioneros]]
            print("Valor del nuevo papel en la caja: {}".format(valor_papel_caja))
            prisioneros_salvados.append(numero_prisionero)
        #No me salve aun pero voy abriri la caja que tenga el numero del papel que saque
        else:
            print("Los numeros NO coinciden, abriendo nueva caja: {}".format(valor_papel_caja))
            nuevo_valor_papel_caja = cajas[valor_papel_caja]
            print("--La nueva caja tiene el papel: {}".format(nuevo_valor_papel_caja))
            valor_papel_caja = nuevo_valor_papel_caja
        contador_intentos += 1
        print("------->Prisioneros salvados: {} ".format(len(prisioneros_salvados)))
        #Ya pasaron todos los prisioneros del 0 1l 99 y se salvaron!!
        if contador_prisioneros == 99:
            print("SE SALVARON TODOS")
            prisioneros_salvados.sort()
            print(prisioneros_salvados)
            break
    else:
        print("Estan todos bien muertos!!")
        break
    time.sleep(1)
