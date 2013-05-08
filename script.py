#This code uses PRAW to access the reddit API so it is important to import
import praw
import json


class redditParser:

	def main(self):
		r = praw.Reddit(user_agent='testing out Reddit API through PRAW by /u/ethnographythroway')
		submissions = r.get_front_page(limit=1)
		#r.login()
		redditLinks=[]
		for submissions in submissions:
			print submissions.score, submissions.title, submissions.url, submissions.permalink
			tempRedditLinks = [submissions.score, submissions.title, submissions.url, submissions.permalink]
			redditLinks.extend(tempRedditLinks)
		return redditLinks





redditParser().main()
