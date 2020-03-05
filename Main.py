import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Setting up page grab basics
positions = ["qb", "rb", "wr", "te"]
weeks = range(1,18)
years = ["2013","2014","2015","2016","2017","2018","2019"]

#setting up headers
qb_headers= ["Week", "Opp", "Score", "QB Rat", "Cmp", "Pa-Att", "Pa-Pct", "Pa-Yds", "Pa-Y/A", "Pa-TD", "Int", "Sacks", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-Lg", "Ru-TD", "Fum", "FumL"]
rb_headers= ["Rank", "Player", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-20+", "Ru-TD", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-TD", "Fum", "Games", "FPts", "FPts/G", "Own"]
wr_headers= ["Rank", "Player", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-LG", "Re-20+", "Re-TD", "Ru-Att", "Ru-Yds", "Ru-TD",  "Fum", "Games", "FPts", "FPts/G", "Own"]
te_headers= ["Rank", "Player", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-LG", "Re-20+", "Re-TD", "Ru-Att", "Ru-Yds", "Ru-TD",  "Fum", "Games", "FPts", "FPts/G", "Own"]

#retreiving lists of players
player_lists = {}

for position in positions:

    page = requests.get("https://www.fantasypros.com/nfl/stats/%s.php?year=2019" % position)

    soup = BeautifulSoup(page.content, "html.parser")

    player_list = [player.get_text() for player in soup.find_all("td", class_ = "player-label")]

    player_lists[position] = player_list

#getting data out of the table
#setting up nested dictionaries
data = {}
for position in positions:
    data[position] = dict(zip(player_lists[position], range(1,len(player_lists[position]))))

link_names = []
for item in player_lists["qb"]:
    split_string1 = item.split("(")
    #print(split_string1)
    split_string2 = split_string1[0].split(" ")
    #print(split_string2)
    link_names.append(split_string2[0].lower()+"-"+split_string2[1].lower())

#for item in link_names:
print(link_names[0])

page = requests.get("https://www.fantasypros.com/nfl/games/%s.php?season=2019" % link_names[0])

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all("td")

all_stats_raw = list(stats)

all_stats = []

for stat in all_stats_raw:
    all_stats.append(stat.get_text())

print(all_stats)

stats_table_dict = {}

for header in qb_headers:
    stats_table_dict[header] = all_stats[qb_headers.index(header)::len(qb_headers)]

#print(stats_table_dict)

#print(stats_trimmed)




#set up empty dataframes

#for player in player_lists["qb"]:

#page = requests.get("https://www.fantasypros.com/nfl/stats/qb.php?year=2019&week=1&range=week")
#soup = BeautifulSoup(page.content, "html.parser")
#table_contents = soup.find("tbody")
#stats = table_contents.find_all("td")
#stats_text = [stat.get_text() for stat in stats]
#stats_trimmed = [stats_text[i:i + 18] for i in range(0, len(stats_text), 18)]
#stats_assigned = dict(zip(player_lists["qb"], stats_trimmed))

#emptydfdict = {}
#for i in qb_headers:
    #emptydfdict[i] = ["a"]

#emptydf = pd.DataFrame(emptydfdict)

#print(emptydf)