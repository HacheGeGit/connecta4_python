# connecta4_python

El juego funciona por consola, sin interfaz gráfica. El funcionamiento es sencillo, las fichas se colocan "dejándolas caer" en la última casilla libre del tablero por medio de un diccionario que guarda las coordenadas de cada una de las columnas y su última fila. Cuando dejamos caer una ficha, la fila de la coordenada en el diccionario de jugadas se modifica para que la siguiente ficha caiga encima de la ficha que hemos colocado antes. 

Cada jugador dispone de una ficha de un color distinto. El tablero se actualiza jugada a jugada borrando y pintando el nuevo tablero turno a turno. El juego permite empezar una nueva partida o para de jugar cuando terminas una partida. 

#Comprobación de quién ha ganado:

Se realiza la comprobación a partir de la cuarta ficha que se ponga en el tablero. La comprobación se realiza mediante bucles y contadores. En el caso de las comprobaciones, tanto horizontales como verticales, se comprueba línea a línea y columna a columna. En el caso de que encuentre una ficha, el contador sumará más 1, y en caso contrario, el contador se igualará a 0.

En el caso de las diagonales el funcionamiento es distinto. En vez de recorrer el tablero, se recorre un diccionario que guarda las posibles 9 diagonales, si estas coinciden con la ficha, se retornará True acabando así la partida. Para las diagonales negativas se recorren el diccionario invirtiendo los índices para obtener las columnas negativas.

Este ejercicio se realizó como parte de un examen de la asignatura Sistemas de gestión empresarial de 2º de DAM en la que se estudia Python para el desarrollo en el ORM Odoo.
