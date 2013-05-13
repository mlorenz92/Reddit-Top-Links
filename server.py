#!/usr/bin/env python
import web
from script import redditParser

#the render variable is referenced within index so that when te app runs it renders the appropriate information
render = web.template.render('')

#this is just to define what the url ending in / is assigned to, in this case it is index
urls = (
	'/', 'index'
	)

#by importing redditParse from the script file, I am able to gather the appropriate information and use it within the index class
class index:

	#its defined as GET because it is getting the appropriate information
	def GET(self):

		redditLinks= redditParser().main()

		#returning and instance of index under render
		return render.index(redditLinks)


#finally the necessary part of the code that once everything is filled out will run it and send the imformation to index.html
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()   