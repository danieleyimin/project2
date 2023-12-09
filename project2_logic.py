class VoteLogic:
    def __init__(self):
        self.candidates = {
            1: "Cameron",
            2: "Allison",
            3: "Diego"
        }
        self.vote_count = {candidate: 0 for candidate in self.candidates.values()}

    def cast_vote(self, candidate_id):
        self.vote_count[self.candidates[candidate_id]] += 1

    def get_results(self):
        return self.vote_count
