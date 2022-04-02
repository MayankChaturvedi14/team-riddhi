from dataclasses import replace
from googleapiclient.discovery import build
from googletrans import Translator
api_key = 'AIzaSyBBLm808s_AZJEaDG62LdEmOwz38OEOYR0'

def video_comments(video_id):
	count = 0
	replies = []
	youtube = build('youtube', 'v3',developerKey=api_key)
	video_response=youtube.commentThreads().list(part='snippet,replies',videoId=video_id).execute()
	while video_response:
		for item in video_response['items']:
			comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
			replies.append(comment)
		if 'nextPageToken' in video_response and count<20:
			video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					videoId = video_id
				).execute()
			count+=1
		else:
			break
	return replies


def translatebaazi(text, src="auto", dest="dutch"):
    text = text
    dest = dest
    src = src
    Trans = Translator()
    Trans1 = Trans.translate(text, src = src, dest = dest)
    return Trans1.text

    


