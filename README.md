![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# *WEB PROJECT* #
## by Hernán Sosa.

Our objective for this project will be **creating a function that gives us information about all the shows** an artist (or group of artists) has done. 
This function should give us:
- Data for an artist or a list or artists.
- Data for a genre or a list of genres.
- We'll have to be able to specify how many artist to get

This data has to be clean, readable and organized. We'll have to use both web and API scraping to gather the data.
By examining both tools, we figured out that our way to do it will be the following:

# 0. Approach:

First, we know that we'll need the following data:
     
     - Artists database
     - Genres database
     - Popularity Database
     - Shows database
     - Info for each show



#### **`Discogs`** is an internet web database which compiles over 170,000 artists, classified by genres. Also classifies every artist by sub-genre and popularity. Includes metadata for each album released for each artist.

Given this information, we'll know that we will use `web scraping` to gather the following information:

    - Artist Database
    - Genres Database
    - Get popularity for each artist
    
#### **`Songkick`** is an API that contains information about every show an artist has done in his carreer. We found out that, in order to access an artist, we need a Songkick ID. For that matter we'll have to split our API job into two parts:

    - Getting ID for an artist
    
    - Fetching Data for that ID
    
    
    
 
#### For the job, we'll be importing the following libraries:

        requests
        json
        BeautifulSoup
        pandas
        json_normalize
        re
        math
        numpy as np

<img src="https://www.discogs.com/images/brand/discogs-logo.svg" alt="drawing" width="200"/>

# 1. Artist, Genres and Popularity



We want to get a list with `n` artists, searching by most popular albums by style in `discogs.com`. By changing the style in the link, we can apply the same job on other music styles. The style code in the link its noted as '`&style_exact=Sample+Style`'. By concatenating them, we can choose multiple styles.

We extracted the artist name for each record stored in the page. The tag for the artist is named 'h5'.

We'll create a function to clean up the string. Luckily for us, these strings come pretty clean.

        def clean_artist(string):
        '''
        This function takes a string and erases the skipline '\n', parenthesis '()' and stars '*'
        '''



Now we find a problem. The sited is mainly organized by GENRES or STYLES (sub-genres). In order to properly use one of them, we'll need to extract the page link instead of the genre/style name, because each type has its own path:


Similarly, we can extract the 'style_exact=Sample+Style' items:

styles_list = [element.get('href') for element in soup.find_all(tag, attrs={'href': re.compile("style_exact=")})]

We'll define a function that searches for a Genre or Style, and returns it's link piece, with the format ' &'GENRE/STYLE'_exact=ENTRY' For that matter, we'll filter if the keyword belongs to Genre or Style, then we'll apply the link piece format.

        def genre_link(string, genres=genres, styles=styles):
        '''
        This function takes as an input a genre or style name, and returns a piece of link depending on its category
        ''' 

We can clearly see that there are some elements which are repeated, so to find 'n' artists we'll iterate over the webpage until our list meets the requirements.

        def artist_scrape(genres='Rock', n=10):
        '''
        This function scrapes the Discogs.com webpage to get 'n' artist names, 
        sorted by popularity and filtered by genre.
        Returns a list with artist names.
    






<img src="https://i.pcmag.com/imagery/reviews/03YAx3GmCDl3P61FI96P5GE-5.fit_scale.size_1028x578.v_1569471412.jpg" alt="drawing" width="250"/>

# 2. Fetching show information

Now that we have the bands list, we want to find out how many concerts they made, when and where. We'll use the `Songkick` API. Because of the structure of this API and the data we collected, we'll have to break this step in two parts:

##  2.1 Artist ID gathering

In order to locate an artist we're interested in, we'll have to find the unique ID of this artist on a separated part of the API of Songkick. `https://www.songkick.com/developer/artist-search`


First thing we find out is that in order to correctly acces the band name, we'll have to replace all whitespaces with '_' (underscores). So we're making a function for it:

        def underscore_artist(artist):
            '''
        This function takes an artist name and transforms its string into 
        a 'Str_Str' format
            '''

We have the form of this link to look for Artist IDs:
        `'https://api.songkick.com/api/3.0/search/artists.json?apikey=' + apikey + '&query=Pink_Floyd'`


        artist_id = results['resultsPage']['results']['artist'][0]['id']

Similarly to the Discogs.com process, we'll make a function that returns all the Artists IDs (in the same order)

        def songkick_artist_id(artist_list, apikey = apikey):
        '''
        This function locates an Songkick ID number for a given list of artists. Then, it creates a tuple
        with the band ID and the band name
    
        Takes two arguments:
        
        artist_list = type lst: List of artist names to be found. If an input it's a string, transform it
                                into a list for a correct processing.
                                
        api_key = type str: Your Songkick API key
    
        The output is a tuple composed of two parts:
    
        output[0]= type int: List of Songkick IDs
        output[1]= type str: Artist names
     
    
  
We want to store the IDs and the Artist Name, because later on we found out that if an Artist plays in a Festival, this artist ID it's kinda randomized on the API


Now that we have the artist name and the artist id, we can now find some more data we're interested on. We want to find:

- The concert name
- The concert date
- The concert time
- The city where the concert was done
- The venue where the concert was done
- The coordinates of that venue
- If the artist was headlining the concert (billing)

https://www.songkick.com/developer/past-events-for-artist

All the data we're looking for it's located on this API link, we'll have to explore the JSON object to find it out:

https://api.songkick.com/api/3.0/artists/{artist_id}/gigography.json?apikey={your_api_key}


In this phase, we're doing a bit of exploration. After finding the right information navegating through the .keys() dictionary method, since we're working with a json file


### 2.2.1 Finding the concert date

                    result['resultsPage']['results']['event'][0]['start']['date']

### 2.2.2 Finding the concert time

                    result['resultsPage']['results']['event'][0]['start']['time'] 

### 2.2.3 Finding the city where the concert was done

                    result['resultsPage']['results']['event'][0]['location']['city']

### 2.2.4 Finding the venue name where the concert was played

                    result['resultsPage']['results']['event'][0]['venue']['displayName']

### 2.2.5 Finding the coordinates of that venue

                    result['resultsPage']['results']['event'][0]['venue']['lat'] 

                    result['resultsPage']['results']['event'][0]['venue']['lng'] 
    
### 2.2.6 Finding out if the artist was headlining the concert ( billing )

                    result['resultsPage']['results']['event'][0]['performance'][0]['billing']

## 2.3 Defining a function for our data rows:

Finding out that the pagination comes as an argument in the link= '&page=%s'. We have 50 entries per page

The number of pages on each ID will be equal to its entries, divided by the elements by page. 
For example, 1104/50=22.08 pages.

Since the number of pages is not an integer, we'll round up this number to iter on the elements that are left. 
If the pages are 22.08, we'll iter over 23 pages.

Now, we're making a function to collect the data of each show for every artist id we pass on the list #artist_id, called `collect_data()`:

        def collect_data(artist_id_list, apikey='PxrJ1AnxJlC6uT7i'):  
        '''
        This function iterates over an artist id list to get the links on each artist.
        Calculates in how many pages the data is stored, and iterates on all of them.
        Then, for each page, requests the information to the API and fetchs all the data we need.
        Stores this data as a list of lists object to ensure compatibility with Pandas Dataframes.
        '''
    

We'll define a function with the scripts we used through the process. This function is called `get_shows_data()`:

        def get_shows_data(n=10, genres='Rock', apikey=apikey, artists = None):
        '''
        This function returns an organized list of lists which contains information about all the shows played
        by that artist over its history. Uses 
        
        n = type int: Tells the function hoy many artists to get info
        

To test it, we have a lot of genres to choose from!
 

Ok, we have our data in a tidy way (as a list of lists for each show). Now, it's time to construct our DataFrame with this data:




# 4. Building the DataFrame

We stored our values in a convenient list of arrays for each show we collected. So, to construct it, we'll just have to call pd.DataFrame and introduce the list we created, along with the columns names:


df = pd.DataFrame(data)
df.columns = ['artist', 'artist_id', 'relevance', 'show_name', 'date', 'time', 'city', 'venue', 'lat', 'lng']
df.head()


We'll use a function to know the percentage of NA values, `df_total_na()`:

                        def df_total_na(df):
                        '''
                        Returns the percentage of total NULL values in the dataset
                        '''
                        total_obs = df.count().sum()
                        total_nas = df.isna().sum().sum()
                        nas_percentage = total_nas *100 / total_obs
    
                        print(f'Our dataset has {round(nas_percentage, 2)}% missing values overall' )


Our dataset has 7.94% missing values overall


Also checking what columns have more percentage of null values, with `colum_nulls_percentage()`

                        def column_nulls_percentage(df):
                        '''
                        Returns a series indicating percentage of NULLS per column
                        '''
    
We find out that time column has a considerable amount of NAs an is not useful for us. We'll arrange the dataframe and don't preserve it for now. artist_id, and show_name are also not useful for us for the moment.

df = df[['artist', 'date', 'time', 'venue', 'city', 'relevance', 'lat', 'lng']]


# 5. Usage of the data

This dataframe is very interesting to understand the music movement and artists. If we know that this dataset is 100% accurate (which it's not), and contains every show an artist has done (which it doesn't), we could ask a lot of questions:

    - Which genres are more active when comes to show playing?
    
    - Is there any way to predict if an artist is coming soon to your Country?
    
    - Which are the more active venues? For what genres?
    
    - Which countries consume what type of show or genre, and what's the history of every country in this aspect?
    
    - Do political/historical events do impact on artist growth or activity?
    
    - What's the tendency of a new artist, relative to number of shows, compared to an older one?
    
    - What's the percentage of festivals shows relative to normal shows for each artist? Why?
    
    - There is more activity related to concerts nowadays, or few years ago?
    

    
We can also include very useful tools:

    - Extract future events
    
    - Genre multiselector
    
    - Genre/Popularity heatmap by Country
    
    - Histogram for an artist/nº of shows per country