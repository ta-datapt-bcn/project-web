<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>


#   Project Ironhack Data Bootcamp

Javier Carrasco Morente

*Data Part Time Barcelona Dic 2019*


## Proyecto

Uso la API de chess.com para obtener informacion y partidas de los jugadores de ajedrez

## Workflow

En primer lugar miro los leaderboard.

Podemos ver que hay diferentes tipos de juego segun el tiempo que tenemos para realizar los movimientos:

- Daily 
    - Cada jugador tiene 24 horas para realizar cada uno de los movimientos.

- Rapid 
    - Cada jugador desde 10 minutos en adelante hasta 1 hora para realizar todos los movimientos.
    - Puede tener incrementos de segundos por cada movimiento.

- Blitz 
    - Cada jugador tiene entre 2 minutos y 10 para realizar todos sus movimientos.
    - Puede tener incrementos de segundos por cada movimiento.

- Bullet
    - Cada jugador tiene un minuto para realizar todos los movimientos.

Tambien hay diferentes tipos de juegos:

- 960
    - Son partidas de ajedrez con las piezas iniciales situadas de forma aleatoria. Es decir, los peones siguen en su posición inicial pero las piezas mayores están desordenadas.

- Kingofthehill
    - Gana el primer jugador que lleve su rey al centro del tablero.

- Bughouse
    - El formato bughouse o pasapiezas, se juega por parejas y se realiza de tal manera que las piezas que capture nuestro compañero a su rival, pasarán a estar disponibles para que las utilicemos. Es decir, si nosotros jugamos con blancas y nuestro compañero (que juega con negras) le captura un caballo a su rival, en nuestro turno tendremos un caballo blanco para utilizar o colocar donde queramos.

- Crazyhouse
    - Te permite utilizar las piezas del rival que capturas. Es decir, si jugamos con blancas capturamos un peón negro del rival, de repente tendremos un peón blanco que podremos incorporar en el tablero en nuestro turno. Para ser más concreto, la pieza capturada cambia de color y pasa a estar a nuestra disposición.

Obtengo el leaderboard de las partidas blitz.
    - Añado el pais y la localizacion de cada jugador.
    - Añado la mejor puntuacion, el numero de victorias, derrotas y empates de cada jugador.

De cada jugador obtengo todas las partidas que han disputado.
    - Me quedo con las partidas que son blitz y cuentan para la puntuacion de rating.
    - Limpio la notacion de cada partida.
Obtengo las diferentes aperturas que hay para despues añadirla.