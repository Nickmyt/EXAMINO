import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep
#Σημείωση πρεπει να βαλεις τα δικα σου κλειδια api kai access_key που εχεις παρει απο το twitter
 
global api
consumer_key = "..."
consumer_secret = "..."
access_key="..."
access_secret="..."
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)
#παιρνει τον λογαριασμο που καταχωρει ο χρηστης 	
USR = input('Insert the First user:')
user = tweepy.api.get_user(USR)
print (user.screen_name)
print (user.followers_count)
 
  
tmp2=[]
number_of_tweets2=10
tweets2 = api.user_timeline(user)
	
	#δημιουργησε ενα array me στοιχεία των Tweet 
tweets_for_csv2 = [tweet.text for tweet in tweets2] # CSV file created 
for j in tweets_for_csv2: 
    #Συνδεουμε τα tweets  με ενα αδειο array
    tmp2.append(j)  
  
    #εκτυπωνουμε τα tweets 
    print(tmp2)
    
#αθροιζει tiw lejeis ton tweet	
sum2= 0
for i in tmp2:
    sum2= sum2 + len(tmp2.split)	
		
#τα ιδια		
USR2 = input("Please insert 2nd user:")		
user2= tweepy.api.get_user(USR2)
print(user2.screen_name)
print(user2.followers_count)

    tmp=[]
    number_of_tweets=10
    tweets = api.user_timeline(screen_name=archillect)
	
	
	 
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
             
            tmp.append(j)  
  
         
        print(tmp) 
        
sum1= 0
for i in tmp:
    sum1= sum1 + len(tmp.split)	
	
#Βρισκουμε το μεγαλυτερο γινομενο
GIMOMENO_XRISTI1= sum2*user.followers_count
GIMOMENO_XRISTI2= sum1*user2.followers_count

if GIMOMENO_XRISTI1>GIMOMENO_XRISTI2:
    print("The first user has the  biggest number"
elif GIMOMENO_XRISTI2>GIMOMENO_XRISTI1:
    print("the second user has the biggest number")	