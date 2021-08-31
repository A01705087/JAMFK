
# JAMFK

La educación es uno de los aspectos que avanzan a la mano de la tecnología disponible. Uno podría comparar los métodos de enseñanza de hace cien años con los de ahora. Los conceptos se simplifican mientras pasa el tiempo. En este proceso de simplificación es donde se crean ideas innovadoras para expandir el aprendizaje. Una de estas formas son las aplicaciones para practicar las matemáticas básicas. Analizando las aplicaciones del mercado, las más reconocidas se enfocan en la seriedad de la compresión, en vez de hacerlo divertido como si fuera un videojuego (una de las cosas que se fijan los niños, el mercado principal). Por eso, quiero crear un juego llamado JAMFK (Juego Amigable de Matemáticas For Kids) para practicar las sumas, y restas de una forma diferente a la vez entretenida para poner otra opción para la educación infantil. Este videojuego tendrá un banco de diez preguntas de cada tipo de operación, y un contador de vidas que se reduce cada que se contesta incorrectamente. Hasta incluso aparecería un mensaje de "Game Over" si se acaban las vidas, pero en el caso contrario de que se terminen de contestar las preguntas correctamente se pondrá un mensaje de celebración.

# Algoritmo

#Inicio del programa

1)print('Bienvenid@ a JMFK, un juego divertido para practicar matemáticas')

2)print('Escoge el tipo de operación')

3)Crear listasuma (Con las preguntas previamente establecidas)

4)Crear variable a con el valor de 0

5)Crear listaresta (Con las preguntas previamente establecidas)

6)Crear variable b con el valor de 1

8)Asignar a la variable modo_de_juego el valor de “suma”

9)Poner valor de tres a contador_de_vidas

10)Asignar valor de 0 a opcion

11)Asignar variable de resultado con 0

12)Asignar variable de respuesta con 0

13)Asignar a la variable acum el valor de 1

14)While opcion>2:

	a.pedir opcion mostrando los números para cada operación
	
#Funciones

15) def generar_pregunta(valor_1,valor_2):
    a.uno=str(valor_1)
    b.dos=str(valor_2)
    c.pregunta=uno,'+', dos
    d.return pregunta
    
16)def crear_respuesta(valor1, valor2):
    a.answer=valor1+valor2
    b.return answer

17)def generar_pregunta2(valor_1, valor_2):
    a.uno=str(valor_1)
    b.dos=str(valor_2)
    c.pregunta=uno,'-', dos
    d.return pregunta

18)def crear_respuesta2(valor1, valor2):
    answer= valor1-valor2
    return answer    
    
    
#Juego
    
    
19.If opcion==0:

      a. Imprimir mensaje de bienvenida de suma.
      
      b. While contador_de_vidas>0 and acum<=10:
      
            a.print('Pregunta', acum)
	    
	    b. print('¿Cuál es el resultado de', generar_pregunta(listasuma[a],listasuma[b]), '?')
	    
	    c. Al paso 15.
            
            d.Asignar a la variable resultado, la resolución de la pregunta con la funcion crear_respuesta(listasuma[a],lista suma[b])
	    
	    e. Ir al paso 16.
            
            c.Pedir respuesta y asignarlo a la variable respuesta
            
            d.If respuesta==resultado:
            
                       a.print("Tuviste la respuesta correcta.")
                                              
             e. else:
             
                       a.print("Tuviste la respuesta incorrecta.")
                       
                       b.Restar uno a la variable contador_de_vidas
            
	    f. sumar uno a acum.
	    
	    g. sumar uno a a
	    
	    h. sumar uno a b
	    
            i. Regresar al paso 19.b
    
                
19.b elif opcion== 1:

      a. Imprimir mensaje de bienvenida de resta.
      
      b. While contador_de_vidas>0 and acum<=10:
      
            a.print('Pregunta', acum)
	    
	    b. print('¿Cuál es el resultado de', generar_pregunta2(listaresta[a],listaresta[b]), '?')
	    
	    c. Al paso 17.
            
            d.Asignar a la variable resultado, la resolución de la pregunta con la funcion crear_respuesta2(listaresta[a],listaresta[b])
	    
	    e. Ir al paso 18.
            
            c.Pedir respuesta y asignarlo a la variable respuesta
            
            d.If respuesta== resultado:
            
                       a.print("Tuviste la respuesta correcta.")
                       
             e. else:
             
                       a.print( "Tuviste la respuesta incorrecta.")
                       
                       b.Restar uno a la variable contador_de_vidas
            
	    f. sumar uno a acum.
	    
	    g. sumar uno a a
	    
	    h. sumar uno a b
	    
            i. Regresar al paso 19.b.b
    
#Conclusión           
        
20) If contador_de_vidas>0:

       a.print("Felicidades, lograste contestar todas las diez preguntas de,” modo_de_juego, “.”)
      
       b.print( “Con:”, contador_de_vidas, “vidas.”)
      
       c.print(“Gracias por jugar JMFK. :)”)
      
     else:
   
   	a.print("Game Over!")
   
	b.print (“Lo siento.”)
      
	c.print(“Puedes tener major suerte para la próxima.”)
