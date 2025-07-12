import requests

def get_leetcode_solved(username):
    url = "https://leetcode-stats-api.herokuapp.com/" + username
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or ("status" in data and data["status"] == "error"):
        print("❌ Invalid LeetCode username or API error")
        return {
            "solved": 0,
            "total_problems": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
            "solved_list": []
        }

    print(f"\n👤 LeetCode Profile for: {username}")
    print(f"✅ Solved: {data['totalSolved']} / {data['totalQuestions']}")
    print(f"🌟 Easy: {data['easySolved']} | Medium: {data['mediumSolved']} | Hard: {data['hardSolved']}")

    # Dummy solved list (can be replaced with actual problems if needed)
    solved_dummy = [
        {"title": "Two Sum", "difficulty": "Easy", "url": "https://leetcode.com/problems/two-sum"},
        {"title": "Merge Intervals", "difficulty": "Medium", "url": "https://leetcode.com/problems/merge-intervals"},
        {"title": "Trapping Rain Water", "difficulty": "Hard", "url": "https://leetcode.com/problems/trapping-rain-water"},
    ]

    return {
        "solved": data['totalSolved'],
        "total_problems": data['totalQuestions'],
        "easy": data['easySolved'],
        "medium": data['mediumSolved'],
        "hard": data['hardSolved'],
        "solved_list": solved_dummy  # optional if you want to filter these
    }
