![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# CLASH ROYALE - Project Web - FINDING THE BEST DECK

Jose Angel Casado
Data Analytics Part Time Dic 2019

## Introducción

Mi proyecto está basado e inspirado en el juego para smartphones y tablets CLASH ROYALE. Un juego de la conocida empresa de desarrollo de juegos SUPERCELL.

Por explicarlo simple y rápido en que consiste este videojuego, combina elementos de los juegos de cartas coleccionables, defender la torre y estrategia de acción en tiempo real y tu objetivo para ganar, es tumbar las 3 torres que tiene el rival (y defender las propias) con un mazo de 8 CARTAS a elegir de las 97 totales que existen en el juego.

Pasado el tiempo estipulado de batalla, si ninguno de los dos ha conseguido tirar ninguna torre o la partida acaba en empate, gana la persona que más daño acumulado ha hecho al rival.

---

## Desarrollo

La meta a alcanzar que me he propuesto es, de la parte de WEB SCRAPING, extraer las 8 mejores cartas por %WIN RATE, es decir, las 8 cartas que, incluidas en la inmensidad de mazos que se pueden crear, (2352332 combinaciones) tienen más probabilidad de darnos una victoria y compararlas con las 8 mejores cartas por POPULATION o POPULARIDAD, es decir, las 8 cartas más usadas realmente en la actualidad, por "moda".
(Usaré la web https://statsroyale.com)

Acto seguido después de la comparación, coger las 4 cartas con mejor balance %WIN RATE/POPULATION y crear un mazo competitivo con las 4 cartas restantes que mejor resultado den combinadas con las 4 que hemos obtenido después del estudio.
(Usaremos la web https://deckbandit.com/)

Una vez tengamos el mazo de 8 cartas, introducir el mazo dentro de la API y extraer la información del mismo:
-Cantidad de veces usado ese mazo en el juego.
-Victorias netas (derrotando las 3 torres)
-Victorias (mínimo una torre destruida, es decir, 1-0, 2-1)
-Empates
-Derrotas
(Usaremos la API RoyaleAPI)



## Resultados esperados

Juntando ambas informaciones de la WEB y de la API veremos que tan bueno es el mazo creado y si valdria para competir a alto nivel.

## Obstáculos encontrados

- Al hacer el Web Scraping quedaban muchos espacios entre carácteres que no he sabido limpiar con scraping. Al crear el DataFrame ya los he podido eliminar.
- Surge un problema en la web de statsroyale.com que en momentos del día, todos los parámetros de las cartas, como el winrate o el %uso se ponen a 0. Y depende de cuando se ejecute el programa, puede dar valores nulos.
- El merge final para unir datos de web con datos de API no he conseguido sacarlo.

## Lecciones aprendidas

Pese a que mi nivel de Web Scraping y conocimiento de APIS es muy mejorable, siento que gracias a este proyecto he podido mejorar mis habilidades.
Además al ser un proyecto más creativo y de búsqueda ha sido entretenido y me ha animado a buscar mucha información por mi cuenta y aprendiendo más.

