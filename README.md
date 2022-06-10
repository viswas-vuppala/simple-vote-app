# Simple Voting Project
The purpose of this project was to create a simple application that creates unique votes and stores them in a repository. 

## Set Up Instructions
1. clone this repository on your computer
2. create a new virtual enviornement by using 'poetry shell'
3. Once you're in the virtual env, install packages with 'poetry install'
4. to run the app type in `uvicorn ddd_votes.main:app --reload` in the command line
5. Click on the link and eidt the url to be "http://....../docs"

## Ports and Adapters
We use a ports and adapters architecture. 
1. The main center hexagon is the domain foler. We have vote.py and vote_repository.py
2. Then we create an adapter for the vote_repository, which acts as the implementation for the repository specific to this "hexagaon"
3. Then we use fastapi to quickly create a swagger doc UI for the drivers side

## Dependencies
We are using poetry to manage dependencies and they can be seen in the .toml file