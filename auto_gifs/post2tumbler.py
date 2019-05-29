import pytumblr

def post2():         
	consumer_key = 'vQcs1LKKu8gbrybkGAS4fXICmw3ZyAG1y8a2kVbbDluUbH8z0H'
	consumer_secret = 'bHkfLjYgnI4xVoAhJXA6aA1pLBclEExTiaSCxtGWTKvyVtsKcj'
	token_key = 'LtoDUCLDciz8aJbnuT59IqvaSnBtzwC0KnJMB8cGyP1EMtGAwe' 
	token_secret = 'wqQ2L0Rwp47PzN75dMv7sbz6gQuuOtJEY5MeW2ilfMoUrI5XLB'

	client = pytumblr.TumblrRestClient(
		 	consumer_key,
         	consumer_secret,
         	token_key,
         	token_secret
         	)
	client.create_photo('gifandgif', state="published", tags=["gif"], data= "fade.gif")