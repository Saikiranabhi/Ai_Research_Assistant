def plan_research(query: str):
    """
    Simple planner: break a research request into 3 tasks.
    You can later replace with a more advanced planner.
    """
    return [
        f"Produce a concise explanation of the key concepts behind: {query}",
        f"List recent developments, papers, or notable resources about: {query}",
        f"Summarize potential future directions and open questions for: {query}"
    ]
