class Username:
    def __init__(self, contests, scores):
        self.contests = contests 
        self.scores = scores 
        self.check = self.scores[0]
        self.amazings = 0
    def main(self):
        # check = self.scores[0]
        for i in range(len(self.scores[1:])):
            if self.scores[i] > self.check:
                self.amazings += 1
                self.check = self.scores[i]
            else:
                self.check = self.scores[i]
                continue 

        print(self.amazings)

    
    def __repr__(self):
        return """A usernameclass that checks amazing performances 
        counts and reports back to user!"""


if __name__ == '__main__':
    contests = int(input())
    scores = [int(x) for x in input().split()]
    username = Username(contests, scores)
    print(username)