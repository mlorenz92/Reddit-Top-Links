#import web
import json
from script import redditParser



class info:

	def GET(self):
		redditLinks= redditParser()

info().GET()