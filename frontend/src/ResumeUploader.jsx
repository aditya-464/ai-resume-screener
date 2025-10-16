import React, { useState } from "react";

function ResumeUploader({ setResults }) {
  const [jobDesc, setJobDesc] = useState("");
  const [files, setFiles] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!jobDesc || files.length === 0) return;

    const formData = new FormData();
    formData.append("job_description", jobDesc);
    for (let file of files) formData.append("files", file);

    const res = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    if (data.results) setResults(data.results);
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <textarea
        placeholder="Enter Job Description..."
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
        rows={4}
        style={{ width: "100%" }}
      />
      <input
        type="file"
        multiple
        accept=".pdf,.docx,.txt"
        onChange={(e) => setFiles(e.target.files)}
        style={{ marginTop: "10px" }}
      />
      <br />
      <button type="submit" style={{ marginTop: "10px" }}>
        Analyze Resumes
      </button>
    </form>
  );
}

export default ResumeUploader;
