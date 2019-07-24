This project was based in obtaining information about recipes for home brewing ("cooking" beer at home).

Basically, beer is made from water and three ingredients: malt, hops and yeast. The public API from BrewDog brewery contains the recipes for 24 of their beers. 

A request was made to the API to get a JSON file containing information about ingredients and amounts. A dataframe was constructed for any of the 3 ingredients (malt, hops and yeast) and they were finally merged in one dataframe.

Beers are usually classified in styles, but the API did not contain any information about the style of the beers. To obtain this information web scrapping was used to find every BrewDog beer style in Ratebeer web page. A request was made to obtain html code from the web site and the beer name and style was obtained from it.

Finally, both dataframes were joined to add the style to the beer recipes.
