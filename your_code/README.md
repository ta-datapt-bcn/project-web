<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>


#   Project Ironhack Data Bootcamp

KRISTINA KUNCEVICIUTE

*Data Part Time Barcelona Dic 2019*


## Content
- [Project Description](#project)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Results](#results)

<a name="project"></a>

## Project Description

The goal of this project is to practice APIs and Web Scraping. Optain data from API and a web page. For the API portion of the project make calls to API, successfully obtain a response, request data, convert it into a Pandas data frame, and export it as a CSV file. For the web scraping portion, scrape the HTML from a page, parse the HTML to extract the necessary information, and either save the results to a text (txt) file if it is text or into a CSV file if it is tabular data.

- Collect the information about the movies that have 'love' in the title for the Valentine's day campaign (Title, Director, Rating, Release Year, Link to Trailers and Videos, download Posters)
- Check if the information from the API is coinciding with the information in IMDB
- Check the correlation between the days to Valentines day and rating

<a name="dataset"></a>

## Data

API: OMDB http://www.omdbapi.com/#usage <br>
Web Sraping: IMDB https://www.imdb.com/

<a name="workflow"></a>

## Workflow

- Use OMDB API: http://www.omdbapi.com/#usage
- Do the API request with the search, movies with word 'love', extract information from 4 pages
- Generate the list of titles of the movies
- Do another API request title by title to get all information about the movies
- Put info from both requests to one dataframe
- Scrape IMDB based on IMDB ID to get the main information
- Check if data is matching in the dataframes from API and IMDB in these columns: Title, Year, Director, IMDB Rating
- Prepare one dataframe with information from API and IMDB and export
- Analyze if there is any correlation between the Release Day days to Valentine's day and the rating value

Libraries used:

- pandas
- json
- requests
- bs4
- urllib.request
- re
- numpy
- time

<a name="results"></a>

## Results

- Collected all the information that was necessary for the campaign, extracted video links from IMDB and downloaded movie posters to a separate folder
- It's possible to select (if needed) which title want, original or English
- It's possible to decide how many movies want to check (by changing the number of pages in the API request)
- Understood the difference in the release year that was given by API
- From checking average rating per bin understood that the average rating is not higher if the release date is closer to the Valentine's day
- Correlation between the ratings and the Valentine's day is very low. As a next step, could check only the movies release in the last few years, maybe there is a different trend latelly. Also, to really see the correlation, would need to ahve a bigger database (have information of more than 40 movies)
- Understood that 47.5% of love movies (from this dataset) have been released very close or close to Valentine's day