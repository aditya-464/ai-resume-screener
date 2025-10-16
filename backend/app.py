import os
import tempfile
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from resume_processor import allowed_file, extract_text, rank_resumes

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50MB

@app.route("/upload", methods=["POST"])
def upload_resumes():
    """
    Upload multiple resumes along with a job description.
    Returns top-ranked candidates.
    """
    if "files" not in request.files or "job_description" not in request.form:
        return jsonify({"error": "Provide files and job_description"}), 400

    files = request.files.getlist("files")
    job_description = request.form["job_description"]

    saved_files = []
    tmpdir = tempfile.mkdtemp()
    for file in files:
        if file.filename == "" or not allowed_file(file.filename):
            continue
        filename = secure_filename(file.filename)
        path = os.path.join(tmpdir, filename)
        file.save(path)
        saved_files.append((filename, path))

    if not saved_files:
        return jsonify({"error": "No valid files uploaded"}), 400

    results = rank_resumes(job_description, saved_files)
    return jsonify({"results": results}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
