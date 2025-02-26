from transformers import pipeline
from utils import load_config

config = load_config()
MODEL_NAME = config.get("default_model", "facebook/bart-large-cnn")

# Load summarizer using Hugging Face pipeline (without use_auth_token)
def load_summarizer():
    return pipeline("summarization", model=MODEL_NAME)

summarizer = load_summarizer()

def summarize_text(text, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]["summary_text"]
