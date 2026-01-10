# 04 December 2025
- let's scrape tamil2lyrics.com
- first we need to to initialize the json where the keys are years and values are list of movies (or albums) released that year 
- the values in the list is dict on it's own
- to do that we need to go to https://www.tamil2lyrics.com/movie/page/{i}/ and scrape the movies and it's year (i is the page number ranging from 1 to 295)
- this html tag div class="col-lg-5 col-sm-5 col-xs-5 big-font" contain the movie name
- this html tag div class="col-lg-2 col-sm-2 col-xs-2" contain the year
- initialized the main.py , let's not get the element inside the tag instead let's get the attribute of the tag for the movie name which has it's url
- we want that to avoid confusion

# 07 December 2025
- sucessfully extracted all the movie and it's year data
- the data is in json format and stored in Step_1 directory itself