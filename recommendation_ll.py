class Problem:
    def __init__(self, name, topic, difficulty):
        self.name = name
        self.topic = topic
        self.difficulty = difficulty

def recommend_problems_cf_ll(solved_set, topic, difficulty, problemset):
    recommended = []
    for prob in problemset:
        if not all(k in prob for k in ("topic", "difficulty", "name", "contestId", "index")):
            continue

        if (
            prob["topic"].lower() == topic.lower()
            and prob["difficulty"].lower() == difficulty.lower()
            and (prob["contestId"], prob["index"]) not in solved_set
        ):
            recommended.append(Problem(prob["name"], prob["topic"], prob["difficulty"]))
    return recommended
