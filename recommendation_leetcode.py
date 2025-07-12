import json
import random

# ✅ Step 1: ADD this helper function
def extract_striver_problems(json_data):
    problems = []
    for step, lectures in json_data.items():
        for lecture, prob_list in lectures.items():
            for prob in prob_list:
                title = prob.get("Problem", "").strip()
                difficulty = prob.get("Difficulty", "").strip()
                url = prob.get("Problem_link") or prob.get("col3_link") or "-"
                if title and difficulty:
                    problems.append({
                        "title": title,
                        "difficulty": difficulty.capitalize(),
                        "tags": [step.lower(), lecture.lower()],
                        "url": url
                    })
    return problems

# ✅ Step 2: KEEP your main function as-is but modify like this
def recommend_leetcode_problems(solved_problems, topic="array", difficulty="Easy"):
    topic = topic.lower().strip()
    difficulty = difficulty.capitalize().strip()

    with open("leetcode_problemset.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    problems = extract_striver_problems(raw_data)

    solved_titles = {p["title"] for p in solved_problems}
    filtered = []

    for prob in problems:
        if (
            prob["title"] not in solved_titles and
            difficulty == prob["difficulty"] and
            any(topic in t for t in prob["tags"])
        ):
            filtered.append(prob)

    print(f"✅ Filtered {len(filtered)} problems matching topic '{topic}' and difficulty '{difficulty}'.")

    if not filtered:
        print("⚠️ No matching problems found.")

    return random.sample(filtered, min(5, len(filtered)))
