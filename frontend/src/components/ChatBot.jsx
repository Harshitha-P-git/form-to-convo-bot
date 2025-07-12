// src/components/ChatBot.jsx
import React, { useState } from "react";

export default function ChatBot({ prompts, onComplete }) {
  const [responses, setResponses] = useState({});
  const [index, setIndex] = useState(0);
  const [answer, setAnswer] = useState("");
  const [error, setError] = useState("");

  // 🛡️ Safety check: prevent crashing if prompts is invalid or empty
  if (!Array.isArray(prompts) || prompts.length === 0) {
    return (
      <div style={{ textAlign: "center", marginTop: "2rem", color: "red" }}>
        ❌ No prompts to display.
      </div>
    );
  }

  const current = prompts[index];

  const handleNext = () => {
    if (!answer.trim()) {
      setError("❗ Please provide a response.");
      return;
    }

    const updated = { ...responses, [current.field_name]: answer.trim() };
    setResponses(updated);
    setAnswer("");
    setError("");

    if (index + 1 < prompts.length) {
      setIndex(index + 1);
    } else {
      onComplete(updated);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.chatBox}>
        <p style={styles.question}>{current.question}</p>
        <input
          type="text"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          style={styles.input}
          placeholder="Type your answer here..."
        />
        {error && <p style={styles.error}>{error}</p>}
        <button onClick={handleNext} style={styles.button}>
          {index + 1 < prompts.length ? "Next ➡️" : "Submit 🚀"}
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "80vh",
    background: "#f5f5f5",
  },
  chatBox: {
    background: "#fff",
    padding: "2rem",
    borderRadius: "8px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
    width: "60%",
    maxWidth: "600px",
    textAlign: "center",
  },
  question: {
    fontSize: "1.5rem",
    marginBottom: "1rem",
    color: "#222",
  },
  input: {
    padding: "0.75rem",
    width: "100%",
    borderRadius: "4px",
    border: "1px solid #ccc",
    fontSize: "1rem",
    marginBottom: "1rem",
  },
  button: {
    padding: "0.75rem 1.5rem",
    fontSize: "1rem",
    background: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  error: {
    color: "red",
    marginBottom: "0.5rem",
  },
};
