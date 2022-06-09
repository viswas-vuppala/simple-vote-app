## This is the implmentation of the vote_repository
from typing import List
from ddd_votes.domain.vote import Vote
from ddd_votes.domain.vote_repository import VoteRepository


class InMemoryVoteRepository(VoteRepository):
    def __init__(self):
        self.votes = []

    def add(self, vote: Vote) -> Vote:
        self.votes.append(vote)
        return vote

    def all(self) -> List[Vote]:
        return self.votes

    def total(self) -> int:
        return len(self.votes)
