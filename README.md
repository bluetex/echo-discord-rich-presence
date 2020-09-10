This project will allow you to produce Rich Presence updates to your Discord user account while you're in Echo VR games.
It's able to see Public and Private matches, the last scored (mouse over small disc icon), and game score (mouse over large disc icon). It will also show the game clock left and will stop when game play stops. 

Echo VR Arena support only right now.


# Requirements
Python3
pip install pypresence

other modules used are: 
import time, json
from pypresence import Presence
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

On your computer, you must have Discord (duh), Echo VR (again duh)
Once both are running, click the discord_rich.py to start updating rich presence in discord.  This will ONLY update every 15 seconds.

