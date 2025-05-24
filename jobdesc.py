import re

# === SKILLS DATABASE ===
SKILLS_DB = [
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "go", "ruby", "kotlin", "swift", "scala", "rust",
     # Web Development
    "html", "css", "react", "angular", "vue", "node.js", "express.js", "next.js", "bootstrap", "tailwind css",
     # Backend & Frameworks
    "django", "flask", "spring", "fastapi", "laravel", ".net", "asp.net", "rails",
      # Databases
    "sql", "mysql", "postgresql", "oracle", "sqlite", "mongodb", "firebase", "redis", "cassandra", "dynamodb",
      # DevOps & Tools
    "git", "github", "bitbucket", "gitlab", "docker", "kubernetes", "jenkins", "ansible", "terraform", "ci/cd",
     # Operating Systems & Shell
    "linux", "bash", "unix", "windows", "powershell",
    # Cloud Platforms
    "aws", "azure", "google cloud", "gcp", "heroku", "netlify", "vercel", "digitalocean",
     # Data Science & ML
    "numpy", "pandas", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "keras", "pytorch", "xgboost", "statsmodels",
    "openai", "huggingface", "langchain", "llm", "transformers", "cv2", "opencv", "nlp", "spacy", "gensim",
      # Data Engineering
    "hadoop", "spark", "hive", "pig", "airflow", "kafka", "databricks", "snowflake",
    # Tools & Editors
    "vscode", "pycharm", "intellij", "jupyter", "colab", "postman", "swagger",
     # APIs
    "rest", "graphql", "soap", "json", "xml",
    # Cybersecurity
    "nmap", "wireshark", "metasploit", "kali linux", "burp suite", "owasp", "hashing", "encryption",
     # Software Engineering Concepts
    "oop", "design patterns", "data structures", "algorithms", "version control", "unit testing", "agile", "scrum",
     # Other Skills
    "web scraping", "beautifulsoup", "selenium", "regex", "jwt", "oauth", "firebase", "sqlite3",
     # Soft/Business Skills (optional)
    "communication", "leadership", "teamwork", "project management", "time management"
]

# === SKILL MATCHING FUNCTION ===
def extract_skills_from_jd(jd_text, skill_list):
    jd_text = jd_text.lower()
    found_skills = []
    for skill in skill_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, jd_text):
            found_skills.append(skill)
    return found_skills

# === USER INPUT ===
print("🔹 Enter your Job Description :\n")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

job_description = " ".join(lines)

# === PROCESS ===
matched_skills = extract_skills_from_jd(job_description, SKILLS_DB)

# === OUTPUT ===
print("\n✅ Extracted Skills:")
for skill in matched_skills:
    print("-", skill)
