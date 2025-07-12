import axios from "axios";

const API_BASE = "http://localhost:5000"; // Flask backend

// 1️⃣ Upload local HTML form file and get fields/prompts
export const uploadForm = async (file) => {
  const formData = new FormData();
  formData.append("form", file);

  const res = await axios.post(`${API_BASE}/generate-prompts`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data; // { fields, prompts }
};

// 2️⃣ Fetch and parse form fields from a live URL
export const parseURL = async (url) => {
  const res = await axios.post(`${API_BASE}/parse_url`, { url });
  return res.data; // { fields, prompts }
};

// 3️⃣ Translate prompts into a selected language
export const translatePrompts = async (prompts, lang) => {
  const res = await axios.post(`${API_BASE}/translate-prompts`, {
    prompts,
    lang,
  });
  return res.data; // { prompts }
};

// 4️⃣ Send responses to Selenium backend to fill the form
export const fillForm = async (form_url, responses) => {
  const res = await axios.post(`${API_BASE}/fill-form`, {
    form_url,
    responses,
  });
  return res.data; // { message }
};
