import os

# Define the folder structure
structure = {
    "app": [
        "__init__.py",
        "main.py",
        "planner_agent.py",
        "researcher_agent.py",
        "summarizer_agent.py",
        "coordinator.py",
        "utils.py"
    ],
    "templates": [
        "index.html"
    ],
    "static/css": [
        "style.css"
    ],
    "venv": [],  # virtual environment folder (placeholder)
    "": [
        "app.py",
        "requirements.txt",
        "Dockerfile",
        ".dockerignore",
        ".gitignore",
        ".env",
        "README.md"
    ]
}

# Create directories and empty files
for folder, files in structure.items():
    if folder:
        os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, "w", encoding="utf-8") as f:
            pass  # create empty file

print("✅ Full Agentic AI Research project template created successfully!")
