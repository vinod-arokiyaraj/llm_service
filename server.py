from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import summarize_text
from utils import load_config

app = FastAPI(title="LLM Summarization Service 🚀")

class SummarizeRequest(BaseModel):
    prompt: str
    max_length: int = 130
    min_length: int = 30

@app.post("/summarize/")
async def summarize_endpoint(request: SummarizeRequest):
    try:
        summary = summarize_text(request.prompt, request.max_length, request.min_length)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    config = load_config()
    uvicorn.run(app, host="0.0.0.0", port=config.get("port", 8001))
