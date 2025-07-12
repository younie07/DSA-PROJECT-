from flask import Flask, render_template, request, url_for
from leetcode_scraper import get_leetcode_solved
from recommendation_leetcode import recommend_leetcode_problems

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    username = request.form.get("username", "").strip()
    topic = request.form.get("topic", "").strip()
    difficulty = request.form.get("difficulty", "").strip()

    # Check for missing inputs
    if not username or not topic or not difficulty:
        return render_template("index.html", error="All fields are required.")

    try:
        user_data = get_leetcode_solved(username)

        solved = user_data["solved"]
        total_problems = user_data["total_problems"]
        easy = user_data["easy"]
        medium = user_data["medium"]
        hard = user_data["hard"]

        recommendations = recommend_leetcode_problems(user_data["solved_list"], topic, difficulty)

        return render_template("results.html",
            username=username,
            solved=solved,
            total_problems=total_problems,
            easy=easy,
            medium=medium,
            hard=hard,
            filtered_count=len(recommendations),
            topic=topic,
            difficulty=difficulty,
            recs=recommendations
        )

    except Exception as e:
        # Show a friendly message if scraper or recommender fails
        return render_template("index.html", error=f"Error: {str(e)}")

# ✅ Required to run the server locally
if __name__ == "__main__":
    app.run(debug=True)
