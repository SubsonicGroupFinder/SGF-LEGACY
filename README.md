# SGI-web-app

The aim of this project is to produce a cross platform looking for group app or LFG for short. It is called Gate Link LFG and will be aimed at gamers so will have a number of functions that will allow users to find other players on their platform and game so that they can play together. We are currently working on a web app that will have feeds showing who is looking for a group and allow users to filter the feeds to find what they are looking for.

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
  * Python3 Django for the back end
  * React, HTML, CSS, JS for the front end
  * Database - undecided
  * server - undecided
  
## Dev Environement
  * make sure that you have python3 installed
  * as well as react, node, and npm
  * the virtual environment for the backend is handled with pipenv
  * so do some version of ```sudo apt-get install pipenv```
  * clone the repo
  * ```cd SGI-web-app```
  * ```cd backend/```
  * ```pipenv install```
  * ```pipenv shell```
  * ```cd webapp_api```
  * ```python3 manage.py runserver```
  * ```cd ../..```
  * ```cd frontend```
  * ```npm install```
  * ```npm start```

This should start both of the servers that you need to have going. The backend will be on localhost:8000 and the frontend will be on localhost:3000. The back is only an api.

This is just a start to get the environment set up, meaning that the only react files are for "App" App.js is the file that has been edited.


