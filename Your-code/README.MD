<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>


#   Project Ironhack Data Bootcamp: API and Web Data Scraping

MIGUEL GARCÍA MELGAR

*Data Part Time Barcelona Dic 2019*


## Content
- [Project Description](#project)
- [API](#API)
- [Web](#web)
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
 
 The API we used to get information with was [pikalytics](https://pikalytics.com/api/p/2020-01/ss-1760).


<a name="web"></a>

## Web
 
 The web we screped information from was [wikidex](https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_con_sus_estad%C3%ADsticas_base).


<a name="workflow"></a>

## Workflow

### Prepare your IDE
- Import Useful Libraries

### Working On The API
- Getting the needed information from the API.
- Drop the columns we don't need and clean the remaining information.
- As there were some issues to clean properly the column team we will make a copy from it and treat it individually.
- Now we'll create new columns in the original dataset to add the information we wanted from the DF we cleaned separately.
- Clean pikalytics dataframe and which will be exported as csv.

### Working On The Web
- Getting the needed information from the web.
- Cleaning the data we got and generating a dataframe.
- Clean wikidex dataframe that is to be export as csv.

## Results

We have been able to obtain just the data we initially thought would be needet. Yet there is too much info in separate dataframes so it is quite difficult to get insights from both of them. So we will make a single dataframe to make interpretation easier.

# Bonus

## Combining Information
- Merging the resulting dataframes.
- Drop columns that add no information.
- Reorder columns.
- Rename columns.
- Resulting combined dataframe to be exported.

## Analyzing
- Look for outliers.
- We clean and manipulate this new "outliers" dataframe.
- Lower outliers, so... Pokémon that are very rarely used in VGC but you should still be careful with.

## Correlations
It seems that "lower" outliers are more depandant on their base stats mean compared to the population overall but there's a very little difference so we should try to focus on other variables. I personally think it could be their battle roles, but this information was not in any of the datasets I worked with or were at least candidates that ended being discarded.
