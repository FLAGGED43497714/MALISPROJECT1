import datetime
import schedule
from os import path
import time
import numpy as np
from func_search_hash_weed import requestTweets

path_matchlist = "matchlist.csv"

matchlist = np.genfromtxt(path_matchlist, dtype=str, delimiter=',')

def job():
    global matchlist
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for indexMatch in range(len(matchlist)):
        runTime = matchlist[indexMatch][0]+" "+matchlist[indexMatch][1]
        if date == str(runTime):
            print(matchlist[indexMatch])
            daymonth = str(matchlist[indexMatch][0])
            daymonth = daymonth.replace(".", "_")
            language = matchlist[indexMatch][4]
            team1 = matchlist[indexMatch][2]
            team2 = matchlist[indexMatch][3]

            requestTweets(team1=team1, team2=team2, daymonth=daymonth, language=language)

            

schedule.every(0.01).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)