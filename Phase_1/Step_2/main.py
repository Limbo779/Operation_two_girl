import requests
from bs4 import BeautifulSoup
import re
import json


data_loc='/home/limbo/Desktop/Random Learning/Operation_two_girl/Step_1/year_&_movies.json'
main_d = {}
with open(data_loc,'r') as file:
    main_d = json.load(file)

def get_html(s):
    url = f"https://www.tamil2lyrics.com/movies/{s}/"
    response = requests.get(url)              
    html = response.text
    return html

def get_songs(html):
    soup = BeautifulSoup(html, "html.parser") # convert the html we recieved to beautifulsoup format for easy editing
    song = soup.find_all("div",class_="col-lg-6 col-sm-6 col-xs-6") # this is where the movie name is present
    song = BeautifulSoup(str(song),"html.parser") # we will convert this part of html to beautifulsoup format 

    song = song.find_all("a") # the name of the movie is present in this tag
    song_list=[]
    for i in song:
        song_list.append(str(i))
    return song_list

year_list = main_d.keys()

for i in year_list:
    print(f"Started with year {i}")
    movies=main_d[i]
    m=[]
    for j in movies:
        html=get_html(j)
        song_list = get_songs(html)
        d={}
        d[f'{j}']=[]
        for k in range(len(song_list)):
            d[f'{j}'] += [((f'{song_list[k]}').split("/"))[4]]
        m.append(d)
        print(f"Finished {j}\n")
    main_d[i]=m

with open('movies_&_songs.json','w') as file:
    json.dump(main_d,file,indent=4)

print("=========================Done Done Done=========================")
