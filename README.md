# GeoTweet
Program to search tweets, tag, hashtag, user, with locations and maps

Credits

- [@Pinperepette](https://twitter.com/Pinperepette)
- [@Daniele_KK](https://twitter.com/Daniele_KK)
- [@eddy_mane](https://twitter.com/eddy_mane)
- [@porelmorro](https://twitter.com/porelmorro)
- [@grostein](https://twitter.com/grostein)
- [@Ludo237](https://twitter.com/Ludo237)

# Requirements:

You can install this requirements by running `python setup.py` before anything else.

Requirements are
- tweepy
- geopy
- folium
- SimpleHTTPServer
- SocketServer
- webbrowser

# How to use:

First of all you have to edit the `keys.py` in order to change the default placeholders with your twitter API values, 
then run `python setup.py` if you need to install the requirements and last `python geotweet.py`


# Usage Example:

For search 200 results on #python hash tag in whatever country:

    python geotweet.py -z IT -n 200 -m

- with `-n` set results count
- with `-m` create the visual map (optional)

**Opening the visual maps:**
After performing the desired command, launch the web server with 

    python geotweet.py -s

and open the browser on the link you see in terminal.

# Example Image:

![](https://github.com/Pinperepette/GeoTweet/blob/master/image.png)
