README
WeekDay2 FLask database
# This is to make a new virtual env
D:\Coding_Temple\week5\day1\Project>python -m venv avengers_env


# JUST  DO  THIS to get into the VE
D:\Coding_Temple\week5\day1\Project>avengers_env\scripts\activate.bat



set FLASK_APP=app.py

set FLASK_ENV=development

pip install Flask-WTF

pip install email-validator

pip install Flask-SQLAlchemy Flask-Migrate

flask db init

flask db migrate -m "Create User"

flask db upgrade



Day 3 Commands
pip install flask-mail sendgrid python-dotenv

pip install flask-login

# Ran this after created  users
flask db migrate -m "Create User"

flask db upgrade


 ironman tony im@gmail.com 123456798520

 thor 9999	thor@gmail.com	780-999-5555

Hulk green	hulk@email.com	999-888-7777

# day 4 commands - notes

 # *********** Day 4
#try below if things are weird
 conda deactivate

# to remove a user from the database 
look at Week5  day4 screen shots

 To remove a file from github
git rm --cached app.db - this semmed to remove the app.db from the 

# FOR Herocu

create Procfile file
pip install gunicorn pillow psycopg2

#  this create a text file of all the versions of you modules
pip freeze > requirements.txt 


# handy command - this was the mac command
"/usr/local/bin:$PATH"

gamora  12345 cindy.stevenson1@gmail.com


<h1 style="color:blue;text-align:center;">This is a heading</h1>


# if you get ERROR [root] Error: Target database is not up to date.

$ flask db stamp head
$ flask db migrate
$ flask db upgrade

# to get onto Heroku
create procfile
create requirements list

# FOR Herocu


pip install gunicorn pillow psycopg2

#  this create a text file of all the versions of you modules
pip freeze > requirements.txt 

# *********** Day 4
#try below if things are weird
 conda deactivate

# to remove a user from the database 
look at Week5  day4 screen shots

 To remove a file from github
git rm --cached app.db - this semmed to remove the app.db from the 

# FOR Herocu
Install in virtual env
create Procfile file
pip install gunicorn pillow psycopg2


# *******GITIGNORE .ENV FILE 
#  this create a text file of all the versions of you modules
pip freeze > requirements.txt 

then commit everything to Heorku


# handy command - this was the mac command
"/usr/local/bin:$PATH"

