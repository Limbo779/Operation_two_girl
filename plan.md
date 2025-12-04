## Phase 1 (Web Scraping)
- first let's scrape the tamil lyrics website to find our target 
- if not found in the lyrics website then we may plan the next phase
- in this phase we will search for the songs using the know information (like female vocal and iconic retha ponnu lyrics)

### implementation plan
- let's scrap tamil2lyrics.com

### Step 1
- this will be done using scrap_movies.py
- first we should get all the movies (or album) names released in or before 2023
- store them in json file with year as key and value as list containing all the movies (or album) released that year
- then sort them in decending order from 2023

### Step 2
- go to individiual movies and get all their songs info 
- and store it in json
- each value is a list of movies (or album) released that year so make the enteries in the list as seperate dictionary 
- and that dictionary contain the movie's (or album's) songs

### Step 3
- finally extract the actual lyrics from the songs 
- and store it in the song's directory as this html (example given below) 
- so each movie will have the list of songs in a list where each list is dict and that contain this lyrics html

ex lyrics html :

<div id="English" class="tabcontent" style="display: block;">
<p style="text-align: center;"><strong><span style="color: #03579c;">Singers </span></strong><strong><span style="color: #03579c;">:</span></strong> Ezhil Durai and Uma Balu</p>
<p style="text-align: center;"><strong><span style="color: #b50202;">Music by :</span></strong> Ezhil Durai</p>
<p style="text-align: center;"><span style="color: rgb(45 50 199);"><strong>Lyrics by :</strong></span> Uma Balu</p>
<p style="text-align: center;"><strong>Dialogue :</strong> ……………..</p>
<p style="text-align: center;"><strong>Female :</strong> Va….. nam<br>
Mannil vanthathe…<br>
Oru mannan nenjile…<br>
Thiru manjam kondathe…<br>
En kannaana kannaa…</p>
<p style="text-align: center;"><strong>Male :</strong> Tho…lil<br>
Thottil kattave…<br>
Ada thulli vanthathe…<br>
Oru thanga mayile…<br>
En kannaana kanne…</p>
<p style="text-align: center;"><strong>Female :</strong> Va….. nam<br>
Mannil vanthathe…<br>
Oru mannan nenjile…<br>
Thiru manjam kondathe…<br>
En kannaana kannaa…</p>
<p style="text-align: center;"><strong>Male :</strong> Tho…lil<br>
Thottil kattave…<br>
Ada thulli vanthathe…<br>
Oru thanga mayile…<br>
En kannaana kanne…</p>
<p style="text-align: center;"><strong>Male :</strong> O…<br>
En kanave..<br>
En kalave…<br>
En kathire…</p>
<p style="text-align: center;"><strong>Female :</strong> O…<br>
En urave..<br>
En unarve…<br>
En uyire…</p>
<p style="text-align: center;"><strong>Male :</strong> Haaa<br>
Poo…. Maalai<br>
Thedi varum…<br>
Isai paadi varum…<br>
Asainthaadi varum…<br>
Manam oorkolam pokum…</p>
<p style="text-align: center;"><strong>Female :</strong> Naan…. unnai<br>
Kaathirunthen…<br>
Ethir paarthirunthen…<br>
Ingu kandukonden…<br>
Ini jenmangal vaazhum…</p>
<p style="text-align: center;"><strong>Female :</strong> Va….. nam<br>
Mannil vanthathe…<br>
Oru mannan nenjile…<br>
Thiru manjam kondathe…<br>
En kannaana kannaa…</p>
<p style="text-align: center;"><strong>Male :</strong> Tho…lil<br>
Thottil kattave…<br>
Ada thulli vanthathe…<br>
Oru thanga mayile…<br>
En kannaana kanne…</p>
<div class="styleIt" style="margin-top: 25px;"> <lite-youtube videoid="WpxdsL3zghA?si=yrfOVQx5DUzF" title="Play: Video"></lite-youtube></div></div>

### Step 4 
- now we got this huge database of tamil song's lyrics , we can finally start searching for target
- we may reduce the possible candidate like excluding pure male vocal , and lyrics with "ponnu","இரட்டை"
- finally we can manually check the final set of candidates (in the hope that there will be few candidates)