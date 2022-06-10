from typing import List
from ddd_votes.adapter.inmemory_vote_repository import InMemoryVoteRepository
from ddd_votes.domain.vote import Vote
from fastapi import FastAPI

app = FastAPI()

vote_repository = InMemoryVoteRepository()

@app.get("/")
def root():
    return {"Message": "Testing the Start"}

@app.post("/vote", response_model=Vote)
def create_vote():
    return Vote().save(vote_repository)

@app.get('/votes', response_model= int)
def get_total_votes():
    return vote_repository.total()

@app.get('/vote_list', response_model= List)
def get_votes_list():
    return vote_repository.all()
