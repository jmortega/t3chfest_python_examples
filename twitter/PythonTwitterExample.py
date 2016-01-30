# -*- encoding: utf-8 -*-
'''
Nota:
Para crear una aplicación cliente en Twitter, es necesario contar con una cuenta de usuario valida, la cual se puede crear desde el centro de desarrolladores: https://apps.twitter.com/
Todos los servicios de la API Rest de Twitter se encuentran disponibles en el siguiente enlace: https://dev.twitter.com/rest/public
Resultan especialmente interesantes aquellos servicios que permiten realizar búsquedas contra Twitter utilizando hashtags o filtros de búsqueda simples. Dichos servicios se encuentran disponibles en los siguientes enlaces:  #https://dev.twitter.com/rest/public/search   #https://dev.twitter.com/rest/reference/get/search/tweets
'''


import twitter
import sqlite3
import csv
import json

apiTwitter = twitter.Api(consumer_key="cRz70QuhNCGvFMlFHy3ARekMY", consumer_secret="WBdhkig3nZ5DTFZS0UKN0k2HnmwgbQ39xQRN6kWzeE2DfvYztg", access_token_key="201832916-lLrZ1Qw4D5zQZii0k3RgOxuY0ymnyJfPkQSXu1sc", access_token_secret="YLKNQfqIfgN9PK8IwYBd3TsSI3fkl1pfXgUkM3aP9Xgl8")
#accountFriends = [account.name for account in apiTwitter.GetFriends()]
#accountFollowers = [account.name for account in apiTwitter.GetFollowers()]

#print "\nFriends:"
#for friend in accountFriends:
#    print friend.encode('utf-8')

#print "\nFollowers"
#for follower in accountFollowers:
#    print follower

print "\nCredentials:"

credentials = apiTwitter.VerifyCredentials()
print credentials

print "\nTimeline:"

timeline = apiTwitter.GetUserTimeline('jmortegac')
print [s.text for s in timeline]

print "\nTweets: "
query = apiTwitter.GetSearch("#T3chFest2016", count=50)

twitter_results = []

for result in query:
    tweet = {}
    print "Tweet: %s " %(result.text.encode('utf-8'))
    tweet['text'] = result.text.encode('utf-8')
    print "Creation date: %s " %(result.created_at)
    tweet['date'] = result.created_at.encode('utf-8')
    print "Favs count: %d" %(result.favorite_count)
    tweet['favorite_count'] = result.favorite_count
    print "Language: %s" %(result.lang)
    tweet['lang'] = result.lang.encode('utf-8')
    print "Retweets count: %d" %(result.retweet_count)
    tweet['retweet_count'] = result.retweet_count
    print "Account: %s" %( result.user.screen_name )
    tweet['account'] = result.user.screen_name.encode('utf-8')
    print "\n"
    twitter_results.append(tweet)
    
connection = sqlite3.connect('db.sqlite3')
print "Database db.sqlite3 created succesfully"
cursor = connection.cursor()

connection.execute("create table if not exists  TwitterMessages(id integer primary key autoincrement, message varchar(140), account varchar(20),favs integer,retweets integer,langTweet varchar(5), dateMessages varchar (30) );")

query = apiTwitter.GetSearch("#T3chFest2016", count=50)

insert = "insert into TwitterMessages(message, dateMessages, favs, langTweet, retweets, account) values(?,?,?,?,?,?)"

for result in query:
        cursor.execute(insert, (result.text, result.created_at, result.favorite_count, result.lang, result.retweet_count, result.user.screen_name))

connection.commit()

outfile = open('twitter.json','wb')
	
for twitter_result in twitter_results:
    line = json.dumps(twitter_result,sort_keys=True, indent=4) + "\n"
    outfile.write(line)
	
with open('twitter.csv' ,'wb') as csvfile:
    twitter_writer = csv.writer(csvfile)
    for result in twitter_results:
        twitter_writer.writerow([str(result['text']),str(result['date']),str(result['favorite_count']),str(result['lang']),str(result['retweet_count'])])