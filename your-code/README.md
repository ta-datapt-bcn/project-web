# API and Web Data Scraping 
## Dani Eiroa


## :musical_note: Part 1. API 
* I used the [Spotify  Web API](https://developer.spotify.com/documentation/web-api/) identifying myself as a developer and obtaining a CLIENT_ID and a CLIENT_SECRET
* The token part was tricky at the beginning. The token expires after some time, so I had to go to the [console](https://developer.spotify.com/console/) to get a new one.
* Initial problems with authentication were later solved using the [SpotiPy library](https://spotipy.readthedocs.io/en/latest/)

### Objectives:
* Getting adequate responses using Spotify's API.
* Extracting information of users.
* Specifically retrieving songs from friends playlists and create a dataframe with those songs.
* Clean resulting dataframe.

### Setbacks:
* Spotify limits the request to a maximum of [50 playlists](https://developer.spotify.com/documentation/web-api/reference/playlists/get-list-users-playlists/) and [100 songs](https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/) per playlist


### Code explanation:
* Step by step explanation is provided in the [notebook](https://github.com/EiroaMD/project-web/blob/master/your-code/API_final_anonymous.ipynb)




## :musical_note: Part 2. Web Scraping
* I chose Wikipedia as a source of tabulated information about the number one hits for every week since 2011.

### Objectives:
* Parsing html webpages.
* Identifying the content and the html tags needed to extract the information wanted.
* Extracting and organising such information.
* Inserting it in a dataframe containing date, number 1 song title and artists.
* Looping to insert also year and number of week for every date.

### Setbacks:
* Different url pattern depending on the year.
* Merged cells inside tables (for consecutive weeks with the same number 1 song) were a bit difficult to parse (ugly if/elif/else chunk of code)

### Code explanation:
* Step by step explanation is provided in the [notebook](https://github.com/EiroaMD/project-web/blob/master/your-code/web_final.ipynb)


## :musical_note: Part 3. Merging dataframes
* Both dataframes are loaded and an inner join is performed.
* EDA is performed over resulting dataframes, and inconsistencies are corrected.
* A count of number of hits for every user is performed and they are ordered by number of hits inside their lists.

* Step by step explanation is provided in the [notebook](https://github.com/EiroaMD/project-web/blob/master/your-code/join_df.ipynb)


## :sweat_smile:​ Improvements
* Many, amongst the most relevant:
    * More dataframe cleaning and manipulation (sorry about this, ran out of time).
    * Extracting more quantitative data, as most of it is qualitative.
    * Cleaner and more elegant coding.
    * Improving the final output and finding other ways to merge both dataframes to extract different information.
    * Implementing a better way to solve the problem of the merged cells of wikipedia tables, such as [this one](https://johnricco.github.io/2017/04/04/python-html/)