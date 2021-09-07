
#Funciones del juego

def generar_pregunta(valor_1, valor_2):
    uno=str(valor_1)
    dos=str(valor_2)
    pregunta=uno,'+', dos
    return pregunta

def crear_respuesta(valor1, valor2):
    answer=valor1 + valor2
    return answer

def generar_pregunta2(valor_1, valor_2):
    uno=str(valor_1)
    dos=str(valor_2)
    pregunta=uno,'-', dos
    return pregunta

def crear_respuesta2(valor1, valor2):
    answer= valor1 - valor2
    return answer

#Inicio del programa

print('Bienvenid@ a JMFK, un juego divertido para practicar matemáticas')
print('Escoge el tipo de operación')
print('Suma,\nResta')
print('Para suma escoja 0, \ny para resta 1')

#Asignar variantes, constantes y creación de bancos de preguntas

contador_de_vidas=3

modo_de_juego="suma"

a=0
b=1

acum=1

resultado=0

respuesta=0

# Elección

opcion=int(input('Escoja su número por favor'))

if opcion>2:
    print('No ha escogido una opción válida')
    opcion = int(input('Por favor hágalo de nuevo, \n Suma es 0, \n y resta 1'))
else:
    print('Muy bien. Comencemos el juego.')

if opcion==0:
    modo_de_juego="suma"
elif opcion==1:
    modo_de_juego="resta"

# Juego

if opcion==0:
    print('Bienvenid@ a la suma')
    print('Ahora contestará diez preguntas')
    print('Recuerde que tiene tres vidas')
    print('Pregunta',acum)
    print('¿Cuál es el resultado de', generar_pregunta(53,3), '?')
    print('Ponga su respuesta')
    resultado= crear_respuesta(53, 3)
    respuesta=int(input())
    if respuesta == resultado:
        print('Tienes la respuesta correcta')
    else:
        print('Tuviste la respuesta incorrecta')
        contador_de_vidas= contador_de_vidas - 1
    acum= acum + 1
    a= a + 1
    b= b + 1

elif opcion==1:
    print('Bienvenid@ a la resta')
    print('Ahora contestarás diez preguntas')
    print('Recuerda que tienes tres vidas')
    print('Pregunta',acum)
    print('¿Cuál es el resultado de', generar_pregunta2(100,25), '?')
    print('Ponga su respuesta')
    resultado= crear_respuesta2(100, 25)
    respuesta=int(input())
    if respuesta == resultado:
        print('Tienes la respuesta correcta')
    else:
        print('Tuviste la respuesta incorrecta')
        contador_de_vidas= contador_de_vidas - 1
    acum= acum + 1
    a= a + 1
    b= b + 1


#Conclusión

if contador_de_vidas>0:
    print('¡Felicidades! Haz logrado contestar las diez preguntas de', modo_de_juego,'.')
    print('Con:', contador_de_vidas, 'vidas.')
    print('Gracias por jugar JMFK. :)')
else:
    print('Game Over!')
    print('Lo siento.')
    print('Puedes tener mejor suerte para la próxima.')