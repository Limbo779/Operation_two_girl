# 11 Jan
 
- this is gonna be a data hunting brutforce approach
- below are the steps for this entire phase

## Step 1
- so we will have raw data from (this place)[https://metabrainz.org/datasets/postgres-dumps#musicbrainz] where we will extract artist information
- then we will make a neat master json for our American Female singer

## Step 2
- we will get all their songs which had over 100M views and it's youtube link
- and download those video's first 10 sec audio clipping using yt-dl
- neatly organize the all the audio clipping and put those details in master json

## Step 3
- here we will have the actual comparision 
- we will use ML stuff to check the simillarity of the song
- we will put all the songs into a clipping direc and all the clipping will be named as a random hash
- we will map the filename hash in master json