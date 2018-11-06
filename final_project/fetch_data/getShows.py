import requests
import json

r = requests.get('https://api.tvmaze.com/shows')

content = json.loads(r.content.decode())

f = open('shows.txt', 'w')

for show in content:
    slist = []
    slist.append(str(show['id']))
    slist.append(show['name'])

    strGenre = ''

    if not show['genres']:
        strGenre = "None"
    else:
        for genre in show['genres']:
            if genre != show['genres'][0]:
                strGenre += '|' + genre
            else:
                strGenre += genre
    
    slist.append(strGenre)

    if not show['officialSite']:
        slist.append(show['url'])
    else:
        slist.append(show['officialSite'])
    slist.append(str(show['rating']['average']))
    slist.append(show['image']['medium'])
    slist.append(show['summary'])

    result = '::'.join(slist) + '\n'
    f.write(result)
