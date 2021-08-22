
# JAMFK

La educación es uno de los aspectos que avanzan a la mano de la tecnología disponible. Uno podría comparar los métodos de enseñanza de hace cien años con los de ahora. Los conceptos se simplifican mientras pasa el tiempo. En este proceso de simplificación es donde se crean ideas innovadoras para expandir el aprendizaje. Una de estas formas son las aplicaciones para practicar las matemáticas básicas. Analizando las aplicaciones del mercado, las más reconocidas se enfocan en la seriedad de la compresión, en vez de hacerlo divertido como si fuera un videojuego (una de las cosas que se fijan los niños, el mercado principal). Por eso, quiero crear un juego llamado JAMFK (Juego Amigable de Matemáticas For Kids) para practicar las sumas, y restas de una forma diferente a la vez entretenida para poner otra opción para la educación infantil. Este videojuego tendrá un banco de diez preguntas de cada tipo de operación, y un contador de vidas que se reduce cada que se contesta incorrectamente. Hasta incluso aparecería un mensaje de "Game Over" si se acaban las vidas, pero en el caso contrario de que se terminen de contestar las preguntas correctamente se pondrá un mensaje de celebración.

Algoritmo

1)Imprimir mensaje de saludo

2)Imprimir opciones de estudio (suma, resta)

3)Crear listasuma (Con las preguntas previamente establecidas)

4)Crear variable a con el valor de 0

5)Crear listaresta (Con las preguntas previamente establecidas)

6)Crear variable b con el valor de 1

7)crear variable c con el valor de 2

8)Asignar a la variable modo_de_juego el valor de “suma”

9)Poner valor de tres a Contador_de_vidas

10)Asignar valor de 0 a opcion

11)Asignar variable de resultado con 0

12)Asignar variable de respuesta con 0

13)Mientras opcion sea menor a 2:

	a.pedir opcion mostrando los números para cada operación
      
b.Si opcion es igual a 0:

      a. Imprimir mensaje de bienvenida de suma.
      
      b. Mientras contador_de_vidas sea mayor a cero:
      
            a.Imprimir operación con elementos de listasuma
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 15.b.b
                       
             e. otro:
             
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                        c. Regresar al paso 15.b.b
                        
        otro:
        
                a.Imprimir mensaje "Game Over"
                
15.b.1 else si opcion es igual a 1:

      a. Imprimir mensaje de bienvenida de resta.
      
      b. Mientras contador sea mayor a cero:
      
            a.Imprimir elemento de listaresta
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 15.b.1.b
                       
             e. otro:
             
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                        c. Regresar al paso 15.b.1.b
                        
        otro:
        
                a.Imprimir mensaje "Game Over"
                

 else:
 
               a. Imprimir mensaje "Esa no es una opción válida."
        
14) Si contador_de_vidas>0:

      Imprimir mensaje "Felicidades, lograste contestar todas las diez preguntas de,” modo_de_juego, “.”
      
      Imprimir mensaje “Con:”, contador_de_vidas, “vidas.”
      
      Imprimir mensaje “Gracias por jugar JMFK. :)”
      
   else:
   
	Imprimir mensaje “Lo siento.”
      
	Imprimir mensaje “Puedes tener major suerte para la próxima.”
