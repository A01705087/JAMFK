
#Inicio de programa

print('Bienvenid@ a JMFK, un juego divertido para practicar matemáticas')
print('Escoge el tipo de operación')
print('Suma,\nResta')
print('Para suma escoja 0, \ny para resta 1')

#Asignar variantes y creación de bancos de preguntas

opcion=int(input('Escoja su número por favor'))
contador_de_vidas=3

modo_de_juego="suma"

a=0
b=1
c=2

if opcion==0:
    modo_de_juego="suma"
elif opcion==1:
    modo_de_juego="resta"

resultado=0

respuesta=0

#Inicio del juego y juego

if opcion==0:
    print('Bienvenid@ a la suma')
    print('Ahora contestará diez preguntas')
    print('Recuerde que tiene tres vidas')
    respuesta=int(input('¿Cuál es el resultado de 2+2 ?'))
    resultado= c+2*b
    if respuesta == resultado:
        print('Tienes la respuesta correcta')
    else:
        print('Tuviste la respuesta incorrecta')
        contador_de_vidas= contador_de_vidas-1

elif opcion==1:
    print('Bienvenid@ a la resta')
    print('Ahora contestarás diez preguntas')
    print('Recuerda que tienes tres vidas')
    respuesta=int(input('¿Cuál es el resultado de 2-2 ?'))
    resultado= c-2*b
    if respuesta == resultado:
        print('Tienes la respuesta correcta')
    else:
        print('Tuviste la respuesta incorrecta')
        contador_de_vidas= contador_de_vidas-1
else:
    print('Esa no es una opción válida')


#Conclusión

if contador_de_vidas>0:
    print('¡Felicidades! Haz logrado contestar las diez preguntas de', modo_de_juego,'.')
    print('Con:', contador_de_vidas, 'vidas.')
    print('Gracias por jugar JMFK. :)')
else:
    print('Lo siento.')
    print('Puedes tener mejor suerte para la próxima.')