// src/App.js

import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import ChatBot from "./components/ChatBot";
import { uploadForm, parseURL, translatePrompts, fillForm } from "./api";

function App() {
  const [step, setStep] = useState("upload");
  const [prompts, setPrompts] = useState([]);
  const [lang, setLang] = useState("en");
  const [formURL, setFormURL] = useState("");
  const [chatResponses, setChatResponses] = useState({});

  const handleRawPrompts = async (raw) => {
    try {
      const { prompts: translated } = await translatePrompts(raw, lang);
      setPrompts(translated);
      setStep("chat");
    } catch (err) {
      console.error("Translation failed:", err);
      alert("❌ Failed to translate prompts");
    }
  };

  const onFileUpload = async (file) => {
    try {
      const { prompts: raw } = await uploadForm(file);
      await handleRawPrompts(raw);
    } catch (err) {
      console.error("File upload error:", err);
      alert("❌ Failed to upload and parse HTML form");
    }
  };

  const onURLParseClick = async () => {
    if (!formURL) return alert("⚠️ Please enter a form URL first");
    try {
      const { prompts: raw } = await parseURL(formURL);
      await handleRawPrompts(raw);
    } catch (err) {
      console.error("URL parse error:", err);
      alert("❌ Failed to fetch or parse the URL");
    }
  };

  const onChatComplete = async (responses) => {
    setChatResponses(responses);
    try {
      await fillForm(formURL || "http://localhost:8000/form_wizard.html", responses);
      setStep("done");
    } catch (err) {
      console.error("Auto-fill error:", err);
      alert("❌ Auto-fill failed");
    }
  };

  return (
    <div style={{ padding: 24, fontFamily: "sans-serif" }}>
      <h1>🧠 Form-to-Convo Chatbot</h1>

      <div style={{ fontSize: "1rem", marginBottom: "1rem" }}>
        Step: <strong>{step === "upload" ? "1. Upload" : step === "chat" ? "2. Chat" : "3. Done"}</strong>
      </div>

      <div style={{ marginBottom: "1.5rem" }}>
        <label>
          🌐 Language:
          <select
            value={lang}
            onChange={(e) => setLang(e.target.value)}
            style={{ padding: "0.4rem", marginLeft: "0.5rem" }}
          >
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="te">Telugu</option>
            <option value="ta">Tamil</option>
            <option value="kn">Kannada</option>
          </select>
        </label>
      </div>

      {step === "upload" && (
        <>
          {/* 🔄 Use the correct prop name expected by UploadForm */}
          <UploadForm onFileSelected={onFileUpload} />

          <hr style={{ margin: "2rem 0" }} />

          <div>
            <h3>🌍 Or Parse from a URL</h3>
            <input
              type="text"
              placeholder="http://localhost:8000/form_wizard.html"
              value={formURL}
              onChange={(e) => setFormURL(e.target.value)}
              style={{ width: 360, padding: 8 }}
            />
            <button
              onClick={onURLParseClick}
              style={{
                marginLeft: 8,
                padding: "0.5rem 1rem",
                backgroundColor: "#007bff",
                color: "white",
                border: "none",
                borderRadius: "4px",
              }}
            >
              Fetch & Generate
            </button>
          </div>
        </>
      )}

      {step === "chat" && <ChatBot prompts={prompts} onComplete={onChatComplete} />}

      {step === "done" && (
        <div style={{ marginTop: 32, textAlign: "center" }}>
          <h2>✅ Form auto-filled and submitted!</h2>
          <pre
            style={{
              textAlign: "left",
              background: "#fafafa",
              padding: 16,
              maxWidth: 600,
              margin: "1rem auto",
              border: "1px solid #ccc",
              borderRadius: "6px",
            }}
          >
            {JSON.stringify(chatResponses, null, 2)}
          </pre>
          <button
            onClick={() => {
              setStep("upload");
              setPrompts([]);
              setFormURL("");
              setChatResponses({});
            }}
            style={{
              marginTop: "1rem",
              padding: "0.6rem 1.2rem",
              backgroundColor: "#28a745",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            🔄 Start Over
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
