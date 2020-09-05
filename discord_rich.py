import time, os, pycurl, re, json
from io import BytesIO
from pypresence import Presence
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#### set up reusable values pre loop
client_id = '707734354910249054'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Checking Status...", details="Logging in.", large_image="disc", large_text="Echo Disk"))

req = Request("http://127.0.0.1:6721/session")

while True:
    while True:
        try:
            response = urlopen(req)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            time.sleep(1)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)        
            time.sleep(1)
        else:
            # everything is fine
            break
        
    #print("We broke free")

#### api only allows updates every 15 seconds
#time.sleep(15) 
 #   while True:  # The presence will stay on as long as the program is running

    #### prevent null status for details field
        new_status = "Checking status"    

    #### save output to out.json curl the local api for the json payload
    with open('out.json', 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://127.0.0.1:6721/session')
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()    
        f = open('out.json', 'r')
        content = f.read()
        f.close()
        
#### we open the file to grab values        
    f = open('out.json',)
    data = json.load(f)

#### grab values from the json payload (values are inside data[""]
#### not in game session data here
    match_type = data["match_type"]
    if match_type == "Social_2.0":
        game_mode = "lobby"
    else: 
        game_mode = "match"
    
#### in session data here
    if game_mode == "match":
        game_clock = data["game_clock"]
    
        clock = data["game_clock_display"]
    
        #### we have to take the underscores off the match type and status field (requires a new var)
        status = data["game_status"]
        new_status = status.replace("_", " ").title()
        
        match_type = data["match_type"]
        new_game = match_type.replace("_", " ")
        game = new_game.replace("Echo ", "")
    
    #### we have to convert the points values from int to str
        blue = data["blue_points"]
        bluescore = str(blue)
        orange = data["orange_points"]
        orangescore = str(orange)
    
        lastscore = data["last_score"]
        person_scored = lastscore["person_scored"]
        team = lastscore["team"]
    
    #### calculate the color of the small disc (who scored etc)    
    
        if team == "blue": 
            disc_color = "disc-blue"
        else: 
            disc_color = "disc-orange"
      
      
    #### pick up time in epoch
        seconds = time.time()
    #### calculate the game clock + now to display the end of game countdown
        game_time = (seconds + game_clock)
      
        if game == "Lobby": 
            person_scored = "none"
            disc_color = "disc"
            game_time = "1"
        else: 
            person_scored = lastscore["person_scored"]
        if blue == 0 and orange == 0:
            disc_color = "disc"
        print(disc_color)
      
    
    #### check values here
        if new_status == "":
            new_status = "stand by"
    #### calculate in game clock
            in_game_clock = ""
    #### end match data
    #### update rich presense
    if game_mode == "match" and new_status == "Playing":
        print(RPC.update(state=game, details=new_status, large_image="disc", large_text="Score: blue-" + bluescore + " orange-" + orangescore, small_image=disc_color, small_text="Last score by : " + person_scored, end=game_time  ))  # Set the presence
    elif game_mode == "match" and new_status != "Playing":
        print(RPC.update(state=game, details=new_status, large_image="disc", large_text="Score: blue-" + bluescore + " orange-" + orangescore, small_image=disc_color, small_text="Last score by : " + person_scored  ))
    else:
        print(RPC.update(details="In Lobby", large_image="disc", large_text="Echo Disk"))

####close the connections
    f.close()
        
    
    time.sleep(15) # Can only update rich presence every 15 seconds
