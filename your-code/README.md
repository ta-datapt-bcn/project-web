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