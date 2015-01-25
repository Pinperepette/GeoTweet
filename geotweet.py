#!/usr/bin/python -u
#-*- coding: utf-8 -*-

#########################################################################
#  This program is free software; you can redistribute it and/or modify #
#  it under the terms of the GNU General Public License as published by #
#  the Free Software Foundation; either version 2 of the License, or    #
#  (at your option) any later version.                                  #
#                                                                       #
#  This program is distributed in the hope that it will be useful,      #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#  GNU General Public License for more details.                         #
#                                                                       #
#  You should have received a copy of the GNU General Public License    #
#  along with this program; if not, write to the Free Software          #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,           #
#  MA 02110-1301, USA.                                                  #
############################# DISCALIMER ################################
#  Usage of this software for probing/attacking targets without prior   #
#  mutual consent, is illegal. It's the end user's responsability to    #
#  obey alla applicable local laws. Developers assume no liability and  #
#  are not responible for any missue or damage caused by thi program    #
#########################################################################

import tweepy, geopy, sys, getopt, time, folium, SimpleHTTPServer, SocketServer, webbrowser

#Autenticazione
from geopy.geocoders import Nominatim
from keys import keys

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
geolocator = Nominatim()

number = 20
TAG = "x"
ZONE = "IT"
check_ZONE = "x"
MAPS = "x"
check_USER = "x"

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False 
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)


def logo_geotweet():
    print "----------------------------------------------"
    printout(" _____         _____               _   " + "\n", GREEN)
    printout("|   __|___ ___|_   _|_ _ _ ___ ___| |_ " + "\n", BLUE)
    printout("|  |  | -_| . | | | | | | | -_| -_|  _|" + "\n", YELLOW)
    printout("|_____|___|___| |_| |_____|___|___|_|  " + "\n", MAGENTA)
    printout("      Another way to use twitter       " + "\n", CYAN)

def credit():
    printout("[+]" , GREEN)
    print ("Create by @Pinperepette, @Daniele_kk, @eddy_mane, @porelmorro, @grostein"+ "\n")


def usage():
    logo_geotweet()

    printout("[USAGE:]   " + "\n" , GREEN)
    print (sys.argv[0] + " " + "[-h|--help] [-t|--tag] [-u|--user] "+ "\n"+"[-z|--zone] [-l|--line] [-n|--number] [-m|--maps]")
    print "----------------------------------------------"
    printout("[EXAMPLE USER:]   "  , BLUE)
    print (" " +sys.argv[0] + " " + "-u Pinperepette")
    printout("[EXAMPLE ZONE:]   ", YELLOW)
    print (" " +sys.argv[0] + " " + "-z IT")
    printout("[EXAMPLE TAG:]   ", RED)
    print ("  " +sys.argv[0] + " " + "-t Coccodio")
    printout("[EXAMPLE LINE:]   ", MAGENTA)
    print (" " +sys.argv[0] + " " + "-l Pinperepette"+ "\n")
    credit()

def http_run():
    printout("[HTTP RUN:]   ", YELLOW)
    print " localhost:8000 "
    printout("[STOP:]   ", RED)
    print " press ctrl + c "
    try:
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", 8000), Handler)
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close()


def search_user():
    user = api.get_user(arg_user_search, include_entities=1)
    print "----------------------------------------------"
    printout("[NAME:]   ", GREEN)
    print user.name.encode('utf-8')
    printout("[ALIAS:]   ", BLUE)
    print "@" + user.screen_name.encode('utf-8')
    printout("[ID:]   ", RED)
    print user.id 
    printout("[URL:]   ", BLACK)
    print user.url
    printout("[GEOLOCATION:]   ", MAGENTA)
    if user.status.geo == None:
        print user.status.geo
    else:
        print user.status.geo['coordinates']
        location = geolocator.reverse(user.status.geo['coordinates'],timeout=20)
        print location.address.encode('utf-8')
    printout("[FOLLOWERS:]   ", GREEN)
    print user.followers_count
    printout("[FRIENDS:]   ", BLUE)
    print user.friends_count
    printout("[BIO:]   ", WHITE)
    print user.description.encode('utf-8')
    credit()

def timeline_user():
    cont = 0
    user = api.user_timeline(screen_name, count=number)
    for tweet in user:
        print "----------------------------------------------"
        printout("[TWEET:] ", YELLOW)
        print " " + tweet.text.encode('utf-8')
        printout("[SOURCE:] ", GREEN)
        print tweet.source.encode('utf-8')
        printout("[DATE:] ", RED)
        print tweet.created_at
        printout("[RT:] ", BLUE)
        print tweet.retweet_count
        printout("[FAV:] ", WHITE)
        print tweet.favorite_count
        if tweet.geo == None:
            printout("[GEOLOCATION:]   ", MAGENTA)
            print tweet.geo
        else:
            printout("[GEOLOCATION:]   ", MAGENTA)
            print tweet.geo['coordinates']
            location = geolocator.reverse(tweet.geo['coordinates'],timeout=20)
            printout("[ADDRESS:]   ", CYAN)
            print location.address.encode('utf-8')
            if cont == 0:
                map_1 = folium.Map(location=tweet.geo['coordinates'], zoom_start=4, width=1800, height =1200)
                cont = cont + 1
            else:
                cont = cont + 1
                map_1.simple_marker(location=tweet.geo['coordinates'],popup=tweet.text.encode('utf-8'))   
                location = geolocator.reverse(tweet.geo['coordinates'],timeout=20)
    if MAPS == "y":
        map_1.create_map(path='maps_user.html')
    credit()

def search_tag():
    c = tweepy.Cursor(api.search, q=TAG)
    for tweet in c.items(int(number)):
        print "------------------------------------------------"
        printout("[NAME:]   ", GREEN)
        print tweet.user.name.encode('utf-8')
        printout("[ALLIAS:]   ", BLUE)
        print "@" + tweet.user.screen_name.encode('utf-8')
        printout("[TWEET:] ", YELLOW)
        print " " + tweet.text.encode('utf-8')
        printout("[ID:] ", RED)
        print tweet.user.id
        printout("[GEOLOCATION:]   ", MAGENTA)
        if tweet.coordinates == None:
           print tweet.coordinates
        else:
            print tweet.coordinates['coordinates']
            location = geolocator.reverse(tweet.coordinates['coordinates'],timeout=20)
            print location.address.encode('utf-8')
        printout("[SOURCE:]   ", BLACK)
        print tweet.source.encode('utf-8')
        printout("[TWEET ID:]   ", WHITE)
        print tweet.id
        printout("[NUMBER RT:]   ", YELLOW)
        print tweet.retweet_count
    if MAPS == "y":
        print "------------------------------------------------"
        printout("[!] ", RED)
        print "in search tag, maps are not abilited"
    else:
        sys.exit(2)
    credit()

def search_zone_map():
    cont = 0
    places = api.geo_search(query=ZONE, granularity="country")
    place_id = places[0].id
    tweets = api.search(q="place:%s" % place_id,count=number)
    for tweet in tweets:
        print "------------------------------------------------"
        printout("[NAME:]   ", GREEN)
        print tweet.user.name.encode('utf-8')
        printout("[ALIAS:]   ", BLUE)
        print "@" + tweet.user.screen_name.encode('utf-8')
        printout("[TWEET:] ", YELLOW)
        print " " + tweet.text.encode('utf-8')
        printout("[GEOLOCATION:]   ", MAGENTA)
        print tweet.geo['coordinates']
        location = geolocator.reverse(tweet.geo['coordinates'],timeout=20)
        printout("[ADDRESS:]   ", CYAN)
        print location.address.encode('utf-8')
        if cont == 0:
                map_1 = folium.Map(location=tweet.geo['coordinates'], zoom_start=4, width=1800, height =1200)
                cont = cont + 1
        else:
            cont = cont + 1
            map_1.simple_marker(location=tweet.geo['coordinates'],popup=tweet.user.screen_name.encode('utf-8'))   
            location = geolocator.reverse(tweet.geo['coordinates'],timeout=20)
    if MAPS == "y":
        map_1.create_map(path='maps.html')
    else:
        sys.exit(2)
    credit()

def getopt_menu():

    global ZONE
    global arg_user_search
    global screen_name
    global TAG
    global number
    global check_ZONE
    global MAPS
    global check_USER

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hz:t:u:l:n:ms", ["help", "zone=","tag=","user=","line=","number=","maps=","server="])
    except getopt.GetoptError as err:
        
        print str(err) 
        sys.exit(2)

    for o, a in opts:

        if o in ("-n", "--number"):
             number = a
        elif o in ("-m", "--maps"):
            MAPS = "y"
        elif o in ("-t", "--tag"):
            TAG = a      
        elif o in ("-l", "--line"):
            screen_name = a
            check_USER = "y"
        elif o in ("-u", "--user"):
            arg_user_search = a 
            search_user()
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-z", "--zone"):
            check_ZONE = "y"
            ZONE = a
        elif o in ("-s", "--server"):
            http_run()  
        else:
            print "CoccoDio"

def main():
    getopt_menu()

    if TAG != "x":
        search_tag()

    if check_ZONE != "x":
        search_zone_map()

    if check_USER != "x":
        timeline_user()

if __name__ == "__main__":
    main()

