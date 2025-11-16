# from flask import Blueprint, render_template, request
# from app.researcher_agent import run_research

# # Create a Blueprint (so it can be registered in __init__.py)
# main_bp = Blueprint("main", __name__)

# @main_bp.route("/", methods=["GET", "POST"])
# def index():
#     result = None
#     if request.method == "POST":
#         query = request.form.get("query", "")
#         if query:
#             ai_response = run_research(query)
#             result = {"summary": ai_response}

#     return render_template("index.html", result=result)


from flask import Blueprint, render_template, request
from app.researcher_agent import run_research

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        if query:
            ai_response = run_research(query)

            # --- Split sections by numbered markers ---
            sections = ai_response.split("2️⃣")
            plan = []
            summary = ai_response  # fallback

            if len(sections) > 1:
                # Split plan part into bullet points
                plan_text = sections[0].replace("<br>", "\n")
                plan = [line.strip() for line in plan_text.split("\n") if line.strip() and not line.startswith("1️⃣")]
                summary = "2️⃣" + sections[1]

            result = {
                "plan": plan,
                "summary": summary
            }

    return render_template("index.html", query=query, result=result)
