import fitz
import re
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

file_path = "CV @ 20-05-2025.pdf"
text = extract_text_from_pdf(file_path)
#print(text)


SKILLS_DB = [
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "go", "ruby", "kotlin", "swift", "scala", "rust",
    
    # Web Development
    "html", "css", "javascript", "react", "angular", "vue", "node.js", "express.js", "next.js", "bootstrap", "tailwind css",
    
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

def extract_skills(text):
    text = text.lower()
    skills_found = []
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            skills_found.append(skill)
    return skills_found


skills_have = extract_skills(text)
print("Skills Found: ", skills_have)



