import requests

URL = "http://www.omdbapi.com/?t=My+Hero+Academia%3A+Heroes+Rising&apikey=a7ad1aed"

info = {
    "Actors": "Kiyotaka Furushima, Tasuku Hatanaka, Ryô Hirohashi, Yoshimasa Hosoya",
    "Director": "Kenji Nagasaki",
    "Genre": "Animation, Action, Adventure, Comedy, Family, Sci-Fi",
    "Language": "Japanese",
    "Plot": "A group of youths aspiring to become professional superheroes, fight in a world full of people with abilities, also known as quirks. Deku and his fellow classmates from Hero Academy face Nine, the strongest villain yet.",
    "Release Date": "26 Feb 2020",
    "Runtime": "104 min",
    "Title": "My Hero Academia: Heroes Rising"
}


res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(res)