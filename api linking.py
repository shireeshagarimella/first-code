import requests
import sys


r = requests.get(" http://www.omdbapi.com/?t={}&apikey=*********".format(sys.argv[1]))
dic = r.json()
print(dic)
print(dic['Ratings'])
rating = [i for i in dic['Ratings'] if (i['Source'] == 'Rotten Tomatoes')]
print(rating)
print(rating[0]['Value'])
