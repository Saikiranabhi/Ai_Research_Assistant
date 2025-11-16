# import os
# import re

# try:
#     import google.generativeai as genai
#     genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#     _MODEL = genai.GenerativeModel("gemini-2.0-flash")
# except Exception:
#     genai = None
#     _MODEL = None


# def run_research(task: str) -> str:
#     """
#     Call Gemini to perform the single research task.
#     If Gemini isn't configured, return a placeholder message.
#     Ensures clean output matching the style of 'Research Plan'.
#     """
#     if _MODEL is None:
#         return f"[offline placeholder] Would research: {task}"

#     try:
#         prompt = f"""
#         Research the topic "{task}" and structure the response into **three clear sections**:

#         1. Produce a concise explanation of the key concepts behind the topic.
#         2. List recent developments, papers, or notable resources.
#         3. Summarize potential future directions and open questions.

#         Format Rules:
#         - Use clear numbered sections (1, 2, 3).
#         - Each point should start with a star (*) and numeric index where needed.
#         - Do NOT include brackets [], escape characters, or code formatting.
#         - Return plain readable text — ready for HTML rendering.
#         """

#         response = _MODEL.generate_content(prompt)
#         text = getattr(response, "text", None)
#         if not text:
#             text = response.get("content", {}).get("text", "") if isinstance(response, dict) else str(response)

#         # Remove unwanted characters like \n, [, ], ', and excessive spaces
#         cleaned = (
#             text.replace("\\n", "\n")
#             .replace("[", "")
#             .replace("]", "")
#             .replace("'", "")
#             .strip()
#         )

#         # Collapse multiple blank lines to a single line break
#         cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

#         # Ensure each line starts properly formatted
#         lines = [line.strip() for line in cleaned.split("\n") if line.strip()]
#         formatted = "\n".join(lines)

#         # Convert newlines to HTML <br> for display
#         html_ready = formatted.replace("\n", "<br>")

#         return html_ready or f"[no text] {task}"

#     except Exception as e:
#         return f"[error contacting Gemini] {str(e)}"


import os
import re

try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    _MODEL = genai.GenerativeModel("gemini-2.0-flash")
except Exception:
    genai = None
    _MODEL = None


def run_research(task: str) -> str:
    """
    Perform a structured research query using Gemini.
    Returns a clean, HTML-ready summary in the 'Research Plan' format.
    """
    if _MODEL is None:
        return f"[offline placeholder] Would research: {task}"

    try:
        prompt = f"""
        Research the topic "{task}" and structure your answer into three clearly separated sections:

        1️⃣ **Key Concepts**
        * Provide a concise explanation of the main ideas and background.

        2️⃣ **Recent Developments, Papers & Notable Resources**
        * Summarize the most recent research, advancements, or tools.

        3️⃣ **Future Directions & Open Questions**
        * Outline potential future research areas, challenges, and open problems.

        Format & Style Rules:
        - Each major section must be clearly numbered (1️⃣, 2️⃣, 3️⃣).
        - Each individual point should begin with a star (*) followed by a numeric index where needed.
        - Keep the writing crisp, formal, and easily scannable.
        - Remove any code formatting, escape sequences (\\n, \\t), or unnecessary brackets.
        - Final output must be clean, structured, and ready for HTML rendering.
        """

        # Generate from Gemini model
        response = _MODEL.generate_content(prompt)
        text = getattr(response, "text", None)
        if not text:
            text = (
                response.get("content", {}).get("text", "")
                if isinstance(response, dict)
                else str(response)
            )

        # --- Clean and format output ---
        cleaned = (
            text.replace("\\n", "\n")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .strip()
        )

        # Collapse multiple blank lines → single blank line
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

        # Clean up spacing & stray symbols
        lines = [line.strip() for line in cleaned.split("\n") if line.strip()]
        formatted = "\n".join(lines)

        # Replace newlines with <br> for HTML display
        html_ready = formatted.replace("\n", "<br>")

        return html_ready or f"[no text] {task}"

    except Exception as e:
        return f"[error contacting Gemini] {str(e)}"
