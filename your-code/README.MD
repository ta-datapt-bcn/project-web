<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Most Popular Video Games 
*Paula Gual*

*Data Part Time Barcelona May 2019*

## Content
- [Project Description](#project)
- [Api](#api)
- [Website](#website)
- [Workflow](#workflow)
- [Results](#results)
- [Obstacles](#obstacles)
- [Lessons Learned](#lessons)

<a name="project"></a>

## Project Description
Fins the 50 most popular videogames, and its social links.
<a name="api"></a>

## API
The API is from the IGBD (Internet Games Data Base)
https://api-v3.igdb.com/

<a name="website"></a>

## Website
The websites are the websites of each game in the IGDB.

<a name="workflow"></a>

## Workflow

### Find an API and a Website
* I tried many Fortnite apis, but as there is no official api, the apis where working unevenly.
* Then I found the IGBD and I liked the API and selected it. They do not have the documentation specificaly for Pyhton, but they have a pretty nice documentation and a not so much complicated way of giving the free access tokens.

### Define the info I need to retrieve

I need to retrieve the 50 most popular games, accorfing to IGDB. And the for each game, retrieve the social links info from their game.

### API

* I test the API with a simple endpoint request
* Then I select the parameters and endpoints I want to retrieve
* I retrieve the info and put it on a data frame
* Then a create another dataframe **games** with just the info I needed.

### WEB

* I test the webscaping parsing proces with the first game
* Then I create a function to retrieve all the urls info about the social links
* I create a list with all the different social sites
* I create a data frame with the url + the list of social sites as columns
* Put all the info in the **social_df** with each game in a row

### MERGE

* Using the 'url' I merge both dataframes in a **final_games**

### Dataset

I export the dataframe in a csv on the output folder

<a name="results"></a>

## Results

A CSV with the 50 most popular games and its social links

<a name="obstacles"></a>

## Obstacles

The Apis are quite difficult to use, as some have a lot of restrictions and other do not work precisely. 

<a name="lessons"></a>

## Lessons Learned

* I have learned to understand much better how to use an API
* I have leaned to test the API to check if it can do what I want prior to start programming
* I have leaned to create a function to parse similar urls
