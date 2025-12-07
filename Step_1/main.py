import requests
from bs4 import BeautifulSoup
import re
import json

main_d={}
for y in range(1,296):
    url = f"https://www.tamil2lyrics.com/movie/page/{y}/"       # this will fetch the raw html of the website                                    
    response = requests.get(url)                                # we then use beautifullsoup4 to get the data we want               
    html = response.text                                        #        

    soup = BeautifulSoup(html, "html.parser") # convert the html we recieved to beautifulsoup format for easy editing
    movie = soup.find_all("div",class_="col-lg-5 col-sm-5 col-xs-5 big-font") # this is where the movie name is present
    movie = BeautifulSoup(str(movie),"html.parser") # we will convert this part of html to beautifulsoup format 

    movies = movie.find_all("a") # the name of the movie is present in this tag
    movie_list=[]
    for i in movies:
        movie_list.append(str(i)) # here we are extracting the content inside the tag but we shall get the attribute to
                                                        # get the link for movie 


    year = soup.find_all("div",class_="col-lg-2 col-sm-2 col-xs-2") # this tag has year
    count=1
    year_list=[]
    for j in year:
        if count >= 4 and count%2==0:
            year_list.append(re.sub(r'<.*?>', '', str(j)))
            count += 1
        else:
            count += 1
    #below will write the movie and it's year into main_d
    for k in range(len(year_list)):
        if int(year_list[k]) in [2024,2025]:
            continue
        elif f'{year_list[k]}' in main_d.keys():
            main_d[f'{year_list[k]}'] += [((f'{movie_list[k]}').split("/"))[4]] 
        else:
            main_d[f'{year_list[k]}'] = [((f'{movie_list[k]}').split("/"))[4]]

    print(f"Page {y} completed")

main_d=dict(sorted(main_d.items(),reverse=True))

# finally we are saving main_d into data.json
with open('year_&_movies.json','w') as file:
    json.dump(main_d,file,indent=4)