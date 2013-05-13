#This code uses PRAW to access the reddit API so it is important to import
import praw
import json



class redditParser:

	def main(self):
		r = praw.Reddit(user_agent='testing out Reddit API through PRAW by /u/ethnographythroway')
		submissions = r.get_front_page(limit=1)
		#You can log in below by simply typing in your ('username','password') and the wrapper will automatically work with your
		#personalized reddit account to deliver the top post that is unique to your account
		#r.login()

		#using a for loop to loop through the submissions and get all of the propper data. In order to be displayed properly
		#they have to be concatinated strings, otherwise JSON views them as JSON objects and attempts to display them as so.
		for submissions in submissions:
			#print submissions.score, submissions.title, submissions.url, submissions.permalink
			redditLinks = "Score: " + str(submissions.score) + ". " + str(submissions.title) + " " + str(submissions.url) + " " + str(submissions.permalink)

		return redditLinks

