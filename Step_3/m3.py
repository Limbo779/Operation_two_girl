import requests
from bs4 import BeautifulSoup
import re
import json
import traceback

data_loc='/home/limbo/Desktop/Random Learning/Operation_two_girl/Step_2/movies_&_songs.json'
main_d = {}
with open(data_loc,'r') as file:
    main_d = json.load(file)

def get_html(s):
    url=f'https://www.tamil2lyrics.com/lyrics/{s}/'
    response = requests.get(url)              
    html = response.text
    return html

def get_lyrics(html):
    soup = BeautifulSoup(html, "html.parser") # convert the html we recieved to beautifulsoup format for easy editing
    lyrics = soup.find_all("div",class_="tabcontent",id='English') # this is where the movie name is present
    #lyrics = BeautifulSoup(str(lyrics),"html.parser") # we will convert this part of html to beautifulsoup format 

    return str(lyrics)
try:
    year_list=[str(y) for y in range(1961,1970+1)]
    for i in year_list:
        if i not in main_d.keys():
            continue
        else:
            print(f'======================Started year {i}======================\n')
            movies=main_d[i]
            for j in movies:
                movie=list(j.keys())[0]
                songs=j[movie]
                for k in range(len(songs)):
                    html=get_html(songs[k])
                    lyrics=get_lyrics(html)
                    d={}
                    d[songs[k]]=lyrics
                    songs[k]=d
                    print(f'Extracted    {list(songs[k].keys())[0]} lyrics\n')
                print(f'============Finished {movie}============\n')

    with open('songs_&_lyrics3.json','w') as file:
        json.dump(main_d,file,indent=4)
except:
    with open('songs_&_lyrics3.json','w') as file:
        json.dump(main_d,file,indent=4)
    traceback.print_exc()