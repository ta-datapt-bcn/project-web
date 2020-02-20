#   Project: API and Web Data Scraping

`Dinis Oliveira Costa`


## Content
- [Project Description](#project)
- [Data](#data)
- [Workflow](#workflow)
- [Results](#results)


## Project Description

- The goal of this project was to practice the APIs and Web Scraping skills acquired until now. It was chosen both an API to obtain data from and a web page to scrape.

- The commands assume a basic understanding of the Pandas, BeautifulSoup and Requests libraries.

## Data

The data used in this project was collected from:

- `TVMAZE` - a free, fast and clean REST API that's easy to use, returns JSON containing lots of information about almost any TV show - and

- `IMDB` - an online database of information related to films, television programs, home videos, video games, and streaming content online.

The goal was to collect relevant information about a TV show called **Game of Thrones** that aired between 2011–2019 and currently sits as the second highest rated television show on IMDB with 9.3/10, only after Breaking Bad (9.5/10).

The focus of this project was to collect data regarding each episode and season and cross it with its public rating on IMDB.

## Workflow

The project follows three essential steps - **API Request**, **Web Scraping** and **Merging and analysing the data** - in order to make it easy to keep track of changes and better structure the clean data set.

Before you begin, start by importing the table and the necessary libraries. Ready? Let's go!

### Step 1 - ` API REQUEST`

- using the TVMAZE API, it is possible to search through all the shows in their database by the show's name
- since the objective is to gather data about each episode, we will use the call the show's main information and its episode list in one single response

1.1 - Getting the data from the AP
1.2 - Passing the data to a DataFrame
1.3 - Data Cleaning

### Step 2: `Web Scraping`:

- resorting to each season's episode list, it is possible to consult the rating each episode got
- using a list of all seasons, we will be able to run a script that collect the elements from all the episodes in each season

2.1 - Defining the Column Names
2.2 - Scraping each of the elements from each page and adding them to a list
2.3 - Data Cleaning the results we've gotten from scraping the HTML code
2.4 -Creating a new DataFrame with the data collected from Web Scrapping


### Step 3: `Merging and analysing the data`

3.1 - Data Cleaning of the final DataFrame
3.2 - Analysis of the results



## Results

- Clean data set containing all the episodes from each of the seasons and information regarding: url, season, number, airdate, runtime, a summary of each episode, the titles of each episode, the ratings and total votes.


## Deliverables

- `GoT_web.ipynb` - containing all the code that built the project
- `data_API.csv` - with all the data collected from the TVMAZE API about the episodes
- `data_HTML.csv` - with the ratings per episode, total votes and titles 
- `got_final.csv` - which compiles all the information in a clean and structured way
- `top5_best.csv` - with the list of 5 highest rated episodes
- `top5_worst.csv` - with the list of 5 lowest rated episodes