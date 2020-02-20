![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

El juego de Pokemon Go se diferencia cada vez más de los juegos de consola, con tipos distintos de pokemones que se pueden encontrar y con distintas features. Por eso necesitamos obtener estadísticas más precisas para poder tener mejor información sobre los mejores counters y ataques posibles.

Para esto extraeremos la siguiente información de dos fuentes: 

1.   De la distinta información de la api https://pokemon-go1.p.rapidapi.com
    - Nro de pokemon y nombre
    - Si el pokemon ha sido liberado en el juego
    - Tipo de pokemon: Un pokemon puede ser de varios tipos, por ejemplo charmander es un dragon de tipo fuego y su evolución charizard es de dos tipos, fuego y volador.
    - Forma de pokemon: Un pokemon puede ser de varios tipos por ejemplo castform es un pokemon que va cambiando de apariencia de acuerdo al clima que se encuentra. Existen pokemones que pueden ser de un tipo y tener ataques y/o forma de otro, por lo que hay que separar la forma del tipo
    - HP (vital points): Puntos de vida que tiene un pokemon
    - Attack: Capacidad de ataque
    - Defensa: Capacidad de defensa
    - MAX HP: La máxima cantidad de HP que puede tener de un pokemon al máximo nivel
    
    (damage that can be inflicted) and deffense in the case of attack. We get those values
    We find the data needs to be cleaned up a little bit to relex the game standard: Mewtwo Armored pokemon it's set to Mewtwo A. There's a lot of nulls that are set to be Normal pokemon form.We hot encode this variable to be more readable.

2. De la web https://pokemondb.net/go/pokedex que contiene la información complementaria a la API
    - % de captura de un pokemon, existen pokemones más difíciles de atrapar que otros
    - % de que el pokemon escape
    - Movimientos rápidos
    - Movimientos cargados
    - Link de la imagen del pokemon
    
La información de la API y la de la web están en un formato un poco distinto por lo que se han realizado algunas tareas de limpieza para que sean iguales y puedan mezclarse correctamente. Además para el dataset final se han descartado las formas Fall_2019, Shadow y Purified ya que tienen los mismos tipos y counters que el tipo normal.

Lo más complicado del ejercicio fue limpiar las formas de pokemon por ser un texto libre, y al ser parte de la llave primaria necesitaba estar perfecto para el match, pero era necesaria para reflejar de forma mas veraz la información del juego.
