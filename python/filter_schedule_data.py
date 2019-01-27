import json
import datetime
import requests

# get NBA schedule data as JSON
year = '2018'
r = requests.get('https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/' + year + '/league/00_full_schedule.json')
json_data = r.json()

# prepare output files
fout = open("filtered_schedule.csv", "w")
fout.writelines('GameDate, GameID, Visitor, Home, HomeWin')

current_dt = datetime.datetime.now() 

# loop through each month/game and write out stats to file
for i in range(len(json_data['lscd'])):
    for j in range(len(json_data['lscd'][i]['mscd']['g'])):
        gamedate = json_data['lscd'][i]['mscd']['g'][j]['gdte']
        gamedate_dt = datetime.datetime.strptime(gamedate, "%Y-%m-%d")

        game_id = json_data['lscd'][i]['mscd']['g'][j]['gid']
        visiting_team = json_data['lscd'][i]['mscd']['g'][j]['v']['ta']
        home_team = json_data['lscd'][i]['mscd']['g'][j]['h']['ta']

        fout.write('\n' + gamedate +','+ game_id +','+ visiting_team +','+ home_team)

        # don't access scores for games that haven't been played yet
        if(gamedate_dt < current_dt):  
            home_team_won = json_data['lscd'][i]['mscd']['g'][j]['h']['s'] > json_data['lscd'][i]['mscd']['g'][j]['v']['s']
            fout.write(','+ str(home_team_won))

        
fout.close()
r.close()
