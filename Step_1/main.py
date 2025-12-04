import requests
from bs4 import BeautifulSoup
import re
import json

main_d={}
for y in range(2,296):
    url = f"https://www.tamil2lyrics.com/movie/page/{y}/"       # this will fetch the raw html of the website                                    
    response = requests.get(url)                                # we then use beautifullsoup4 to get the data we want               
    html = response.text                                        #        

    soup = BeautifulSoup(html, "html.parser")
    movie = soup.find_all("div",class_="col-lg-5 col-sm-5 col-xs-5 big-font")
    movie = BeautifulSoup(str(movie),"html.parser")

    movies = movie.find_all("a")
    movie_list=[]
    for i in movies:
        movie_list.append(re.sub(r'<.*?>', '', str(i)))


    year = soup.find_all("div",class_="col-lg-2 col-sm-2 col-xs-2")
    count=1
    year_list=[]
    for j in year:
        if count >= 4 and count%2==0:
            year_list.append(re.sub(r'<.*?>', '', str(j)))
            count += 1
        else:
            count += 1
    
    for k in range(len(year_list)):
        if f'{year_list[k]}' in main_d.keys():
            main_d[f'{year_list[k]}'] += [((f'{movie_list[k]}').lower()).replace(" ","-")]
        else:
            main_d[f'{year_list[k]}'] = [((f'{movie_list[k]}').lower()).replace(" ","-")]

    print(f"Page {y} completed")

with open('data.json','w') as file:
    json.dump(main_d,file,indent=4)