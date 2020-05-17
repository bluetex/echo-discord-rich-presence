This project will allow you to produce Rich Presence updates to your Discord user account while you're in Echo VR games.
It's able to see Public and Private matches, the last scored (mouse over small disc icon), and game score (mouse over large disc icon). It will also show the game clock left and will stop when game play stops. 


# Requirements
Python3
pip install pypresence

other modules used are: 
import time, os, pycurl, re, json
from pypresence import Presence
from io import BytesIO
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

Discord APP Dev
Go to https://discord.com/developers/applications 
Register a new application
-- populate your ClientID in the discord_rich.py on line 12
-- on the "Art Assets" > "Rich Presence Assets" section of discord applications... add 3 images from this repo: disc, disc-orange, disc-blue

On your computer, you must have Discord (duh), Echo VR (again duh)
Once both are running, click the discord_rich.py to start updating rich presence in discord.  This will ONLY update every 15 seconds.

