# def summarize(results):
#     """
#     Combine researcher outputs and create a short summary.
#     Keep simple — replace with a Gemini summarizer later if desired.
#     """
#     if not results:
#         return "No results to summarize."

#     combined = "\n\n".join(results)
#     # keep result length manageable for display
#     if len(combined) > 3000:
#         combined = combined[:3000] + "\n\n...[truncated]"

#     return combined


import re

def summarize(results):
    """
    Combine researcher outputs into a clean, numbered summary.
    The result matches the 'Research Plan' style with clear sections.
    """
    if not results:
        return "No results to summarize."

    # Combine all results into one large text block
    combined = "\n\n".join(results)

    # Trim overly long responses
    if len(combined) > 3000:
        combined = combined[:3000] + "\n\n...[truncated]"

    # Clean unwanted characters
    cleaned = (
        combined.replace("\\n", "\n")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .strip()
    )

    # Collapse multiple blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    # Format output as structured Research Plan summary
    summary_template = f"""
1️⃣ **Key Concepts**
{cleaned.split('**I.')[0].strip() if '**I.' in cleaned else cleaned[:1000].strip()}

2️⃣ **Recent Developments, Papers & Resources**
{extract_section(cleaned, 'I.', 'II.')}

3️⃣ **Future Directions & Open Questions**
{extract_section(cleaned, 'II.', 'III.')}
""".strip()

    # Replace newlines with <br> for HTML rendering
    html_ready = summary_template.replace("\n", "<br>")

    return html_ready


def extract_section(text, start_marker, end_marker):
    """
    Extract a section of text between two markers.
    Example: extract_section(text, 'I.', 'II.')
    """
    pattern = re.compile(rf"\*\*{start_marker}(.*?)\*\*{end_marker}", re.S)
    match = pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        # fallback — return approximate portion if markers missing
        parts = text.split(f"**{start_marker}")
        if len(parts) > 1:
            section = parts[1]
            if f"**{end_marker}" in section:
                section = section.split(f"**{end_marker}")[0]
            return section.strip()
    return "[Not found]"
