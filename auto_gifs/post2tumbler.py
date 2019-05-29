import pytumblr

def post2():         
	consumer_key = 'xxxxxxx'
	consumer_secret = 'xxxxxxx'
	token_key = 'xxxxxxx' 
	token_secret = 'xxxxxxx'

	client = pytumblr.TumblrRestClient(
		 	consumer_key,
         	consumer_secret,
         	token_key,
         	token_secret
         	)
	client.create_photo('gifandgif', state="published", tags=["gif"], data= "fade.gif")
