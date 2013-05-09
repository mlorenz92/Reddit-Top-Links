Reddit Top Links
================

A Reddit Scrapper that works with PRAW and the Reddit API to collect the top links.

### How To Install Dependencies

All of the dependencies for this project can be installed via pip. Pip is very easy to install. If you don't have pip installed you can either download it directly from [pip](http://www.pip-installer.org/en/latest/installing.html) or if you have easy_install it can be installed by runnning 'easy_install pip'. This project requires PRAW and Web.py as dependencies and these can easily be installed via pip. 

- [praw](https://github.com/praw-dev/praw)

In order to install praw just run 


	$ pip install praw

from the command line.

-[web.py](http://webpy.org/)

In order to install web.py just run 

	$ sudo easy_install web.py

or you can download it via git

.. code-block:: bash

	git clone git://github.com/webpy/webpy.git
	ln -s `pwd`/webpy/web .

### How To Use

This project works best when used within its own virtual environment, so as to make sure the dependencies don't interact with previously installed dependencies and projects. 