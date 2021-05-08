# SGF-web-app

The aim of this project is to produce a cross platform looking for group app or LFG for short. It is called Subsonic Group Finder and will be aimed at gamers so will have a number of functions that will allow users to find other players on their platform and game so that they can play together. We are currently working on a web app that will have feeds showing who is looking for a group and allow users to filter the feeds to find what they are looking for.

This project is a group project, though it was started by SS-git-dev. 

## Acronyms 
  * LFG- Looking for Group
  * SS- Subsonic Syndicate, a community that will be using this service
  * 2FA- 2 factor authentication
  * SEO- Search Engine optimization

## Goals
  * Clean, sustainable, code that can be passed on to the next person
  * Team cooperation
  * Respecting everyone's abilities and ideas
  * Learning new things
  * Fun
  
## Tech Stack
  * Python3 Django for the backend
  ** All apps in django are api's there are no templates
  * React, HTML, CSS, JS for the front end
  * Database - SQL/mySQL
  * server - cpanel/goDaddy
  
## Dev Environement
  * make sure that you have python3 installed
  * as well as react, node, and npm
  * the virtual environment for the backend is handled with pipenv
  * so do some version of ```sudo apt-get install pipenv```
  * clone the repo
  * ```cd SGF-web-app```
  * ```cd backend/```
  * ```pipenv install```
  * ```pipenv shell```
  * ```cd webapp_api```
  * ```python3 manage.py runserver```
  * ```cd ../..```
  * ```cd frontend```
  * ```npm install```
  * ```npm start```

## Backend:
  After you activate the enviornment and get there server running here are the endpoints we have at the current moment:
  
  - http://127.0.0.1:8000/api/v1/custom/register/
  - http://127.0.0.1:8000/api/v1/custom/verify-email/ - Not Valid Yet

  - http://127.0.0.1:8000/api/v1/custom/user/
  - http://127.0.0.1:8000/api/v1/custom/login/
  - http://127.0.0.1:8000/api/v1/custom/logout/
  

  - http://127.0.0.1:8000/api/v1/custom/password/reset/ - Not Valid Yet
  - http://127.0.0.1:8000/api/v1/custom/password/reset/confirm/ -Not Valid Yet
  - http://127.0.0.1:8000/api/v1/custom/password/reset/change/

**Note**: you may have to do some migrations stuff for django to get the things working

If things get weird don't be afraid to delete the migration in users and the sqlite db.  *** This is fine for now but once we get rolling do not touch the migrations***



This should start both of the servers that you need to have going. The backend will be on localhost:8000 and the frontend will be on localhost:3000. The back is only an api.

This is just a start to get the environment set up, meaning that the only react files are for "App" App.js is the file that has been edited.


