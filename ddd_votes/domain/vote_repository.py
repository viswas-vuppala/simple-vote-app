import abc
from typing import List

from ddd_votes.domain.vote import Vote


class VoteRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, vote: Vote) -> Vote:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Vote]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError