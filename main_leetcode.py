import json
from leetcode_scraper import get_leetcode_solved
from recommendation_leetcode import recommend_leetcode_problems




# ✅ Load LeetCode dataset
with open("leetcode_problemset.json", "r", encoding="utf-8") as f:
    leetcode_data = json.load(f)


# =========================
# ✅ LEETCODE RECOMMENDER
# =========================
lc_user = input("\nEnter LeetCode username: ")
solved_lc = get_leetcode_solved(lc_user)

topic_lc = input("\n[LC] Enter topic: ")
difficulty_lc = input("[LC] Enter difficulty (Easy/Medium/Hard): ").capitalize()

recs_lc = recommend_leetcode_problems(solved_lc, topic_lc, difficulty_lc)
print("\n📌 LeetCode Recommendations:")
if recs_lc:
    for i, p in enumerate(recs_lc, 1):
        print(f"{i}. {p['title']} ({p['difficulty']}) - Link: {p.get('url', '-')}")
else:
    print("❌ No recommendations found for the given topic and difficulty.")
