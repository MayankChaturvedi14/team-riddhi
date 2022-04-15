from unittest import main
from googleapiclient.discovery import build
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
api_key = 'AIzaSyBBLm808s_AZJEaDG62LdEmOwz38OEOYR0'

def video_comments(video_id):
	replies = []
	youtube = build('youtube', 'v3',developerKey=api_key)
	video_response=youtube.commentThreads().list(part='snippet,replies',videoId=video_id).execute()
	for item in video_response['items']:
		comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
		replies.append(comment)			
	return replies


def translatebaazi(text):
    text = text
    Trans = Translator()
    Trans1 = Trans.translate(text, src = "auto", dest = "dutch")
    return Trans1.text

    
def sentiment_scores(sentence):
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	if sentiment_dict['compound'] >= 0.05 :
		return("Positive")
	elif sentiment_dict['compound'] <= - 0.05 :
		return("Negative")

	else :
		return("Neutral")
