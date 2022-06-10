from ddd_votes.adapter.inmemory_vote_repository import InMemoryVoteRepository
from ddd_votes.domain.vote import Vote
from fastapi import FastAPI

app = FastAPI()

vote_repository = InMemoryVoteRepository()

@app.get("/")
def root():
    return {"Message": "Testing the Start"}
