import torch
from transformers import pipeline
from fastapi import FastAPI, Request

# Define the model and revision explicitly for consistency
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
REVISION = "a4f8f3e"

# Initialize FastAPI app
app = FastAPI()

# Load summarization pipeline
summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    revision=REVISION,
    device=0 if torch.cuda.is_available() else -1  # Use GPU if available
)

# Define POST endpoint
@app.post("/summarize")
async def summarize(request: Request):
    payload = await request.json()
    text = payload.get("text", "")

    if not text:
        return {"error": "Missing 'text' field in request body."}

    summary_output = summarizer(
        text,
        max_length=50,
        min_length=10,
        do_sample=False
    )

    return {"summary": summary_output[0]["summary_text"]}
