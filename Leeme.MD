<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>


#   Project Ironhack Data Bootcamp

Gabriela Pardo de Andrade Aljure

*Data Part Time Barcelona Dic 2019*


## Content
- [Project Description](#project)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Results](#results)

<a name="project"></a>

## Project Description


For my project I have selected de Star Wars API: SWAPI (swapi.co/api/). 

The objective of this project is to create a data set of all the Star Wars Episodes with the Titles of the movie and the Characters, Planets, Starships, Vehicles, Species, Movies poster and hyperlinks to the official website for each episode.

Issues encountered:

-Main Api is made up of SubApis.

-Information in the SubApis is a direct refrence to the other SupApis, meaning many of the columns of the SupApis are lists of links for other supapis.

-I was not able to create one dataframe with both images and clickable links because:

    1) To introduce the images in the DF It turned into: IPython.core.display.HTML which did not let me becaus: HTML' object has no attribute 'style' and to make the link clickable I was using: .style.format
    
    2) I could make a link clickable but when I turned it into an HTML object it would lose the clickable format.



<a name="dataset"></a>

## Dataset



<a name="workflow"></a>

## Workflow

Please refer to the Jupyter Notebook, which is explained in [here](https://github.com/Gabjure/project-web/blob/master/STAR%20WARS%20API%20AND%20WEB%20SCRAPING.ipynb)


<a name="results"></a>

## Results

![DataFrame 1](/img/sw_clickable.jpg)
