Reddit Top Links
================

A Reddit Scrapper that works with PRAW and the Reddit API to collect the top links.

### How To Use

This project works best when used within its own virtual environment, so as to make sure the dependencies don't interact with previously installed dependencies and projects. In addition virtualenvwrapper will need to be installed because it makes switching between environments easier

Virtualenv can be installed by running from the command line.
	
	$ pip install virtualenv

Once downloaded install virtualenvwrapper by running from the commnand line.

	$ pip install virtualenvwrapper

Once both are downloaded you will need to create your virtual environment. It can be named whatever you want, just make sure you remember what it is called. For the purposes of this project I have named it 'reddit'. Cd to the directory where this project will be located and run. 

	$ mkvirtualenv reddit

Now you can intall the proper dependencies in this virtual environment so it doesn't interact with other projects you may be running. 

### How To Install Dependencies

All of the dependencies for this project can be installed via pip. Pip is very easy to install. If you don't have pip installed you can either download it directly from [pip](http://www.pip-installer.org/en/latest/installing.html) or if you have easy_install it can be installed by runnning 'easy_install pip'. This project requires PRAW and Web.py as dependencies and these can easily be installed via pip. 

- [praw](https://github.com/praw-dev/praw)

In order to install praw just run from the command line.


	$ pip install praw


- [web.py](http://webpy.org/)

In order to install web.py just run from the command line.

	$ sudo easy_install web.py

or you can download it via git

	git clone git://github.com/webpy/webpy.git
	ln -s `pwd`/webpy/web .

