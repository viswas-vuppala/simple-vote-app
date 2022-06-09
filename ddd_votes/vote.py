from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    #Preventing the circular import problem
    from ddd_votes.vote_repository import VoteRepository

@dataclass
class Vote:
    vote_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, vote_repository: 'VoteRepository'):
        return vote_repository.add(self)

    def __hash__(self):
        return hash(self.vote_id)
