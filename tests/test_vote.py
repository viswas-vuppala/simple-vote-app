import uuid

from ddd_votes.vote import Vote

def test_vote_existing_vote_id():
    vote_id = str(uuid.uuid4())

    assert Vote(vote_id).vote_id == vote_id


def test_vote_defaults():
    vote_id = str(uuid.uuid4())

    assert Vote().vote_id != vote_id