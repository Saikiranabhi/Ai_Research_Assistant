from app.planner_agent import plan_research
from app.researcher_agent import run_research
from app.summarizer_agent import summarize
from app.utils import hash_text

def run_agentic_research(query: str):
    """
    Orchestrates the planner -> researcher -> summarizer pipeline.
    Returns a dict with plan, results, and summary.
    """
    plan = plan_research(query)
    results = []

    for step in plan:
        result = run_research(step)
        results.append(result)

    summary = summarize(results)

    return {
        "query": query,
        "id": hash_text(query),
        "plan": plan,
        "results": results,
        "summary": summary
    }
