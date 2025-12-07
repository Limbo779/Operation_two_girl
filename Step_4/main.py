import json
from bs4 import BeautifulSoup
import re
import itertools

def check_candidate(html_content):
    """
    Scans HTML lyrics. 
    Returns True if it finds the phrase "Retha/Otha + Ponnu" (Tanglish variants).
    """
    
    # 1. PARSE HTML & CLEAN TEXT
    if isinstance(html_content, str):
        soup = BeautifulSoup(html_content, 'html.parser')
    else:
        soup = html_content

    # Replace <br> with spaces to ensure words don't merge (e.g., "end<br>start")
    for br in soup.find_all("br"):
        br.replace_with(" ")

    # Get clean text, lowercase for insensitive matching
    text = soup.get_text(separator=' ', strip=True).lower()

    # ---------------------------------------------------------
    # THE "RETHA/OTHA PONNU" REGEX
    # ---------------------------------------------------------
    # This pattern catches:
    # Prefix: retha, ratha, retta, rettai, rattai (Double/Blood variants)
    #         otha, othai, oththa, otrai, otthai (Single variants)
    # Anchor: ponnu, pennu, penne, kannu (Girl/Eye variants)
    
    # \b checks for word boundaries
    # r[aeiouy]t+ : Starts with r + vowel + t (matches ret, ratt, rott)
    # h* : Optional h (retha vs retta)
    # [aeiouy]* : Optional ending vowel (retha vs rethai)
    
    pattern = r'\b(r[aeiouy]t+h*[aeiouy]*|o[aeiou]t+h*[aeiouy]*)\s+(ponnu|pennu|penne|kannu)\b'

    # Search for the pattern
    match = re.search(pattern, text)

    # ---------------------------------------------------------
    # RESULT
    # ---------------------------------------------------------
    # If ANY match is found, return True immediately.
    if match:
        return True
        
    return False

list_retha = ["retha", "ratha", "raththa", "rattha", "retta", "rettai", "rettha"]
list_otha = ["otha", "othai", "oththa", "otrai", "ottrai", "orra"]
list_ponnu = ["ponnu", "ponu", "pona", "pennu", "penne", "penn", "ponna"]
combinations = list(itertools.product(list_retha, list_otha, list_ponnu))


def check_song_candidate(html_content):
    global list_otha,list_ponnu,list_retha,combinations
    text = str(html_content).lower() 
    if "female :" not in text and ("male :" in text):
        return False
    else:
        for i in combinations:
            combo = list(i)
            if (combo[0] in text) and (combo[1] in text) and (combo[2] in text):
                return True
        return False

year_list={
    1:[str(y) for y in range(1941,1950+1)],
    2:[str(y) for y in range(1951,1960+1)],
    3:[str(y) for y in range(1961,1970+1)],
    4:[str(y) for y in range(1971,1980+1)],
    5:[str(y) for y in range(1981,1990+1)],
    6:[str(y) for y in range(1991,2000+1)],
    7:[str(y) for y in range(2001,2005+1)],
    8:[str(y) for y in range(2006,2010+1)],
    9:[str(y) for y in range(2011,2018+1)],
    10:[str(y) for y in range(2019,2023+1)]
}

candidates=[]

for i in range(1,11):
    data_loc=f'/home/limbo/Desktop/Random Learning/Operation_two_girl/Step_3/songs_&_lyrics{i}.json'
    main_d = {}
    with open(data_loc,'r') as file:
        main_d = json.load(file)

    for j in year_list[i]:
        print(f"==========Started {j} year==========")
        if j in list(main_d.keys()):    
            movies=main_d[j]
        else:
            continue
        for k in range(len(movies)):
            movie=movies[k]
            movie_name=list(movie.keys())[0]
            print(f"=======Checking {movie_name} =======")
            songs=movie[movie_name]
            for ij in range(len(songs)):
                song=songs[ij]
                song_name=list(song.keys())[0]
                lyrics=song[song_name]    
                lyrics = BeautifulSoup(lyrics,"html.parser")
                if check_song_candidate(lyrics):
                    print(f"\n\n\n{song_name} PASSED\n\n\n")
                    candidates.append(song_name)
                else:
                    print(f" {song_name} failed\n")
                    continue
    
print()
print(candidates)

d={}
d['1']=candidates
with open('candidates.json','w') as f:
    json.dump(d,f,indent=4)