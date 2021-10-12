
# JAMFK

La educación es uno de los aspectos que avanzan a la mano de la tecnología disponible. Uno podría comparar los métodos de enseñanza de hace cien años con los de ahora. Los conceptos se simplifican mientras pasa el tiempo. En este proceso de simplificación es donde se crean ideas innovadoras para expandir el aprendizaje. Una de estas formas son las aplicaciones para practicar las matemáticas básicas. Analizando las aplicaciones del mercado, las más reconocidas se enfocan en la seriedad de la compresión, en vez de hacerlo divertido como si fuera un videojuego (una de las cosas que se fijan los niños, el mercado principal). Por eso, quiero crear un juego llamado JAMFK (Juego Amigable de Matemáticas For Kids) para practicar las sumas, y restas de una forma diferente a la vez entretenida para poner otra opción para la educación infantil, sumándome a la tendencia de aplicaciones como Matific o Smartick (El Mundo, s.f). Este videojuego tendrá un banco de diez preguntas de cada tipo de operación, y un contador de vidas que se reduce cada que se contesta incorrectamente. Hasta incluso aparecería un mensaje de "Game Over" si se acaban las vidas, pero en el caso contrario de que se terminen de contestar las preguntas correctamente se pondrá un mensaje de celebración.

# Algoritmo

#Funciones

1) def generar_pregunta(valor_1,valor_2):
    a.uno=str(valor_1)
    b.dos=str(valor_2)
    c.pregunta=uno,'+', dos
    d.return pregunta
    
2)def crear_respuesta(valor1, valor2):
    a.answer= valor absoluto de valor1 + valor absoluto de valor2
    b.return answer

3)def generar_pregunta2(valor_1, valor_2):
    a.uno=str(valor_1)
    b.dos=str(valor_2)
    c.pregunta= uno,'-',dos
    d.return pregunta

4)def crear_respuesta2(valor1, valor2):
    answer= valor absoluto de valor1 - valor absoluto de valor2
    return answer    

#Inicio del programa

5)print('Bienvenid@ a JMFK, un juego divertido para practicar matemáticas')

6)print('Escoge el tipo de operación')

7)Crear listasuma (Con las preguntas previamente establecidas)

8)Crear variable a con el valor de 0

9)Crear listaresta (Con las preguntas previamente establecidas)

10)Crear variable b con el valor de 1

11)Asignar a la variable modo_de_juego el valor de “suma”

12)Poner valor de tres a contador_de_vidas

13)Asignar valor de 0 a opcion

14)Asignar variable de resultado con 0

15)Asignar variable de respuesta con 0

16)Asignar a la variable acum el valor de 1

17)While opcion>=2:

	a.pedir opcion mostrando los números para cada operación
    
    
#Juego
    
    
18.If opcion==0:

      a. Imprimir mensaje de bienvenida de suma.
      
      b. While contador_de_vidas>0 and acum<=10:
      
            a.print('Pregunta', acum)
	    
	    b. print('¿Cuál es el resultado de', generar_pregunta(listasuma[a],listasuma[b]), '?')
	    
	    c. Al paso 1.
            
            d.Asignar a la variable resultado, la resolución de la pregunta con la funcion crear_respuesta(listasuma[a],lista suma[b])
	    
	    e. Ir al paso 2.
            
            c.Pedir respuesta y asignarlo a la variable respuesta
            
            d.If respuesta==resultado:
            
                       a.print("Tuviste la respuesta correcta.")
                                              
             e. else:
             
                       a.print("Tuviste la respuesta incorrecta.")
                       
                       b.Restar uno a la variable contador_de_vidas
            
	    f. sumar uno a acum.
	    
	    g. sumar uno a a
	    
	    h. sumar dos a b
	    
            i. Regresar al paso 18.b
    
                
18.b elif opcion== 1:

      a. Imprimir mensaje de bienvenida de resta.
      
      b. While contador_de_vidas>0 and acum<=10:
      
            a.print('Pregunta', acum)
	    
	    b. print('¿Cuál es el resultado de', generar_pregunta2(listaresta[a],listaresta[b]), '?')
	    
	    c. Al paso 3.
            
            d.Asignar a la variable resultado, la resolución de la pregunta con la funcion crear_respuesta2(listaresta[a],listaresta[b])
	    
	    e. Ir al paso 4.
            
            c.Pedir respuesta y asignarlo a la variable respuesta
            
            d.If respuesta== resultado:
            
                       a.print("Tuviste la respuesta correcta.")
                       
             e. else:
             
                       a.print( "Tuviste la respuesta incorrecta.")
                       
                       b.Restar uno a la variable contador_de_vidas
            
	    f. sumar uno a acum.
	    
	    g. sumar uno a a
	    
	    h. sumar dos a b
	    
            i. Regresar al paso 18.b.b
    
#Conclusión           
        
20) If contador_de_vidas>0:

       a.print("Felicidades, lograste contestar todas las diez preguntas de,” modo_de_juego, “.”)
      
       b.print( “Con:”, contador_de_vidas, “vidas.”)

       c.print(“Gracias por jugar JMFK. :)”)
      
     else:
   
   	a.print("Game Over!")
   
	b.print (“Lo siento.”)
      
	c.print(“Puedes tener major suerte para la próxima.”)
	
Referencias:

El Mundo. (s.f.). Apps y consejos para que tus hijos aprendan matemáticas y además se diviertan. Recuperado de:	
    https://saposyprincesas.elmundo.es/ocio-en-casa/apps-videojuegos/apps-hijos-aprendan-matematicas/

Referencias de funciones dentro del programa:

Python Software Foundation.(2021). Built-in Functions. Recuperado de:
	https://docs.python.org/3.10/library/functions.html#abs 

Python Software Foundation.(2021). Built-in Types. Recuperado de:
	https://docs.python.org/3.10/library/stdtypes.html#text-sequence-type-str
