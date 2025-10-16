import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile
import docx
import pypdf

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"pdf", "docx", "txt"}

def extract_text_from_pdf(path):
    text = []
    reader = pypdf.PdfReader(path)
    for page in reader.pages:
        try:
            text.append(page.extract_text() or "")
        except:
            continue
    return "\n".join(text)

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text(path):
    ext = path.rsplit(".", 1)[1].lower()
    if ext == "pdf":
        return extract_text_from_pdf(path)
    elif ext == "docx":
        return extract_text_from_docx(path)
    else:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

def rank_resumes(job_description, files):
    """
    job_description: str
    files: list of tuples [(filename, path), ...]
    Returns: list of dicts with filename and similarity score
    """
    job_emb = model.encode([job_description])
    results = []

    for filename, path in files:
        text = extract_text(path)
        resume_emb = model.encode([text])
        score = float(cosine_similarity(job_emb, resume_emb)[0][0])
        results.append({"filename": filename, "score": score})

    # Sort descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
