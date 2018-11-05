import requests
import json

r = requests.get('https://api.tvmaze.com/shows')

content = json.loads(r.content.decode())

f = open('shows.txt', 'w')

for show in content:
    sid = show['id']
    sname = show['name']

    f.write(str(sid) + ',' + sname + '\n')
