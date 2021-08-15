
# JAMFK

La educación es uno de los aspectos que avanzan a la mano de la tecnología disponible. Uno podría comparar los métodos de enseñanza de hacer cien años con los de ahora. Los conceptos se simplifican mientras pasa el tiempo. En este proceso de simplificación es donde se crean ideas innovadoras para expandir el aprendizaje. Una de estas formas son las aplicaciones para practicar las matemáticas básicas. Analizando las aplicaciones del mercado, las más reconocidas se enfocan en la seriedad de la compresión, en vez de hacerlo divertido como si fuera un videojuego (una de las cosas que se fijan los niños, el mercado principal). Por eso, quiero crear un juego llamado JAMFK (Juego Amigable de Matemáticas For Kids) para practicar las sumas, restas, multiplicaciones, y divisiones de una forma diferente a la vez entretenida para poner otra opción para la educación infantil. Este videojuego tendrá un banco de diez preguntas de cada tipo de operación, y un contador de vidas que se reduce cada que se contesta incorrectamente. Hasta incluso aparecería un mensaje de "Game Over" si se acaban las vidas, pero en el caso contrario de que se terminen de contestar las preguntas correctamente se pondrá un mensaje de celebración.

Algoritmo

1)Imprimir mensaje de saludo

2)Imprimir opciones de estudio (suma, resta, multiplicar, dividir)

3)Crear listasuma (Con las preguntas previamente establecidas)

4)Asignar a la variable choice1, el valor de suma

5)Crear listaresta (Con las preguntas previamente establecidas)

6)Asignar a la variable choice2, el valor de resta

7)Crear listamultiplicar (Con las preguntas previamente establecidas)

8)Asignar a la variable choice3, el valor de multiplicar

9)Crear listadividir (Con las preguntas previamente establecidas)

10)Asignar a la variable choice4, el valor de dividir

11)Poner valor de tres a contador

11)Pedir opcion con el mensaje "Escribe tu opción"

13)Si opcion es igual a choice1:

      a. Imprimir mensaje de bienvenida de suma.
      
      b. Mientras contador sea mayor a cero:
      
            a.Imprimir elemento de listasuma
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 13.b
                       
             e. otro:
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                       c. Regresar al paso 13.b
        otro:
                a.Imprimir mensaje "Game Over"
                
                b.Imprimir mensaje "Puedes tener mejor suerte para la próxima."
                
                c.Fin del programa.
                
13.1 else si opcion es igual a choice2:

      a. Imprimir mensaje de bienvenida de resta.
      
      b. Mientras contador sea mayor a cero:
      
            a.Imprimir elemento de listaresta
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 13.b
                       
             e. otro:
             
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                       c. Regresar al paso 13.1.b
                        
        otro:
        
                a.Imprimir mensaje "Game Over"
                
                b.Imprimir mensaje "Puedes tener mejor suerte para la próxima."
                
                c.Fin del programa.
                
13.2 else Si opcion es igual a choice3:

      a. Imprimir mensaje de bienvenida de multiplicar.
      
      b. Mientras contador sea mayor a cero:
      
            a.Imprimir elemento de listamultiplicar
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 13.2.b
                       
             e. otro:
             
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                       c. Regresar al paso 13.2.b
                       
        otro:
        
                a.Imprimir mensaje "Game Over"
                
                b.Imprimir mensaje "Puedes tener mejor suerte para la próxima."
                
                c.Fin del programa.
                
13.3 else si opcion es igual a choice4:

      a. Imprimir mensaje de bienvenida de dividir.
      
      b. Mientras contador sea mayor a cero:
      
            a.Imprimir elemento de listadividir
            
            b.Asignar a la variable resultado, la resolución de la pregunta
            
            c.Pedir respuesta
            
            d.Si respuesta es igual a resultado:
            
                       a.Imprimir "Tuviste la respuesta correcta."
                       
                       b. Regresar al paso 13.3.b
                       
             e. otro:
             
                       a.Imprimir "Tuviste la respuesta incorrecta."
                       
                       b.Restar uno a la variable contador.
                       
                       c. Regresar al paso 13.3.b
                       
        otro:
        
                a.Imprimir mensaje "Game Over"
                
                b.Imprimir mensaje "Puedes tener mejor suerte para la próxima".
                
                c.Fin del programa.
                
13.4 else:

               a. Imprimir mensaje "Esa no es una opción válida."
               
               b. Fin del programa.
               
14) Imprimir mensaje "Felicidades, lograste contestar todas las preguntas con", contador "de vidas." 

