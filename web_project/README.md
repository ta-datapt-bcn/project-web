![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

Isaac Rodriguez
Data Part Time Barcelona Dic 2019

## Overview

How much do your groceries cost in Bitcoin? Purpose of this project is to take a step further and know by first-hand how we are going to life in the future. 1€ just for a can of coke? Not in the future as we will talk about satoshis.

Structured as a utopia, we are going to scrape the ulabox website to get all the items and then convert the prices in a btc format - also in satoshis.

---

## References

* __Website__: Ulabox to get all items by category and subcategory. As there is no a public api, used scraping technologies to do it.

* __API__: Blockchain API is used to get the bitcoin price in real time.

## Structure

* __1__: From Ulabox website, save all categories with its link inside a DataFrame(df_category).
* __2__: From each category, look up for its subcategory and save it also into a DataFrame(df_subcategory).
* __3__: From each subcategory, look up all items available and get name, brand, price, also append each one into a DataFrame(df_articles).
* __1__: Get current BTC price from Blockchain API and create a new column (price_btc) with the price in euros converted.

## Room for improvements

* __Pagination__: When we scrape each category we should be able to enter all available pages to get all items.
* __More cryptocurrencies__: Not only Bitcoin but Ethereum, Litecoin, etc.
* __Play with data__: Be able to filter items by category, subcategory, price, etc.
* __Get items from others stores__: Mercadona, Carrefour, etc.

## Conclusions

This project helped so much to deeply understand web scraping technologies. Applied creativity as this project was open to choose what website and API use. Even I already submitted it I will be in charge to make a useful product.
