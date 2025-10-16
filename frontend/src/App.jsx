import React, { useState } from "react";
import ResumeUploader from "./ResumeUploader.jsx";

function App() {
  const [results, setResults] = useState([]);

  return (
    <div style={{ padding: "20px" }}>
      <h2>📝 AI Resume Screener</h2>
      <ResumeUploader setResults={setResults} />
      <ul>
        {results.map((r, idx) => (
          <li key={idx}>
            {r.filename}: {r.score.toFixed(3)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
