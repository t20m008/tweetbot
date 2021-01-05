# coding: utf-8
#tweetを投稿

import tweepy
import config
import datetime

# 取得した各種キーを格納-----------------------------------------------------
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token= config.access_token_key
access_token_secret = config.access_token_secret

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# ツイート
for i in range(1):
    d = datetime.datetime.now()
    text = d.strftime ("%Y/%m/%d %H:%M:%S")
    api.update_status(text)


#from sympy import prime, sieve
#prime = [i for i in sieve.primerange(1,100)]


# いいね
#api.create_favorite('1335981479239663616')
# 画像投稿
#api.update_with_media('py.png','text tweet with image.','a')
#api.update_with_media(filename = 'py.png',status = 'text tweet with image.',lat = '35.9779', long = '138.9331')

# フォロワー情報取得
#api.followers()
#file = 'followers.csv'
#fileobj = open(file, 'w', encoding = 'utf-8')
#fileobj.write(str(api.followers()))
#fileobj.close()