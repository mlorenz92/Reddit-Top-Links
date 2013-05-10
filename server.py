#!/usr/bin/env python
import web
#import json
#import re
from script import redditParser

render = web.template.render('')

urls = (
	'/', 'index'
	)

class index:

	def GET(self):

		redditLinks= redditParser().main()  

		return render.index(redditLinks)

class links:

	def GET(self):
		
		redditLinks= redditParser().main()


#info().GET()

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()   