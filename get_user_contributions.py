#!/usr/bin/env python3

#!/usr/bin/python3

"""
    get_usercontribs.py

    MediaWiki API Demos
    Demo of `Usercontribs` module: List user contributions.

    MIT License
"""
import sys
import os
import requests

S = requests.Session()

def get_usercontrib_details(language, wikisite,username,start_date, end_date):

    URL = "https://" +language +  "." + wikisite + ".org/w/api.php"

    PARAMS = {
       "uclimit" : 500,
       "action": "query",
       "format": "json",
       "list": "usercontribs",
       "ucuser": username,
       "ucstart": start_date + " 00:00:00",
       "ucend": end_date + " 23:59:59",
       "ucdir": "newer",
       "ucprop": "ids|title|sizediff|size|timestamp",
       }

    csv_content = []

    while True:

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        print(DATA)
        USERCONTRIBS = DATA["query"]["usercontribs"]
        for uc in USERCONTRIBS:
#            print(uc)
            csv_line = uc["title"] + "," + str(uc["size"]) + "," + str(uc["sizediff"]) +"," + uc["timestamp"]
            csv_content.append(csv_line)

        if "continue" in DATA:
            PARAMS["uccontinue"] = DATA["continue"]["uccontinue"]
            PARAMS["continue"] = DATA["continue"]["continue"]
 #           print(DATA)

            USERCONTRIBS = DATA["query"]["usercontribs"]
            for uc in USERCONTRIBS:
  #              print(uc)
                csv_line = uc["title"] + "," + str(uc["size"]) + "," + str(uc["sizediff"]) +"," + uc["timestamp"] 
                csv_content.append(csv_line)

        else:
            break

    return csv_content


language = sys.argv[1]
wikisite  = sys.argv[2]
username = sys.argv[3]
start_date = sys.argv[4]
end_date = sys.argv[5]
#csv_data = get_usercontrib_details("ta","wikisource","Tshrinivasan","2015-03-06","2015-03-06")
csv_data = get_usercontrib_details(language,wikisite,username,start_date,end_date)

if os.path.isfile('./data/usercontrib_data.csv'):
	os.remove("./data/user_contrib.csv")

usercontrib_file = open('./data/user_contrib.csv','w')
usercontrib_file.write("page,size,sizediff,timestamp" + "\n")
for line in csv_data:
    print(line)
    usercontrib_file.write(line + "\n")
usercontrib_file.close()



query_details = open('data/query_details.html','w')
query_details.write('<link href="../css/bootstrap.min.css" rel="stylesheet">\n')
query_details.write("<p>Wikisite = https://"+language+"."+wikisite+".org &emsp; Username = " + username + "&emsp; Start Date = " + start_date + "&emsp; End Date = " + end_date +"</p>")
query_details.close()

