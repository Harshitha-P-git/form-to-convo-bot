// src/components/UploadForm.jsx
import React, { useState } from "react";

export default function UploadForm({ onFileSelected }) {
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    if (selected && selected.name.endsWith(".html")) {
      setFile(selected);
      setError("");
    } else {
      setFile(null);
      setError("❌ Please select a valid .html file.");
    }
  };

  const handleUpload = () => {
    if (!file) {
      setError("⚠️ Please select an HTML file first.");
      return;
    }
    onFileSelected(file); // 🔄 Let App.js handle upload logic
  };

  return (
    <div style={{ marginBottom: "1.5rem" }}>
      <h3>📂 Upload your HTML form</h3>
      <input type="file" accept=".html" onChange={handleFileChange} />
      <button
        onClick={handleUpload}
        disabled={!file}
        style={{
          marginLeft: "1rem",
          padding: "0.5rem 1rem",
          backgroundColor: "#007bff",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: !file ? "not-allowed" : "pointer",
        }}
      >
        Upload Form
      </button>
      {error && <p style={{ color: "red", marginTop: "0.5rem" }}>{error}</p>}
    </div>
  );
}
