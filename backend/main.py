from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from form_parser import fetch_html_from_url, parse_form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Form Parser API")

# Allow all origins for now (for frontend like React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.post("/parse-form")
async def parse_form_from_url(request: URLRequest):
    try:
        html = fetch_html_from_url(request.url)
        fields = parse_form(html)
        return {"status": "success", "fields": fields}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
