![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Web Data Scraping

## Overview

In this project I have imagined that I work for Revlon Professional, a brand of professional haircare products. 
I wish to improve the positioning of our products on the Amazon search results, so I need to scrape Amazon data to analyze it and understand why some products rank higher than others. 

## Objectives

* Objective 1: obtain data from the Haircare products section when a user perfroms a search of our brand ("revlon professional"). We want to check which articles rank higher to see if they are the ones we want to prioritise or not, and if not, take actions to change the order. Total products: 796.
* Objective 2: obtain data from the Haircare products section when a user perfroms a search for professional products ("profesional"). We want to check how we rank compared to our competitors, and identify trends for the top ranking products to improve our ranking. Total products: 5.000+.

## Necessary Data

I chose to obtain the following fields because they might have an impact on a product's ranking: 
* Product name
* Brand
* Final price
* Bulk price
* Price before discount
* Rating
* Number of reviews
* Delivery date

## Methods and results

For the first objective, I used BeautifulSoup. I identified the differences between the URLs of the different pages and created URLs with an f string and a for loop. The resulting csv file is in the outputs folder. 
For the second objective, I used Scrapy. The resulting csv file is in the outputs folder.
I also did some scraping with Selenium, but it was too slow and I did not continue with it. 

## Obstacles

* Complexity of the HTML code on Amazon.
* The brand is not in a separate HTML object, it's contained in the title.
* Some products have some empty fields (solved with default=None or with try/except).
* User Agent not added on Scrapy (solved it adding it in settings.py)
* Identation error (solved it by converting it to spaces with Sublime)

## Learnings

* Learned to read HTML and XPath
* Learned to use BeautifulSoup, Scrapy and Selenium
* Used Sublime text editor for the first time 

## Next steps

* Cleaning and analyzing the data
* Creating a more complex spider that goes into the page of each product
