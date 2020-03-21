import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Setting up page grab basics
positions = ["qb", "rb", "wr", "te"]
weeks = range(1,18)
years = ["2013","2014","2015","2016","2017","2018","2019"]

#setting up headers
headers = {"qb" : ["Week", "Opp", "Score", "QB Rat", "Cmp", "Pa-Att", "Pa-Pct", "Pa-Yds", "Pa-Y/A", "Pa-TD", "Int", "Sacks", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-Lg", "Ru-TD", "Fum", "FumL"],
           "rb" : ["Week", "Opp", "Score", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-Lg", "Ru-TD", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-Lg", "Re-TD", "Fum", "FumL"],
           "wr" : ["Week", "Opp", "Score", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-LG", "Re-TD", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-Lg", "Ru-TD",  "Fum", "FumL"],
           "te" : ["Week", "Opp", "Score", "Rec", "Tgt", "Re-Yds", "Re-Y/R", "Re-LG", "Re-TD", "Ru-Att", "Ru-Yds", "Yu-Y/A", "Ru-Lg", "Ru-TD",  "Fum", "FumL"]}

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
player_guide = {}

for position in positions:
    player_names = []
    player_links = []
    for item in player_lists[position]:
        split_string1 = item.split("(")
        split_string2 = split_string1[0].split(" ")
        player_names.append(split_string2[0]+" "+split_string2[1])
        player_links.append(split_string2[0].lower()+"-"+split_string2[1].lower())
        if position == "qb":
            if "josh-allen" in player_links:
                player_links[player_links.index("josh-allen")] = "josh-allen-qb"
            if "robert-griffin" in player_links:
                player_links[player_links.index("robert-griffin")] = "robert-griffin-iii"
            if "ryan-griffin" in player_links:
                player_links[player_links.index("ryan-griffin")] = "ryan-griffin-qb"
            if "c.j.-beathard" in player_links:
                player_links[player_links.index("c.j.-beathard")] = "cj-beathard"
            if "j.t.-barrett" in player_links:
                player_links[player_links.index("j.t.-barrett")] = "jt-barrett"
            if "john-david" in player_links:
                player_links[player_links.index("john-david")] = "john-david-booty"
        if position == "rb":
            if "le'veon-bell" in player_links:
                player_links[player_links.index("le'veon-bell")] = "leveon-bell"
            if "ronald-jones" in player_links:
                player_links[player_links.index("ronald-jones")] = "ronald-jones-ii"
            if "adrian-peterson" in player_links:
                player_links[player_links.index("adrian-peterson")] = "adrian-peterson-min"
            if "david-johnson" in player_links:
                player_links[player_links.index("david-johnson")] = "david-johnson-rb"
            if "benny-snell" in player_links:
                player_links[player_links.index("benny-snell")] = "benjamin-snell-jr"
            if "jeff-wilson" in player_links:
                player_links[player_links.index("jeff-wilson")] = "jeffery-wilson"
            if "justin-jackson" in player_links:
                player_links[player_links.index("justin-jackson")] = "justin-jackson-rb"
            if "c.j.-prosise" in player_links:
                player_links[player_links.index("c.j.-prosise")] = "cj-prosise"
            if "t.j.-yeldon" in player_links:
                player_links[player_links.index("t.j.-yeldon")] = "tj-yeldon"
            if "d'ernest-johnson" in player_links:
                player_links[player_links.index("d'ernest-johnson")] = "dernest-johnson"
            if "mike-davis" in player_links:
                player_links[player_links.index("mike-davis")] = "mike-davis-rb"
            if "c.j.-anderson" in player_links:
                player_links[player_links.index("c.j.-anderson")] = "cj-anderson"
            if "t.j.-logan" in player_links:
                player_links[player_links.index("t.j.-logan")] = "tj-logan"
            if "damien-harris" in player_links:
                player_links[player_links.index("damien-harris")] = "damien-harris-rb"
            if "buddy-howell" in player_links:
                player_links[player_links.index("buddy-howell")] = "gregory-howell"
            if "de'lance-turner" in player_links:
                player_links[player_links.index("de'lance-turner")] = "delance-turner"
            if "aca'cedric-ware" in player_links:
                player_links[player_links.index("aca'cedric-ware")] = "acacedric-ware"
            if "bryce-love" in player_links:
                player_links[player_links.index("bryce-love")] = "bryce-love-rb"
            if "oren-o'neal" in player_links:
                player_links[player_links.index("oren-o'neal")] = "oren-oneal"
            if "reagan-maui'a" in player_links:
                player_links[player_links.index("reagan-maui'a")] = "reagan-mauia"
            if "j.j.-arrington" in player_links:
                player_links[player_links.index("j.j.-arrington")] = "jj-arrington"
            if "chris-ivory" in player_links:
                player_links[player_links.index("chris-ivory")] = "christopher-ivory"
            if "b.j.-askew" in player_links:
                player_links[player_links.index("b.j.-askew")] = "bj-askew"
        if position == "wr":
            if "michael-thomas" in player_links:
                player_links[player_links.index("michael-thomas")] = "michael-thomas-wr"
            if "d.j.-chark" in player_links:
                player_links[player_links.index("d.j.-chark")] = "dj-chark"
            if "d.j.-moore" in player_links:
                player_links[player_links.index("d.j.-moore")] = "dj-moore-wr"
            if "t.y.-hilton" in player_links:
                player_links[player_links.index("t.y.-hilton")] = "ty-hilton"
            if "marquez-valdes-scantling" in player_links:
                player_links[player_links.index("marquez-valdes-scantling")] = "marquez-valdesscantling"
            if "ted-ginn" in player_links:
                player_links[player_links.index("ted-ginn")] = "ted-ginn-jr"
            if "tre'quan-smith" in player_links:
                player_links[player_links.index("tre'quan-smith")] = "trequan-smith"
            if "n'keal-harry" in player_links:
                player_links[player_links.index("n'keal-harry")] = "nkeal-harry"
            if "j.j.-arcega-whiteside" in player_links:
                player_links[player_links.index("j.j.-arcega-whiteside")] = "jj-arcega-whiteside"
            if "duke-williams" in player_links:
                player_links[player_links.index("duke-williams")] = "duke-williams-wr"
            if "devin-smith" in player_links:
                player_links[player_links.index("devin-smith")] = "devin-smith-wr"
            if "steven-mitchell" in player_links:
                player_links[player_links.index("steven-mitchell")] = "steven-mitchell-jr"
            if "da'mari-scott" in player_links:
                player_links[player_links.index("da'mari-scott")] = "damari-scott"
            if "stanley-morgan" in player_links:
                player_links[player_links.index("stanley-morgan")] = "stanley-morgan-jr"
            if "ryan grant" in player_links:
                player_links[player_links.index("ryan-grant")] = "ryan-grant-wr"
            if "mike-thomas" in player_links:
                player_links[player_links.index("mike-thomas")] = "mike-thomas-wr"
            if "de'anthony-thomas" in player_links:
                player_links[player_links.index("de'anthony-thomas")] = "deanthony-thomas"
            if "moritz-bohringer" in player_links:
                player_links[player_links.index("moritz-bohringer")] = "moritz-boehringer"
            if "t.j.-rahming" in player_links:
                player_links[player_links.index("t.j.-rahming")] = "tj-rahming"
            if "lil'jordan-humphrey" in player_links:
                player_links[player_links.index("lil'jordan-humphrey")] = "liljordan-humphrey"
            if "jon'vea-johnson" in player_links:
                player_links[player_links.index("jon'vea-johnson")] = "jonvea-johnson"
            if "j'mon-moore" in player_links:
                player_links[player_links.index("j'mon-moore")] = "jmon-moore"
            if "equanimeous-st." in player_links:
                player_links[player_links.index("equanimeous-st.")] = "equanimeous-st-brown"
            if "j.j.-jones" in player_links:
                player_links[player_links.index("j.j.-jones")] = "jj-jones"
        if position == "te":
            if "o.j.-howard" in player_links:
                player_links[player_links.index("o.j.-howard")] = "oj-howard"
            if "irv-smith" in player_links:
                player_links[player_links.index("irv-smith")] = "irv-smith-jr"
            if "josh-hill" in player_links:
                player_links[player_links.index("josh-hill")] = "josh-hill-te"
            if "james-o'shaughnessy" in player_links:
                player_links[player_links.index("james-o'shaughnessy")] = "james-oshaughnessy"
            if "nick-o'leary" in player_links:
                player_links[player_links.index("nick-o'leary")] = "nick-oleary"
            if "chris-herndon" in player_links:
                player_links[player_links.index("chris-herndon")] = "chris-herndon-iv"
            if "jason-vander" in player_links:
                player_links[player_links.index("jason-vander")] = "jason-vander-laan"
            if "moritz-bohringer" in player_links:
                player_links[player_links.index("moritz-bohringer")] = "moritz-boehringer"
            if "l.j.-smith" in player_links:
                player_links[player_links.index("l.j.-smith")] = "lj-smith"
            if "brad-st." in player_links:
                player_links[player_links.index("brad-st.")] = "brad-st-louis"
            if "j.p.-foschi" in player_links:
                player_links[player_links.index("j.p.-foschi")] = "jp-foschi"

    if "patrick-ricard" in player_links:
        del player_links[player_links.index("patrick-ricard")]
    if "nick-bellore" in player_links:
        del player_links[player_links.index("nick-bellore")]
    if "rico-gafford" in player_links:
        del player_links[player_links.index("rico-gafford")]
    if "patrick-scales" in player_links:
        del player_links[player_links.index("patrick-scales")]
    if "james-winchester" in player_links:
        del player_links[player_links.index("james-winchester")]
    if "tyler-ott" in player_links:
        del player_links[player_links.index("tyler-ott")]
    if "kevin-mcdermott" in player_links:
        del player_links[player_links.index("kevin-mcdermott")]
    if "clark-harris" in player_links:
        del player_links[player_links.index("clark-harris")]
    if "dillon-gordon" in player_links:
        del player_links[player_links.index("dillon-gordon")]
    if "james-franklin" in player_links:
        del player_links[player_links.index("james-franklin")]

    data[position] = dict(zip(player_names, player_links))
    
    player_guide[position] = dict(zip(player_links, player_names))

    for link in player_links:
      stats_table = pd.DataFrame()
      for year in years:
        print(link)
        page = requests.get("https://www.fantasypros.com/nfl/games/%s.php?season=%s" % (link, year))

        soup = BeautifulSoup(page.content, "html.parser")

        stats = soup.find_all("td")

        all_stats_raw = list(stats)

        all_stats = []

        for stat in all_stats_raw:
            all_stats.append(stat.get_text())

        while "BYE Week" in all_stats:
            del_loc = all_stats.index("BYE Week")
            del all_stats[del_loc]
            del all_stats[del_loc-1]

        del all_stats[-len(headers[position]):]
        
        if len(all_stats) != 0:

          stats_table_dict = {}

          for header in headers[position]:
              stats_table_dict[header] = all_stats[headers[position].index(header)::len(headers[position])]
          stats_table_dict["Year"] = [year]*(len(stats_table_dict["Week"]))

          stats_table_temp = pd.DataFrame(stats_table_dict)

          stats_table_temp["Week"] = stats_table_temp["Week"].str.split(" ").str[1]
          stats_table_temp[["H/A", "Opp"]] = stats_table_temp["Opp"].str.split(" ",expand=True)
          stats_table_temp[["Result", "Score"]] = stats_table_temp["Score"].str.split(", ",expand=True)
          
          for i in range(len(stats_table_temp["Week"])):
            if stats_table_temp.loc[i, "H/A"] == "@":
                stats_table_temp.loc[i,"H/A"] = "Away"
            else:
                stats_table_temp.loc[i,"H/A"] = "Home"

            #setting up headers
            if position == "qb":
                stats_table_temp = stats_table_temp[["Year", "Week", "H/A", "Opp", "Result", "Score", "QB Rat", "Cmp", "Pa-Att", "Pa-Pct", "Pa-Yds", "Pa-Y/A", "Pa-TD", "Int", "Sacks", "Ru-Att", "Ru-Yds", "Ru-Y/A", "Ru-Lg", "Ru-TD", "Fum", "FumL"]]
          print(stats_table_temp)
          stats_table = stats_table.append(stats_table_temp)
          #print(stats_table)
      data[position][player_guide[position][link]] = stats_table
      
    print(data[position])