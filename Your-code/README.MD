<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>


#   Project Ironhack Data Bootcamp

MIGUEL GARCÍA MELGAR

*Data Part Time Barcelona Dic 2019*


## Content
- [Project Description](#project)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Results](#results)

<a name="project"></a>

## Project Description

### Overview

The goal of this project is for you to practice what you have learned in the APIs and Web Scraping chapter of this program. For this project, you will choose both an API to obtain data from and a web page to scrape. For the API portion of the project will need to make calls to your chosen **API**, successfully obtain a response, request data, convert it into a Pandas data frame, and **export it as a CSV file**. For the **web** scraping portion of the project, you will need to scrape the HTML from your chosen page, parse the HTML to extract the necessary information, and either **save the results to a text (txt) file if it is text or into a CSV file if it is tabular data**.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!


### Technical Requirements

The technical requirements for this project are as follows:

* You must obtain data from an API using Python.
* You must scrape and clean HTML from a web page using Python.
* The results should be two files - one containing the tabular results of your API request and the other containing the results of your web page scrape.
* Your code should be saved in a Jupyter Notebook and your results should be saved in a folder named output.
* You should include a README.md file that describes the steps you took and your thought process for obtaining data from the API and web page.

### Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* An **output folder** containing the outputs of your API and scraping efforts.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

<a name="API"></a>

## API
 
 The API we used to get information with was [PokéAPI](https://pokeapi.co/).


<a name="web"></a>

## Web
 
 The web we screped information from was [pikalytics](https://www.pikalytics.com/).


<a name="workflow"></a>

## Workflow

### Prepare your IDE

- Download CSV
- Rename it as Shark_Attack
- Import the needed libraries
- Import CSV 

### Examine For Potential Issues
- Used .shape and .head() to obtain an overview
- Missing Values: Calculated the percentage of null values using .info and .isnull
- .shape and .head() to get a general overview of the contents
### Start Cleaning The Data
- Drop columns with more than 50% null values
- Drop rows that are still missing more than 33.33% values
- Check On Similarly Named Columns
  - Dropped rows with mistakes (non identical values in the row) in href & href formula
  - Dropped rows with mistakes (non identical values in the row) in "Case" columns
### Data manipulation
- Reorder Columns
- Rename Columns
- Extreme Values And Outliers
- Low Variance Columns
- Duplicates removal
- Data Type
- Remove columns I won't use
- Remove unknown years
### Fix Countries
- Created a dictionary to clasify countries by hemisphere
- Cleaned the data related to countries and sorted the values in Country alphabetically
- Created an hemisphere column indicating in which hemisphere is each country
### Seasons
- Used months indicated in the dates and the hemispheres info to get the seasons when the incidents were reported.
<a name="results"></a>

## Results

At first we got a 5992x24 dataframe but after the cleaning and a bit of manipulation is a 5798x9 dataframe. If I had more time I'd like to clean much more and do it more carfully as I dropped some data that might have been corrected replacing info and using RegEx.

I feel that the oldest the information is the less precise it is and there were also more null values in those rows. It should be interesting to convert more columns data to numeric typs so as to makes some statistics analysis and decide properly on that since wich year we should keep the data and which variables should be dropped.


# Bonus

## Graphic representation of Country x Hemisphere x Season
- Used plotly.express to visualize better the relationship between Country, Hemisphere and Season.
- I decided to drop all data but what was registered from 1995.
- There I found that some Dates were not cleaned propperly so I decided to restart this last part using creating and working on a new dataframe based on the one used during the whole project. In short, I dropped them.
- This bonus started with the "clean" 5798x9 dataframe but ended up working on a new dataset of 2047x9.