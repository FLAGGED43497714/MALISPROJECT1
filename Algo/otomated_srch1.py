import datetime
import schedule
from os import path
import time
import numpy as np
from func_search_hash_weed import requestTweets
import pandas as pd

path_matchlist = "epl-2021-GMTStandardTime.csv"


matchlist = pd.read_csv(path_matchlist, delimiter=',', dtype=str)

def job():
    global matchlist
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    print('date = '+str(date))
    for indexMatch in range(len(matchlist)):
        runTime = matchlist['Date'][indexMatch]
        if date == str(runTime):
            print('Running ...')
            daymonth = str(matchlist['Date'][indexMatch][:10]) #:10 => juste la date et pas l'heure 
            daymonth = daymonth.replace("/", "_")
            if matchlist['Div'][indexMatch] == 'E0' :
                language = 'en'
            if matchlist['Div'][indexMatch] == 'SP1' :
                language = 'es'
            if matchlist['Div'][indexMatch] == 'FR1' :
                language = 'fr'
            if matchlist['Div'][indexMatch] == 'AL1' :
                language = 'de'
            if matchlist['Div'][indexMatch] == 'IT1' :
                language = 'it'
            


            team1 = matchlist['Home Team'][indexMatch]
            team2 = matchlist['Away Team'][indexMatch]

            requestTweets(team1=team1, team2=team2, daymonth=daymonth, language=language, nb_tweets=1000)



schedule.every(1).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(59)