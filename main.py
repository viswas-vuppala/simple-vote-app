from ddd_votes.adapter.inmemory_vote_repository import InMemoryVoteRepository
from ddd_votes.domain.vote import Vote

def main():
    vote_repository = InMemoryVoteRepository()

    Vote().save(vote_repository)
    Vote().save(vote_repository)

    print(vote_repository.all())
    print(f'Total Votes: {vote_repository.total()}')

if __name__ == '__main__':
    main()