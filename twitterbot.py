import tweepy, time, sys

argfile = str(sys.argv[1])

consumerkey = 'vC9BtadMgSQ4BAPiQe2hwTd82'
consumersecret = 'ZbBCRqa0ocMjjRHUZRHYJkkfHQjDXc5SNUYEJzcIiz2mYjRPV6'
accesstoken = '1489785306-BR1HufiSLxj5VLs34Wcei0HcVtTLo1CGUf9jW3a'
accesssecret = '06rmBnaBoaZcn0zcSZbi26tr613qtB3x6MMoAMUR6YUSM'
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesssecret)
api = tweepy.API(auth)

filename = open(argfile)
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(60)
 
