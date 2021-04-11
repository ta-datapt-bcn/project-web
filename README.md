![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# PROJECT 3_ Project web_Carlos Azagra

The goal of this project is practicing what I have learned in the APIs and Web Scraping chapter of this program. I will scrap two different websitdes related to football by using two different methods:

- **API - Football Data**: from which I will obtain different type of data such as participants, standings, matches, results or scorers from different competitions of different countries. By using this API I can only access to information about last 3 years.

- **Web Scrapping by reading HTML - BD Futbol**: from which I cannot obtain as much data as Football Data, but I have more access to historic data, which will allow me to get other type of data to get other analysis.

## API_Football-Data.org

Football-Data is a website that includes a big quanity of data from many different competitions from all around the world. The data of the API is divided into 4 main areas:

1. Competitions: which have information like standings, matches, teams and scorers
2. Matches: which have information like line ups, scorers or date
3. Teams: which have information like matches or players
4. Areas: which have information from competitions and their locations

The data is public but makes the consumer to cerate a user with its own token to access more specific data.

I will scrap the API by defining a class and creating different functions that will allow me to obtain different type of data from the competition I am interested on.

Once I have defined the class and its functions I will create an element in the class with which I will access the information by calling the functions and indicating the arguments that I need. Once I get the desired output it will be converted to a Pandas DataFrame and exported to a CSV file.

### Query competitions - La Liga

Obtain the following information from Spanish competition La Liga:
 
 1. Participant Teams in current season (2020)
 2. Next matchday and its schedules in current season (2020)
 3. Standings from last season (2019)
 4. Top10 scorers from two seasons ago (2018)

### Query teams - FC Barcelona

Obtain the following information from FC Barcelona:

5. Basic club information
6. Competitions in which the team competes this season 
7. Players from the squad

## Web Scrapping_Bdfutbol.com

Bdfutbol is a website dedicated to collect data related to football. 

As I commented, I cannot obtain as much detailed information (and not as easy) as the one in the API,but this website includes data from all the history of many competitions.

Instead of being able to call de functions to get information from the competition or team desired by the user, I will set a more precise goal to get by studying this data.

In this case, I will study the stats of FC Barcelona during the 15 completed seasons Messi has been a player for this team, and I will compare them to the rpevious 15 seasons, in order to try to analyse the effect the player has had. Of course it is very simplistic to make this analysis, as in the team Messi is not playing alone, but it is the easiest way to make a comparision.

I will compare:
- Total games won
- Total games draw
- Total games lost
- Total goals scored
- Total goals received

By doing so, I will be using LXML library and XPATH to obtain data from the HTML of the website.

Output needed:

1. Standings per season of 15 years with Messi
2. Standings per season of 15 years without Messi
3. Total standings: sum of both 15 years with and without Messi
4. Direct comparision between total standings


Once I get the desired output it will be converted to a Pandas DataFrame and exported to a CSV file. 

---

## Deliveries:

- **project3_projectweb.ipynb** - Notebook with all the coding
- **API_output folder** - Folder that contains all the output from the API Football-Data.org in .csv files
- **WS_output** - Folder that contains all the output from the website Bdfutbol in .csv files

