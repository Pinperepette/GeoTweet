# GeoTweet
Program to search tweets, tag, hashtag, user, with locations and maps
- credits @Pinperepette, @Daniele_KK, @eddy_mane, @porelmorro, @grostein.

# Addictions:
tweepy, geopy, folium, SimpleHTTPServer, SocketServer, webbrowser

# Settings:
Edit your keys.py with your twitter api.

#Usage Example:

For search 200 results on #python in a country:

python geotweet.py -z IT -n 200 -m

with -n set results count
with -m create the visual map (optional)

For open the visual maps:
after performing the desired command , 
launch the web server with 

python geotweet.py -s

and open the browser on the link you see in terminal.
