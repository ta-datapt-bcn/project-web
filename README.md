{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"https://bit.ly/2VnXWr2\" alt=\"Ironhack Logo\" width=\"100\" align=\"right\"/>\n",
    "\n",
    "\n",
    "#   Project Ironhack Data Bootcamp\n",
    "\n",
    "Oscar M. Montero\n",
    "\n",
    "*Data Part Time Barcelona Dic 2019*\n",
    "\n",
    "\n",
    "## Content\n",
    "\n",
    "- [Project Description](#project)\n",
    "- [Workflow](#workflow)\n",
    "- [Results](#results)\n",
    "\n",
    "<a name=\"project\"></a>\n",
    "\n",
    "## Project Description\n",
    "\n",
    "En este proyecto buscamos aplicar los conocimientos obtenidos de Web Scraping y Obtención y tratamiento de APIs.\n",
    "La temática elegida ha sido Peliculas Ganadoras de Oscar a la Mejor Película y su puntuación en IMDB. La idea es obtener ambas informaciones de diferentes fuentes y métodos de extracción, poder limpiar los datos obtenidos, y relacionarlos. ¿Qué películas han ganado más Oscar? ¿Cuál es su puntuación en IMDB? ¿Cuántos Oscar han ganado las mejores puntuadas en IMDB? Estas y otras preguntas son las que daremos respuesta en este proyecto.\n",
    "\n",
    "\n",
    "\n",
    "<a name=\"workflow\"></a>\n",
    "\n",
    "## Workflow\n",
    "\n",
    "- WEB SCRAPING -\n",
    "\n",
    "Hemos trabajado Web Scraping desde el link de Wikipedia con el listado de películas ganadoras de Oscar a la Mejor Película. https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films\n",
    "\n",
    "Con Web Scraping hemos extraído la tabla de ganadores y nominados cada año, y hemos trabajado sobre ella para quedarnos solamente con el listado de ganadores por cada año. Hemos convertido a DataFrame para poder limpiar algunas informaciones que no nos interesaban, reordenar columnas, y sacar ya unas primeras conclusiones en cuanto a películas con más premios, con más nominaciones y como extra un ratio de premios ganados en relación con el número de candidaturas que tenían.\n",
    "\n",
    "- API -\n",
    "\n",
    "Una de las principales web de opinión y análisis de cine es IMDB. Sin embargo, no dispone de API que permita extraer información de ella. Como alternativa, tenemos OMDB, una web con API accesible gracias a la cual introduciendo el título de la película o el ID que tiene en IMDB, nos da toda la información de cada una de ellas. Año de la película, director, actores principales, recaudación en taquilla, entre otras, son algunas de las muchas informaciones que nos proporciona.\n",
    "\n",
    "En el proyecto hemos comprobado como funciona esta API con un primer ejemplo de película, y una vez mostrado, lo que hacemos es llamar a esta API para todo el listado de películas que hemos extraído previamente del link de Wikipedia que hemos ya comentado.\n",
    "\n",
    "De esta manera, iremos sacando toda la información de cada película ganadora de Oscar a la mejor película, entre ello el dato que más nos interesaba, que era su puntuación en IMDB.\n",
    "\n",
    "<a name=\"results\"></a>\n",
    "\n",
    "## Results\n",
    "\n",
    "- Combinación Web Scraping + APIs -\n",
    "\n",
    "En este tercer bloque hemos relacionado las dos tablas obtenidas previamente. Tanto la tabla con las películas ganadoras de Oscar a la mejor película como la tabla con la información obtenida mediante API de cada una de ellas.\n",
    "\n",
    "Hacemos un merge de ambas tablas para unificar la información de cada película, eliminamos algunas columnas que no nos resultan interesantes para nuestro análisis y sacamos resultados comentados en el notebook sobre cuál es la puntuación en IMDB de las películas con más premios Oscar y viceversa, cuántos Oscar han ganado las películas mejor valoradas en IMDB.\n",
    "\n",
    "¿Se corresponde las películas más galardonadas con las mejor valoradas por los espectadores? ¿Hay alguna gran película para los amantes del cine que sin embargo no haya conseguido tantos premios como pudiera parecer? Algunos resultados son sorprendentes e inesperados. Cojan sitio en su butaca, apaguen los móviles y disfruten del proyecto. Acción!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
